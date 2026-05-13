# Linux Users & Networking
*User management and network commands*

## Users and Groups
*Manage system accounts*

**`/etc/passwd`** – User account info  
**`/etc/shadow`** – Hashed passwords  
**`/etc/group`** – Group memberships  

```bash
whoami                      # current user
id alice                    # UID, GID, groups of alice
groups alice                # list groups for alice

useradd -m alice            # create user with home dir
usermod -aG docker alice    # add alice to docker group
userdel -r alice            # delete user and home dir
passwd alice                # set password

su alice                    # switch to alice
sudo command                # run as root
sudo -u alice command       # run as alice

# Usage
usermod -aG sudo alice      # give alice sudo access
sudo -u www-data whoami     # verify web server user
```

---

## SSH
*Secure remote access*

```bash
ssh user@host               # connect to remote host
ssh -p 2222 user@host       # custom port
ssh -i ~/.ssh/key.pem user@host  # specific key

# Key management
ssh-keygen -t ed25519       # generate new key pair
ssh-copy-id user@host       # copy public key to server

# Config shortcut (~/.ssh/config)
# Host prod
#   HostName 10.0.0.5
#   User ubuntu
#   IdentityFile ~/.ssh/prod.pem

ssh prod                    # uses config shortcut

# Usage
ssh -i key.pem ubuntu@54.1.2.3    # connect to EC2
ssh-copy-id -i key.pub user@10.0.0.5  # deploy key
```

---

## Network Commands
*Diagnose and inspect connectivity*

```bash
ip addr                     # show network interfaces and IPs
ip route                    # show routing table
ping google.com             # test reachability
ping -c 4 google.com        # 4 packets only

traceroute google.com       # show packet route
curl -I https://example.com # HTTP headers only
wget https://example.com/file.zip  # download file

netstat -tuln               # listening ports
ss -tuln                    # modern netstat alternative
lsof -i :8080               # what's on port 8080

# Usage
lsof -i :5432               # → check if Postgres is up
ss -tuln | grep LISTEN      # → list all open ports
```

---

## Environment Variables
*Shell variables and PATH*

```bash
env                         # list all env vars
printenv HOME               # print specific var
export MY_VAR=hello         # set var for session
echo $MY_VAR                # use var

# Persist in shell config
echo 'export PATH=$PATH:/opt/myapp/bin' >> ~/.bashrc
source ~/.bashrc            # reload config

# Usage
export DATABASE_URL="postgresql://user:pass@localhost/db"
echo $PATH                  # → check binary search path
```
