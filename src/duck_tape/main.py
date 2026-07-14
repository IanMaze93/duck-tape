from rich.console import Console
from duck_tape.tools.logo import get_logo
import typer
from duck_tape.commands import code

app = typer.Typer(
    name="duck-tape",
    help="Personal scripts and utilities held together with questionable engineering.",
    no_args_is_help=True,
)

console = Console()

console.print(get_logo(), style="bold green")

app.add_typer(code.app, name="code", help="Code Commands for Ian's Projects.")


@app.command()
def version() -> None:
    """Display the installed version."""

    typer.echo("duck-tape 0.1.0")


if __name__ == "__main__":
    app()
