# Bash Advanced
*Text processing, error handling, and patterns*

## String Manipulation
*Built-in string operations*

```bash
str="Hello, World"

echo ${#str}            # → 13 (length)
echo ${str:7}           # → World (substring from index 7)
echo ${str:7:5}         # → World (start:length)
echo ${str/World/Bash}  # → Hello, Bash (replace first)
echo ${str//l/L}        # → HeLLo, WorLd (replace all)
echo ${str^^}           # → HELLO, WORLD (uppercase)
echo ${str,,}           # → hello, world (lowercase)

# Remove prefix/suffix
file="report.tar.gz"
echo ${file%.gz}        # → report.tar (remove .gz)
echo ${file%%.*}        # → report (remove all after first dot)
echo ${file#report.}    # → tar.gz (remove prefix)
```

---

## Arrays
*Indexed and associative arrays*

```bash
# Indexed array
fruits=("apple" "banana" "cherry")
echo ${fruits[0]}       # → apple
echo ${fruits[@]}       # → all elements
echo ${#fruits[@]}      # → 3 (length)

fruits+=("date")        # append
unset fruits[1]         # remove element

# Loop over array
for fruit in "${fruits[@]}"; do
    echo "$fruit"
done

# Associative array (Bash 4+)
declare -A config
config[host]="localhost"
config[port]="5432"
echo ${config[host]}    # → localhost
```

---

## Text Processing
*grep, sed, awk essentials*

```bash
# grep — search
grep "error" app.log            # lines with "error"
grep -c "error" app.log         # count matches
grep -v "debug" app.log         # lines WITHOUT "debug"
grep -E "err|warn" app.log      # regex alternation

# sed — stream editor
sed 's/foo/bar/' file.txt       # replace first occurrence per line
sed 's/foo/bar/g' file.txt      # replace all
sed -n '5,10p' file.txt         # print lines 5-10
sed '/^#/d' config.txt          # delete comment lines

# awk — field processing
awk '{print $1}' file.txt       # print first column
awk -F: '{print $1}' /etc/passwd  # split on :
awk '{sum += $1} END {print sum}' numbers.txt  # sum column
```

---

## Error Handling
*Defensive scripting*

```bash
#!/usr/bin/env bash
set -euo pipefail

# Trap on exit
cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/lock.$$
}
trap cleanup EXIT

# Trap on error
trap 'echo "Error on line $LINENO"' ERR

# Manual check
command || { echo "command failed"; exit 1; }

# Default values for unset vars
name="${NAME:-default}"     # use "default" if NAME unset
port="${PORT:=8080}"        # assign 8080 if PORT unset
```

---

## Common Patterns
*Useful script idioms*

```bash
# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if command exists
if ! command -v docker &>/dev/null; then
    echo "docker not found"
    exit 1
fi

# Require argument
if [ $# -lt 1 ]; then
    echo "Usage: $0 <environment>"
    exit 1
fi
ENV="$1"

# Redirect output
command > output.log 2>&1   # stdout + stderr to file
command >> output.log        # append
command 2>/dev/null          # discard errors
```
