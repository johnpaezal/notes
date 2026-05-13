# CDK Patterns

## Environment Configuration

*Bind stack to account and region.*

```python
# app.py
import aws_cdk as cdk
import os

app = cdk.App()

env_prod = cdk.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"],
    region=os.environ["CDK_DEFAULT_REGION"],
)

MyAppStack(app, "MyAppStack-Prod", env=env_prod)

app.synth()
```

**CDK_DEFAULT_ACCOUNT** – Set by `aws sts get-caller-identity`.  
**CDK_DEFAULT_REGION** – Set by AWS CLI profile or env var.  
Omitting `env` = environment-agnostic stack (no account/region-specific lookups).  

---

## Multi-Stack Pattern

*Share VPC across stacks.*

```python
# app.py
vpc_stack = VpcStack(app, "VpcStack", env=env)
app_stack = AppStack(app, "AppStack", vpc=vpc_stack.vpc, env=env)
app_stack.add_dependency(vpc_stack)

# vpc_stack.py
class VpcStack(cdk.Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)
        self.vpc = ec2.Vpc(self, "SharedVpc", max_azs=2)

# app_stack.py
class AppStack(cdk.Stack):
    def __init__(self, scope, id, vpc: ec2.Vpc, **kwargs):
        super().__init__(scope, id, **kwargs)
        # use passed vpc directly
```

**`from_lookup`** – Import existing VPC by ID/tags (requires bootstrap):
```python
vpc = ec2.Vpc.from_lookup(self, "Vpc", vpc_id="vpc-0abc123")
```

---

## Custom Construct: LambdaWithDLQ

*Reusable Lambda + SQS DLQ construct.*

```python
from constructs import Construct
from aws_cdk import aws_lambda as _lambda, aws_sqs as sqs, Duration

class LambdaWithDlq(Construct):

    def __init__(self, scope: Construct, id: str,
                 code_path: str, handler: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.dlq = sqs.Queue(
            self, "DLQ",
            retention_period=Duration.days(14),
        )

        self.function = _lambda.Function(
            self, "Fn",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler=handler,
            code=_lambda.Code.from_asset(code_path),
            dead_letter_queue=self.dlq,
            retry_attempts=2,
        )

# Usage in a Stack:
# processor = LambdaWithDlq(self, "Processor", code_path="lambda", handler="app.main")
# processor.function.grant_invoke(some_other_resource)
```

---

## RemovalPolicy

*Control resource deletion behavior.*

**`RemovalPolicy.RETAIN`** – Default for stateful resources (S3, RDS, DynamoDB); resource stays after `cdk destroy`.  
**`RemovalPolicy.DESTROY`** – Delete resource on `cdk destroy`; use in dev/test only.  
**`RemovalPolicy.SNAPSHOT`** – RDS/ElastiCache; creates snapshot before deletion.  

```python
# Dev stack: destroy everything
bucket = s3.Bucket(self, "DevBucket", removal_policy=RemovalPolicy.DESTROY)

# Prod stack: retain data
bucket = s3.Bucket(self, "ProdBucket", removal_policy=RemovalPolicy.RETAIN)
```

---

## SSM Parameter Store: Sharing Values Between Stacks

*Cross-stack values via SSM.*

```python
from aws_cdk import aws_ssm as ssm

# Stack A: write
ssm.StringParameter(
    self, "VpcIdParam",
    parameter_name="/myapp/prod/vpc-id",
    string_value=vpc.vpc_id,
)

# Stack B: read (same account/region, no dependency needed)
vpc_id = ssm.StringParameter.value_for_string_parameter(
    self, "/myapp/prod/vpc-id"
)
```

---

## Best Practices

*CDK usage guidelines.*

**One stack per environment** – Deploy separate stacks for dev/staging/prod.  
**Prefer L2 over L1** – L2 generates least-privilege IAM automatically.  
**No hardcoded account IDs** – Use `cdk.Aws.ACCOUNT_ID` or env vars.  
**Use `from_lookup` for existing resources** – Import VPCs, hosted zones without recreating them.  
**Always `cdk diff` before `cdk deploy`** – Review changes before applying.  
**Destroy vs Retain** – Default to `RETAIN` for production data, `DESTROY` for dev.  
**Separate stateful and stateless stacks** – Reduces risk of accidental data deletion.  
