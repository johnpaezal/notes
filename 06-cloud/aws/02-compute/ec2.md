# AWS EC2
*Virtual machines in the cloud*

## What is EC2
*Elastic Compute Cloud — rent virtual servers*

**EC2 (Elastic Compute Cloud)** – Virtual machine you control (OS, runtime, ports)  
**Instance** – A running EC2 virtual machine  
**AMI (Amazon Machine Image)** – Template: OS + software; used to launch instances  
**Instance Type** – CPU + RAM configuration (`t3.micro`, `m5.large`, `c5.2xlarge`)  
**Key Pair** – SSH key for remote access  
**User Data** – Script that runs at first boot  

---

## Instance Types
*Naming pattern and families*

```
t3.micro
│ │ └── Size: nano, micro, small, medium, large, xlarge, 2xlarge...
│ └──── Generation: 3rd gen
└────── Family: t (burstable)
```

| Family | Use Case |
|--------|----------|
| `t` | Burstable, low cost (dev, small apps) |
| `m` | General purpose (balanced CPU/RAM) |
| `c` | Compute optimized (high CPU) |
| `r` | Memory optimized (in-memory DB, cache) |
| `g/p` | GPU instances (ML training) |

---

## Pricing Models
*How you pay for EC2*

**On-Demand** – Pay by the hour/second; no commitment; most expensive  
**Reserved** – Commit 1 or 3 years; up to 72% discount  
**Spot** – Unused capacity; up to 90% discount; can be interrupted  
**Savings Plans** – Flexible commitment on compute spend  

**Rule**: On-Demand for dev/test, Reserved for stable prod workloads, Spot for batch/CI.

---

## Security Groups
*Stateful virtual firewall for instances*

```
Inbound rules:
  Port 22   TCP  0.0.0.0/0   (SSH)
  Port 80   TCP  0.0.0.0/0   (HTTP)
  Port 443  TCP  0.0.0.0/0   (HTTPS)
  Port 5432 TCP  10.0.0.0/16 (Postgres, only from VPC)

Outbound rules:
  All traffic  All  0.0.0.0/0 (default: allow all out)
```

**Stateful** – If inbound is allowed, return traffic is automatically allowed.

---

## Launch and Connect
*Create and access an EC2 instance*

```bash
# Launch via CLI
aws ec2 run-instances \
  --image-id ami-0abcdef1234567890 \
  --instance-type t3.micro \
  --key-name my-key \
  --security-group-ids sg-abc123 \
  --subnet-id subnet-abc123

# Connect via SSH
ssh -i ~/.ssh/my-key.pem ubuntu@<public-ip>

# User data script example (install nginx at boot)
#!/bin/bash
apt-get update -y
apt-get install -y nginx
systemctl start nginx
systemctl enable nginx
```

---

## Elastic IP and Metadata
*Static IPs and instance info*

**Elastic IP** – Static public IP; survives stop/start; billed when not attached  
**Instance Metadata** – Info about the running instance accessible from within  

```bash
# From inside EC2
curl http://169.254.169.254/latest/meta-data/instance-id
curl http://169.254.169.254/latest/meta-data/public-ipv4
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```
