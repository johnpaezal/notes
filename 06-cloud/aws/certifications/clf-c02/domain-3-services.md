# AWS CLF-C02 Domain 3: Cloud Technology and Services

## Compute
*Run applications on AWS*

**EC2** – Virtual servers (IaaS); full OS control, instance types, pricing models  
**Lambda** – Serverless functions; event-driven, no server management, max 15 min  
**ECS** – Elastic Container Service; run Docker containers (EC2 or Fargate launch)  
**EKS** – Elastic Kubernetes Service; managed Kubernetes control plane  
**Elastic Beanstalk** – PaaS; upload code, AWS handles infra (EC2, ELB, Auto Scaling)  
**Lightsail** – Simplified VPS for small apps; fixed monthly pricing  
**Batch** – Managed batch processing jobs at any scale  
**Fargate** – Serverless compute engine for containers (used with ECS/EKS)  

**EC2 pricing models**:  
**On-Demand** – Pay by second, no commitment  
**Reserved** – 1 or 3-year commitment; up to 72% discount  
**Spot** – Bid for unused capacity; up to 90% discount, can be interrupted  
**Savings Plans** – Flexible commitment ($/hour) across instance families  
**Dedicated Host** – Physical server dedicated to one customer  

---

## Storage
*Store and retrieve data*

**S3** – Object storage; unlimited data, 5TB max per object, 11 9s durability  
**EBS** – Elastic Block Store; persistent block storage attached to one EC2  
**EFS** – Elastic File System; shared NFS file system across multiple EC2s  
**S3 Glacier** – Archive storage; retrieval from minutes to hours; very low cost  
**S3 Glacier Deep Archive** – Cheapest storage; 12-48 hour retrieval  
**Storage Gateway** – Hybrid storage connecting on-premises to S3/EBS  
**FSx** – Managed file systems (Windows FSx, Lustre FSx for HPC)  

**S3 storage classes**:  
**Standard** – Frequent access, high availability  
**Standard-IA** – Infrequent access, lower cost, retrieval fee  
**One Zone-IA** – Single AZ, lower cost, less resilient  
**Intelligent-Tiering** – Auto-moves objects between tiers based on access  
**Glacier Instant Retrieval** – Archive with millisecond access  

---

## Databases
*Managed data storage services*

**RDS** – Relational managed DB; MySQL, PostgreSQL, Oracle, SQL Server, MariaDB  
**Aurora** – AWS-built relational DB; MySQL/PostgreSQL-compatible, 5x faster than MySQL  
**DynamoDB** – Serverless NoSQL; key-value and document, single-digit ms latency  
**ElastiCache** – In-memory cache; Redis or Memcached; sub-ms response  
**Redshift** – Columnar data warehouse; SQL analytics on petabyte scale  
**DocumentDB** – MongoDB-compatible managed document database  
**Neptune** – Managed graph database  
**QLDB** – Immutable ledger database for transaction history  

---

## Networking
*Connect and route traffic*

**VPC** – Virtual Private Cloud; isolated network with subnets, route tables, gateways  
**Route 53** – Scalable DNS service; domain registration, health checks, routing policies  
**CloudFront** – CDN; caches content at 400+ edge locations globally  
**Direct Connect** – Dedicated private network line from on-premises to AWS  
**API Gateway** – Create, publish, and manage REST/HTTP/WebSocket APIs  
**Elastic Load Balancing (ELB)** – Distributes traffic across targets  
**ALB** – Application Load Balancer; HTTP/S, path/host-based routing  
**NLB** – Network Load Balancer; TCP/UDP, ultra-high performance  
**CLB** – Classic Load Balancer; legacy, avoid for new workloads  
**VPN** – Site-to-site encrypted tunnel over public internet to VPC  
**Transit Gateway** – Hub connecting multiple VPCs and on-premises networks  

---

## Developer and DevOps
*Build, deploy, and automate*

**CloudFormation** – IaC; define AWS resources in JSON/YAML templates  
**CodePipeline** – Fully managed CI/CD orchestration service  
**CodeBuild** – Fully managed build and test service (like Jenkins, managed)  
**CodeDeploy** – Automates deployments to EC2, Lambda, ECS, on-premises  
**CodeCommit** – Managed Git repository service (deprecated — migrate to GitHub)  
**Elastic Beanstalk** – PaaS; handles deployment, capacity, scaling (see Compute)  
**Cloud9** – Browser-based IDE with direct AWS service access  
**CDK** – Cloud Development Kit; define IaC using TypeScript, Python, Java  

---

## Management and Monitoring
*Observe, audit, and govern*

**CloudWatch** – Metrics, logs, dashboards, alarms, and events for AWS resources  
**CloudTrail** – API audit log; records every API call with user, time, source IP  
**Config** – Resource inventory and compliance; tracks config changes over time  
**Trusted Advisor** – Real-time best practice checks (cost, security, performance, limits)  
**Systems Manager** – Operational hub; run commands, patch, session manager, parameter store  
**AWS Organizations** – Manage multiple accounts; consolidated billing, SCPs  
**Control Tower** – Automates multi-account setup with guardrails  
**Health Dashboard** – Service health status and personal account health events  

---

## Migration
*Move workloads to AWS*

**AWS Migration Hub** – Central tracking for application migrations  
**DMS** – Database Migration Service; migrate databases with minimal downtime  
**SMS** – Server Migration Service; migrate on-premises VMs to EC2 AMIs  
**Application Migration Service (MGN)** – Lift-and-shift server replication  
**Snowball** – Physical device to transfer 80TB of data to AWS offline  
**Snowball Edge** – Snowball with compute (Lambda, EC2) for edge processing  
**Snowmobile** – Exabyte-scale data transfer via shipping container truck  
**DataSync** – Online data transfer from on-premises NFS/SMB to S3/EFS  

---

## Analytics
*Process and analyze data at scale*

**Athena** – Serverless SQL queries directly on S3 data; pay per query  
**Glue** – Serverless ETL; discover, transform, and load data  
**Kinesis** – Real-time streaming data ingestion, processing, and analytics  
**QuickSight** – BI dashboards and visualizations; ML-powered insights  
**EMR** – Managed Hadoop/Spark clusters for big data processing  
**Lake Formation** – Build and secure data lakes on S3  
**OpenSearch Service** – Managed Elasticsearch/OpenSearch for log analytics  

---

## AI / ML Services
*Pre-built machine learning APIs*

**Rekognition** – Image and video analysis (objects, faces, text detection)  
**Polly** – Text-to-speech conversion in multiple languages  
**Transcribe** – Speech-to-text (audio/video transcription)  
**Translate** – Neural machine translation between languages  
**Comprehend** – Natural language processing; sentiment, entities, key phrases  
**SageMaker** – End-to-end ML platform; build, train, and deploy models  
**Lex** – Conversational AI (chatbots); powers Alexa  
**Textract** – Extract text and data from scanned documents  
