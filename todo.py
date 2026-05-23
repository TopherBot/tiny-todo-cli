import json
import os
from pathlib import Path
import click

DATA_FILE = Path("todo.json")

def _load_data():
    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return []

def _save_data(items):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)

@click.group()
def cli():
    """Simple todo list manager."""

@cli.command()
@click.argument("text")
def add(text):
    """Add a new todo item."""
    items = _load_data()
    items.append({"text": text, "done": False})
    _save_data(items)
    click.echo(f"Added: {text}")

@cli.command(name="list")
def list_items():
    """List all todo items."""
    items = _load_data()
    if not items:
        click.echo("No items.")
        return
    for idx, itm in enumerate(items, 1):
        status = "✅" if itm["done"] else "❌"
        click.echo(f"{idx}. [{status}] {itm['text']}")

@cli.command()
@click.argument("index", type=int)
def done(index):
    """Mark an item as done by its 1‑based index."""
    items = _load_data()
    if 1 <= index <= len(items):
        items[index - 1]["done"] = True
        _save_data(items)
        click.echo(f"Marked item {index} as done.")
    else:
        click.echo("Invalid index.")

@cli.command()
@click.argument("index", type=int)
def delete(index):
    """Delete an item by its 1‑based index."""
    items = _load_data()
    if 1 <= index <= len(items):
        removed = items.pop(index - 1)
        _save_data(items)
        click.echo(f"Deleted: {removed['text']}")
    else:
        click.echo("Invalid index.")

if __name__ == "__main__":
    cli()
