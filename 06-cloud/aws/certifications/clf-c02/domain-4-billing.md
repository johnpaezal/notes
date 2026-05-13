# AWS CLF-C02 Domain 4: Billing, Pricing, and Support

## AWS Pricing Models
*How AWS charges for services*

**Pay-as-you-go** – Pay only for what you use, no upfront cost  
**Save when you reserve** – Commit to 1 or 3 years for up to 72% discount  
**Pay less by using more** – Volume discounts (e.g., S3 tiered pricing)  
**Pay less as AWS grows** – AWS passes cost savings to customers over time  

**Reserved Instances (RI)** – Commit to specific instance type/region; Standard or Convertible  
**Savings Plans** – Flexible $/hour commitment; covers EC2, Lambda, Fargate  
**Spot Instances** – Unused EC2 capacity at up to 90% discount; interruptible  

---

## Total Cost of Ownership (TCO)
*On-premises vs cloud cost comparison*

**TCO** – Full cost of owning + operating infra (hardware, power, staff, space)  
**AWS Pricing Calculator** – Estimate monthly AWS costs before deploying  
**TCO Calculator** – Compare on-premises costs vs AWS to build business case  

**On-premises hidden costs**: server hardware, rack space, power/cooling, network gear, IT staff, software licenses, disaster recovery  

**Cloud eliminates**: upfront capital, maintenance contracts, hardware refresh cycles  

---

## AWS Free Tier
*No-cost services to get started*

| Type | Description | Examples |
|------|------------|---------|
| **Always Free** | Never expire, any customer | Lambda 1M requests/mo, DynamoDB 25GB, CloudWatch 10 metrics |
| **12 Months Free** | From account creation date | EC2 t2.micro 750h/mo, S3 5GB Standard, RDS db.t2.micro 750h/mo |
| **Trials** | Short-term free trial per service | SageMaker, Inspector, Lightsail 3 months |

---

## AWS Organizations
*Manage multiple AWS accounts*

**AWS Organizations** – Central management for multiple AWS accounts  
**Management account** – Root account that creates and manages the organization  
**Member account** – Any other account in the org  
**Consolidated Billing** – Single bill for all accounts; volume discounts shared  
**SCP (Service Control Policy)** – Policy to allow/deny services at OU or account level  
**OU (Organizational Unit)** – Group of accounts within the organization hierarchy  

**SCP behavior**: SCPs never grant permissions — they only limit what IAM policies can allow. Root user in member account is also subject to SCPs.

---

## AWS Support Plans
*Response times and features by tier*

| Feature | Basic | Developer | Business | Enterprise |
|---------|-------|-----------|----------|-----------|
| **Cost** | Free | $29/mo | $100/mo | $15,000/mo |
| **Tech support** | None | Business hours (email) | 24/7 (phone, email, chat) | 24/7 (phone, email, chat) |
| **General guidance** | — | < 24h | < 24h | < 24h |
| **System impaired** | — | < 12h | < 4h | < 4h |
| **Production down** | — | — | < 1h | < 1h |
| **Business critical** | — | — | — | < 15 min |
| **Trusted Advisor** | 7 core checks | 7 core checks | All checks | All checks |
| **TAM** | No | No | No | Yes |
| **Concierge** | No | No | No | Yes |

**TAM (Technical Account Manager)** – Dedicated advisor; only in Enterprise plan  
**Concierge** – Billing and account specialist; only in Enterprise plan  

---

## Cost Management Tools
*Visualize, control, and optimize spend*

**Cost Explorer** – Visualize and analyze AWS spending over time; forecasting  
**AWS Budgets** – Set budget alerts when costs/usage exceed thresholds  
**Cost and Usage Report (CUR)** – Detailed hourly/daily cost data exported to S3  
**Trusted Advisor** – Cost optimization checks (idle resources, unused RIs)  
**Savings Plans recommendations** – Shown in Cost Explorer based on usage  
**Right Sizing** – Recommendations to downsize over-provisioned EC2 instances  

---

## AWS Marketplace
*Third-party software on AWS*

**AWS Marketplace** – Digital catalog of third-party software and services  
**Pre-configured AMIs** – Launch vendor-configured EC2 instances instantly  
**SaaS subscriptions** – Subscribe to software billed through AWS account  
**CloudFormation templates** – Deploy vendor architectures with one click  

**Benefits**: consolidated billing (Marketplace charges on AWS bill), BYOL support, free trials on select products  
