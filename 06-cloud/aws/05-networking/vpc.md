# AWS VPC
*Virtual Private Cloud — your isolated network*

## What is VPC
*Private, logically isolated network in AWS*

**VPC (Virtual Private Cloud)** – Logically isolated section of the AWS cloud  
**CIDR Block** – IP range assigned to VPC (e.g., `10.0.0.0/16`)  
**Subnet** – Sub-range of VPC IP addresses, tied to one AZ  
**Public Subnet** – Has route to Internet Gateway (resources can have public IPs)  
**Private Subnet** – No route to internet (use NAT for outbound)  
**Default VPC** – AWS-created VPC in every region; all subnets are public  

---

## VPC Components
*Building blocks of a VPC*

**Internet Gateway (IGW)** – Connects VPC to the internet (attach to VPC)  
**NAT Gateway** – Lets private subnet resources reach internet (outbound only)  
**Route Table** – Rules that direct traffic; each subnet associates with one  
**Security Group** – Stateful firewall at instance level  
**Network ACL (NACL)** – Stateless firewall at subnet level  
**VPC Peering** – Private connection between two VPCs  
**VPC Endpoint** – Private connection to AWS services (S3, DynamoDB) without internet  

---

## Typical Architecture
*Standard 2-tier VPC layout*

```
VPC: 10.0.0.0/16
├── Public Subnet  10.0.1.0/24  (AZ-a)  ← ALB, Bastion
│   └── Internet Gateway
├── Public Subnet  10.0.2.0/24  (AZ-b)  ← ALB (multi-AZ)
│   └── Internet Gateway
├── Private Subnet 10.0.3.0/24  (AZ-a)  ← EC2 / ECS app
│   └── NAT Gateway (routes to Public subnet)
└── Private Subnet 10.0.4.0/24  (AZ-b)  ← RDS, ElastiCache
```

**Rule**: web-facing resources in public subnets, databases and app servers in private.

---

## Route Tables
*Direct traffic between subnets and gateways*

```
Public Subnet Route Table:
  10.0.0.0/16  →  local
  0.0.0.0/0    →  igw-abc123    ← all internet traffic via IGW

Private Subnet Route Table:
  10.0.0.0/16  →  local
  0.0.0.0/0    →  nat-abc123    ← outbound via NAT Gateway
```

---

## Security Groups vs NACLs
*Two layers of network security*

| | Security Group | NACL |
|---|---|---|
| Level | Instance | Subnet |
| State | Stateful | Stateless |
| Rules | Allow only | Allow + Deny |
| Applies to | ENI (instance) | All instances in subnet |
| Default | Deny all inbound | Allow all |

**Stateful**: return traffic automatically allowed (SG).  
**Stateless**: must explicitly allow both inbound AND outbound (NACL).
