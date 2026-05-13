# Bash Basics
*Shell scripting fundamentals*

## Script Structure
*Anatomy of a Bash script*

```bash
#!/usr/bin/env bash
# Shebang: tells OS to use bash

set -euo pipefail   # exit on error, undefined var, pipe fail

echo "Hello, World"

# Usage
chmod +x script.sh
./script.sh
```

**`set -e`** – Exit immediately if a command fails  
**`set -u`** – Treat unset variables as errors  
**`set -o pipefail`** – Fail if any pipe command fails  

---

## Variables
*Storing and using values*

```bash
name="Alice"           # no spaces around =
echo $name             # → Alice
echo "${name}s"        # → Alices (braces for clarity)

readonly MAX=100       # constant
unset name             # remove variable

# Command substitution
today=$(date +%Y-%m-%d)
files=$(ls *.txt)

# Arithmetic
count=5
echo $((count + 3))    # → 8
echo $((count * 2))    # → 10
```

---

## Conditionals
*Branching logic*

```bash
# if/elif/else
if [ "$name" = "Alice" ]; then
    echo "Hello Alice"
elif [ "$name" = "Bob" ]; then
    echo "Hello Bob"
else
    echo "Who are you?"
fi

# File tests
if [ -f "file.txt" ]; then echo "exists"; fi
if [ -d "dir/" ];     then echo "is dir"; fi
if [ -z "$var" ];     then echo "empty"; fi
if [ -n "$var" ];     then echo "not empty"; fi

# Numeric comparison
if [ $count -gt 5 ]; then echo "greater"; fi
# -eq  -ne  -lt  -le  -gt  -ge
```

---

## Loops
*Iterating over values*

```bash
# for loop
for file in *.log; do
    echo "Processing $file"
done

# for range
for i in {1..5}; do
    echo "Step $i"
done

# while loop
count=0
while [ $count -lt 5 ]; do
    echo $count
    ((count++))
done

# Loop over lines in file
while IFS= read -r line; do
    echo "$line"
done < input.txt
```

---

## Functions
*Reusable code blocks*

```bash
greet() {
    local name="$1"     # $1 = first argument
    echo "Hello, $name"
    return 0            # exit code
}

# Usage
greet "Alice"           # → Hello, Alice
greet "Bob"             # → Hello, Bob

# Check return value
if greet "Alice"; then
    echo "Greeted successfully"
fi
```

**`$1`, `$2`, ...`$n`** – Positional arguments  
**`$@`** – All arguments as separate words  
**`$#`** – Number of arguments  
**`$?`** – Exit code of last command  
**`$$`** – PID of current script  
