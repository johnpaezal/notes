# CDK Basics

## Core Concepts

*Define AWS infra with code.*

**CDK** – AWS Cloud Development Kit; defines infra using real code.  
**App** – Root CDK construct; entry point of every CDK project.  
**Stack** – Maps 1:1 to a CloudFormation stack; unit of deployment.  
**Construct** – Building block; each resource or group of resources.  
**Synthesize** – Convert CDK code to CloudFormation JSON/YAML templates.  
**Bootstrap** – Provision CDK assets bucket and ECR repo in an account/region.  

---

## CDK vs Terraform

*Language and abstraction comparison.*

| Feature | CDK | Terraform |
|---|---|---|
| Language | Python, TypeScript, Java, C# | HCL (domain-specific) |
| State management | CloudFormation handles state | `.tfstate` file |
| Abstraction | L1/L2/L3 constructs | Modules, resources |
| Ecosystem | AWS-only | Multi-cloud |
| Testing | pytest, Jest | Terratest |
| Drift detection | `cdk diff` + CloudFormation | `terraform plan` |

---

## Setup and Project Structure

*Install, bootstrap, init.*

```bash
# Install
pip install aws-cdk-lib constructs

# Bootstrap account/region (once per account)
cdk bootstrap aws://ACCOUNT_ID/us-east-1

# Create new project
cdk init app --language python
```

**Project structure after `cdk init`:**

```
my-cdk-app/
├── app.py              # CDK App entry point
├── cdk.json            # CDK configuration and context
├── cdk.out/            # Synthesized CloudFormation templates
├── my_cdk_app/
│   ├── __init__.py
│   └── my_cdk_app_stack.py   # Stack definition
├── requirements.txt
└── tests/
```

---

## Basic Stack: S3 Bucket with Output

*S3 bucket with versioning enabled.*

```python
# my_cdk_app/my_cdk_app_stack.py
import aws_cdk as cdk
from aws_cdk import aws_s3 as s3
from constructs import Construct

class MyCdkAppStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self, "MyBucket",
            versioned=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )

        cdk.CfnOutput(
            self, "BucketName",
            value=bucket.bucket_name,
            description="S3 bucket name",
        )

# app.py
app = cdk.App()
MyCdkAppStack(app, "MyCdkAppStack")
app.synth()
```

```bash
# Usage
cdk synth          # generate CloudFormation template
cdk diff           # show pending changes
cdk deploy         # deploy to AWS
cdk destroy        # delete all resources
cdk ls             # list all stacks
```

---

## cdk.json and cdk.out

*CDK config and output directory.*

**`cdk.json`** – CDK project config; stores the `app` command and context values.  
**`cdk.out/`** – Generated CloudFormation templates; never commit to git.  
**Context** – Key/value pairs available at synth time; used for environment-specific config.  

```json
{
  "app": "python3 app.py",
  "context": {
    "@aws-cdk/aws-s3:serverAccessLogsUseBucketPolicy": true,
    "env": "dev"
  }
}
```
