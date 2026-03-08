# Python CLI

## argparse (Built-in)
*Parse command-line arguments*

```python
import argparse

parser = argparse.ArgumentParser(description="User management tool")

# Positional argument (required)
parser.add_argument("username", help="Username to process")

# Optional argument
parser.add_argument("--age", type=int, default=18, help="User age")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
parser.add_argument("--output", choices=["json", "csv"], default="json")

args = parser.parse_args()

# Usage
# python script.py alice --age 25 --verbose
print(args.username)   # "alice"
print(args.age)        # 25
print(args.verbose)    # True
```

---

## Subcommands with argparse
*Commands like `git commit`, `git push`*

```python
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

# "create" subcommand
create = subparsers.add_parser("create", help="Create a user")
create.add_argument("name")
create.add_argument("--admin", action="store_true")

# "delete" subcommand
delete = subparsers.add_parser("delete", help="Delete a user")
delete.add_argument("name")

args = parser.parse_args()

# Usage
# python script.py create alice --admin
# python script.py delete alice
if args.command == "create":
    print(f"Creating {args.name}, admin={args.admin}")
elif args.command == "delete":
    print(f"Deleting {args.name}")
```

---

## click (Third-party)
*Decorator-based CLI framework*

```bash
pip install click
```

```python
import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument("name")
@click.option("--age", default=18, help="User age")
@click.option("--verbose", is_flag=True)
def create(name, age, verbose):
    """Create a new user."""
    if verbose:
        click.echo(f"Creating user: {name}, age={age}")

@cli.command()
@click.argument("name")
@click.confirmation_option(prompt="Are you sure?")
def delete(name):
    """Delete a user."""
    click.echo(f"Deleted {name}")

# Usage
# python script.py create alice --age 25 --verbose
# python script.py delete alice
if __name__ == "__main__":
    cli()
```

---

## click Utilities
*Helpful CLI building blocks*

```python
import click

# Prompt user for input
name = click.prompt("Enter your name")
password = click.prompt("Password", hide_input=True)

# Styled output
click.echo(click.style("Success!", fg="green", bold=True))
click.echo(click.style("Error!", fg="red"))

# Progress bar
with click.progressbar(items, label="Processing") as bar:
    for item in bar:
        process(item)

# File argument (auto opens/closes)
@click.argument("file", type=click.File("r"))
def read(file):
    content = file.read()
```

---

## argparse vs click

| | argparse | click |
|--|----------|-------|
| Built-in | Yes | No |
| Syntax | Imperative | Decorators |
| Subcommands | Manual | `@group` / `@command` |
| Help text | Auto-generated | Auto-generated |
| Best for | Simple scripts | Complex CLIs |

---

## Best Practices

**`if __name__ == "__main__"`** – Always guard CLI entry point  
**`click`** – Prefer over `argparse` for CLIs with multiple commands  
**`--verbose` flag** – Add to every CLI for debugging without code changes  
**Help text** – Always write `help=` or docstrings; users depend on them  
**Exit codes** – Use `sys.exit(1)` on error; `0` on success  
