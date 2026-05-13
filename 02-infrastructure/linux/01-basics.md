# Linux Basics
*Filesystem, navigation, and core commands*

## Filesystem Structure
*Standard Linux directory layout*

**`/`** – Root of the filesystem  
**`/home`** – User home directories (`/home/alice`)  
**`/etc`** – System config files  
**`/var`** – Variable data: logs, databases, caches  
**`/tmp`** – Temporary files (cleared on reboot)  
**`/bin`** – Essential user binaries (`ls`, `cp`, `mv`)  
**`/usr/bin`** – Non-essential user binaries  
**`/opt`** – Third-party software  
**`/proc`** – Virtual filesystem: kernel and process info  

---

## Navigation
*Moving through the filesystem*

```bash
pwd               # print working directory
cd /etc           # absolute path
cd ..             # go up one level
cd ~              # go to home directory
cd -              # go to previous directory

ls                # list files
ls -la            # long format + hidden files
ls -lh            # human-readable sizes

# Usage
pwd               # → /home/alice
ls -lh /var/log   # → shows log files with sizes
```

---

## File Operations
*Create, copy, move, delete*

```bash
touch file.txt              # create empty file
mkdir -p a/b/c              # create nested directories
cp file.txt backup.txt      # copy file
cp -r dir/ backup/          # copy directory recursively
mv file.txt /tmp/           # move file
mv old.txt new.txt          # rename file
rm file.txt                 # delete file
rm -rf dir/                 # delete directory recursively

# Usage
mkdir -p ~/projects/api
cp -r src/ src-backup/
rm -rf /tmp/old-build/
```

---

## Viewing Files
*Display file content*

```bash
cat file.txt          # print entire file
less file.txt         # paginated view (q to quit)
head -n 20 file.txt   # first 20 lines
tail -n 20 file.txt   # last 20 lines
tail -f app.log       # follow file in real time (logs)

# Usage
tail -f /var/log/syslog   # monitor system log live
head -n 5 /etc/passwd     # peek at first 5 users
```

---

## File Search
*Find files and content*

```bash
find /var/log -name "*.log"         # find by name
find . -type f -mtime -1            # files modified last 24h
find . -size +10M                   # files larger than 10MB

grep "error" app.log                # search in file
grep -r "config" /etc/              # recursive search
grep -n "TODO" *.py                 # show line numbers
grep -i "warning" app.log           # case-insensitive

# Usage
grep -r "DATABASE_URL" .            # find where DB URL is set
find /tmp -type f -mtime +7         # old temp files
```

---

## Permissions
*File ownership and access control*

**`r`** – Read (4)  
**`w`** – Write (2)  
**`x`** – Execute (1)  

```bash
ls -l file.txt
# -rwxr-xr-- 1 alice dev 1024 Jan 1 file.txt
#  │││└── other: r--  (4)
#  ││└─── group: r-x  (5)
#  │└──── owner: rwx  (7)
#  └───── type: - file, d dir, l symlink

chmod 755 script.sh   # rwxr-xr-x
chmod +x script.sh    # add execute for all
chown alice:dev file  # change owner:group

# Usage
chmod 600 ~/.ssh/id_rsa     # private key: owner only
chmod 755 /var/www/html     # web dir: readable by all
```
