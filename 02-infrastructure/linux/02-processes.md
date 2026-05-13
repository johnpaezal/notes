# Linux Processes
*Managing running programs and system resources*

## Process Basics
*What is a process*

**Process** – Running instance of a program  
**PID** – Process ID; unique integer assigned by kernel  
**PPID** – Parent Process ID  
**Daemon** – Background process with no terminal (e.g., `sshd`, `nginx`)

```bash
ps aux              # list all running processes
ps aux | grep nginx # find specific process
pgrep nginx         # get PID by name

# Usage
ps aux | grep python   # → find running Python scripts
pgrep -l java          # → list Java processes with names
```

---

## Monitoring
*Real-time system state*

```bash
top           # real-time process viewer (q to quit)
htop          # improved top (if installed)
free -h       # memory usage (human-readable)
df -h         # disk usage per mount
du -sh /var/* # disk usage per directory

# Usage
free -h       # → check if server is memory-constrained
df -h         # → check if disk is nearly full
```

---

## Signals and Kill
*Stop, pause, and control processes*

**`SIGTERM (15)`** – Graceful stop (default)  
**`SIGKILL (9)`** – Force kill, cannot be caught  
**`SIGHUP (1)`** – Reload config (daemons)  

```bash
kill 1234           # send SIGTERM to PID 1234
kill -9 1234        # force kill
killall nginx       # kill all processes named nginx
pkill -f "python app.py"  # kill by command match

# Usage
kill $(pgrep nginx)         # graceful stop nginx
kill -9 $(pgrep -f hung)    # force kill hung process
```

---

## Foreground and Background
*Job control*

```bash
command &           # run in background
jobs                # list background jobs
fg %1               # bring job 1 to foreground
bg %1               # resume job 1 in background
Ctrl+C              # kill foreground process
Ctrl+Z              # suspend foreground process

nohup command &     # run in background, survive logout
disown %1           # detach job from shell

# Usage
python server.py &      # run server in background
nohup ./batch.sh &      # run batch job, ignore hangup
```

---

## systemd Services
*Managing system daemons*

```bash
systemctl status nginx          # check service status
systemctl start nginx           # start service
systemctl stop nginx            # stop service
systemctl restart nginx         # restart
systemctl reload nginx          # reload config without restart
systemctl enable nginx          # start on boot
systemctl disable nginx         # don't start on boot

journalctl -u nginx             # view service logs
journalctl -u nginx -f          # follow logs
journalctl -u nginx --since "1h ago"

# Usage
systemctl enable --now nginx    # enable + start immediately
journalctl -u app -f            # tail application logs
```
