# CDK Constructs

## L1 vs L2 vs L3

*Three abstraction levels explained.*

**L1 (Cfn prefix)** – 1:1 CloudFormation resource; no defaults; full control.  
**L2** – Curated constructs with sensible defaults; type-safe; hides boilerplate.  
**L3 (Patterns)** – Complete solutions combining multiple L2 constructs.  

| Level | Prefix example | Abstraction | When to use |
|---|---|---|---|
| L1 | `CfnBucket` | Raw CloudFormation | Need unsupported property |
| L2 | `Bucket` | Opinionated defaults | Most use cases |
| L3 | `ApplicationLoadBalancedFargateService` | Full pattern | Quick production setups |

---

## L2: S3 Bucket

*Bucket with versioning and cleanup.*

```python
from aws_cdk import aws_s3 as s3, RemovalPolicy

bucket = s3.Bucket(
    self, "AppBucket",
    versioned=True,
    removal_policy=RemovalPolicy.DESTROY,   # delete bucket on cdk destroy
    auto_delete_objects=True,               # empty bucket before deleting
    encryption=s3.BucketEncryption.S3_MANAGED,
)

# Usage: bucket.bucket_name, bucket.bucket_arn
```

---

## L2: VPC

*VPC with subnets and NAT.*

```python
from aws_cdk import aws_ec2 as ec2

vpc = ec2.Vpc(
    self, "AppVpc",
    max_azs=2,
    nat_gateways=1,                          # 0 = no NAT, saves cost in dev
    subnet_configuration=[
        ec2.SubnetConfiguration(
            name="Public",
            subnet_type=ec2.SubnetType.PUBLIC,
            cidr_mask=24,
        ),
        ec2.SubnetConfiguration(
            name="Private",
            subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
            cidr_mask=24,
        ),
    ],
)
```

---

## L2: Lambda Function

*Function with env vars and timeout.*

```python
from aws_cdk import aws_lambda as _lambda, Duration

fn = _lambda.Function(
    self, "AppFunction",
    runtime=_lambda.Runtime.PYTHON_3_12,
    handler="handler.main",
    code=_lambda.Code.from_asset("lambda"),
    environment={"TABLE_NAME": "my-table"},
    timeout=Duration.seconds(30),
    memory_size=256,
)
```

---

## L2: RDS DatabaseInstance

*RDS with Secrets Manager credentials.*

```python
from aws_cdk import aws_rds as rds, aws_ec2 as ec2

db = rds.DatabaseInstance(
    self, "AppDb",
    engine=rds.DatabaseInstanceEngine.postgres(
        version=rds.PostgresEngineVersion.VER_16
    ),
    instance_type=ec2.InstanceType.of(
        ec2.InstanceClass.T3, ec2.InstanceSize.MICRO
    ),
    vpc=vpc,
    vpc_subnets=ec2.SubnetSelection(
        subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
    ),
    credentials=rds.Credentials.from_generated_secret("postgres"),
    deletion_protection=False,
)
```

---

## Passing References Between Constructs

*Connect constructs via attributes.*

```python
# Pass bucket name to Lambda as environment variable
fn = _lambda.Function(
    self, "Processor",
    runtime=_lambda.Runtime.PYTHON_3_12,
    handler="handler.main",
    code=_lambda.Code.from_asset("lambda"),
    environment={
        "BUCKET_NAME": bucket.bucket_name,   # direct reference
        "DB_SECRET_ARN": db.secret.secret_arn,
    },
)

# Grant permissions (CDK generates the IAM policy automatically)
bucket.grant_read_write(fn)
db.secret.grant_read(fn)
```

---

## CfnOutput

*Export values from stack.*

```python
import aws_cdk as cdk

cdk.CfnOutput(self, "BucketName", value=bucket.bucket_name)
cdk.CfnOutput(self, "ApiUrl",     value=api.url, export_name="AppApiUrl")
```

---

## Tags

*Apply tags to all resources.*

```python
import aws_cdk as cdk

# Tag all resources in a construct or stack
cdk.Tags.of(self).add("Environment", "prod")
cdk.Tags.of(self).add("Project", "my-app")

# Tag a specific construct
cdk.Tags.of(bucket).add("DataClassification", "confidential")
```
