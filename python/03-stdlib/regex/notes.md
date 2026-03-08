# Python Regex

## Core Functions
*Match patterns in strings*

```python
import re

text = "Email: user@example.com, Phone: 555-1234"

re.search(r"\d+", text)          # first match anywhere
re.match(r"\d+", text)           # match at start only
re.findall(r"\d+", text)         # all matches as list → ['555', '1234']
re.finditer(r"\d+", text)        # iterator of match objects
re.sub(r"\d+", "###", text)      # replace all matches
re.split(r"[,\s]+", text)        # split by pattern
```

---

## Common Patterns
*Frequently used regex building blocks*

| Pattern | Matches |
|---------|---------|
| `.` | Any character (except newline) |
| `\d` | Digit `[0-9]` |
| `\w` | Word char `[a-zA-Z0-9_]` |
| `\s` | Whitespace |
| `\D`, `\W`, `\S` | Negated versions |
| `^` | Start of string |
| `$` | End of string |
| `[abc]` | Any of a, b, c |
| `[^abc]` | Not a, b, c |

---

## Quantifiers
*Control how many times a pattern repeats*

| Pattern | Meaning |
|---------|---------|
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 (optional) |
| `{n}` | Exactly n times |
| `{n,m}` | Between n and m times |
| `*?`, `+?` | Non-greedy (minimal match) |

---

## Groups & Capturing
*Extract specific parts of a match*

```python
import re

# Capture groups
match = re.search(r"(\w+)@(\w+)\.(\w+)", "user@example.com")
match.group(0)   # "user@example.com"  full match
match.group(1)   # "user"
match.group(2)   # "example"

# Named groups
match = re.search(r"(?P<user>\w+)@(?P<domain>\w+)", "alice@gmail.com")
match.group("user")    # "alice"
match.group("domain")  # "gmail"

# Non-capturing group
re.findall(r"(?:http|https)://\S+", text)
```

---

## Flags
*Modify matching behavior*

```python
import re

re.search(r"hello", "Hello World", re.IGNORECASE)  # case-insensitive
re.findall(r"^\w+", text, re.MULTILINE)             # ^ matches each line start
re.search(r".", text, re.DOTALL)                    # . matches newline too

# Combine flags
re.search(r"hello", text, re.IGNORECASE | re.MULTILINE)
```

---

## Compiled Patterns
*Reuse patterns for performance*

```python
import re

EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[a-z]{2,}")
PHONE_RE = re.compile(r"\d{3}[-.\s]\d{4}")

# Usage
emails = EMAIL_RE.findall(text)
phones = PHONE_RE.findall(text)

# Validate
def is_valid_email(s):
    return bool(EMAIL_RE.fullmatch(s))
```

---

## Best Practices

**Raw strings** – Always use `r"..."` to avoid double-escaping backslashes  
**`re.compile`** – Compile patterns used more than once  
**Named groups** – Use `(?P<name>...)` for readable captures  
**Non-greedy** – Prefer `+?` / `*?` when matching minimal content  
**`fullmatch`** – Use to validate entire strings, not just substrings  
