# AWS CLF-C02 Domain 1: Cloud Concepts

## What is Cloud Computing
*On-demand IT resources delivery*

**Cloud Computing** – On-demand delivery of IT resources over the internet  
**Pay-as-you-go** – Pay only for what you consume  
**Broad network access** – Available over network from any device  
**Resource pooling** – Multi-tenant shared infrastructure  
**Rapid elasticity** – Scale up/down quickly on demand  
**Measured service** – Usage monitored, controlled, and billed  

---

## Six Advantages of Cloud
*Why cloud beats on-premises*

**Trade CapEx for OpEx** – No upfront hardware investment; pay as you use  
**Massive economies of scale** – AWS aggregates usage → lower prices  
**Stop guessing capacity** – Scale to exact need, no over/under-provisioning  
**Increase speed and agility** – Resources in minutes, not weeks  
**Stop spending on data centers** – Focus on apps, not infrastructure  
**Go global in minutes** – Deploy in multiple AWS Regions instantly  

---

## Cloud Deployment Models
*Public, private, hybrid*

| Model | Definition | Use Case |
|-------|-----------|----------|
| **Public** | Resources owned/operated by third-party cloud provider | Startups, variable workloads, web apps |
| **Private** | Cloud infra used exclusively by one organization (on-prem or hosted) | Government, strict compliance, sensitive data |
| **Hybrid** | Mix of public + private connected together | Regulated industries, legacy system migration |

---

## Cloud Service Models
*IaaS, PaaS, SaaS layers*

| Model | Definition | AWS Example | You Manage | AWS Manages |
|-------|-----------|------------|-----------|------------|
| **IaaS** | Virtualized compute, storage, network | EC2, S3, VPC | OS, runtime, apps, data | Hardware, network, hypervisor |
| **PaaS** | Platform to deploy apps without managing infra | Elastic Beanstalk, RDS | App code, data | OS, runtime, scaling, patching |
| **SaaS** | Ready-to-use software over the internet | Amazon WorkMail, Chime | User access, config | Everything else |

---

## AWS Well-Architected Framework
*Six pillars of good design*

**Operational Excellence** – Run and monitor systems, continuously improve processes  
**Security** – Protect data, systems, and assets using risk assessments  
**Reliability** – Recover from failures, scale dynamically, mitigate disruptions  
**Performance Efficiency** – Use resources efficiently as demand changes  
**Cost Optimization** – Avoid unnecessary costs, use right sizing and pricing models  
**Sustainability** – Minimize environmental impact of cloud workloads  

---

## AWS Global Infrastructure
*Regions, AZs, edge locations*

**Region** – Geographic area with 2+ Availability Zones (e.g., `us-east-1`)  
**Availability Zone (AZ)** – One or more discrete data centers with redundant power/network (e.g., `us-east-1a`)  
**Edge Location** – Data center for CloudFront/Route 53 caching closer to users (200+ globally)  
**Local Zone** – AWS infra extension to metro areas for ultra-low latency  
**Wavelength Zone** – AWS infra embedded in telecom networks for 5G edge apps  

**Region selection criteria**: Compliance, latency, available services, cost
