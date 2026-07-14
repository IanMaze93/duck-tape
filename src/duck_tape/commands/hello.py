from pathlib import Path

import typer
from rich.console import Console

app = typer.Typer(
    help="Hello test",
    no_args_is_help=True,
)

console = Console()


@app.command("say_hello", help="Say hello to the world.")
def hello():
    console.print("Hello!")

