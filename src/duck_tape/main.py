from rich.console import Console
from duck_tape.tools.linux.create_executable import create_executable
from duck_tape.tools.logo import get_logo
import typer
from duck_tape.commands import code
from duck_tape.commands import backups

app = typer.Typer(
    add_completion=False,
    name="duck-tape",
    help="Personal scripts and utilities held together with questionable engineering.",
    no_args_is_help=True,
)

console = Console()

console.print(get_logo(), style="bold green")

app.add_typer(code.app, name="code", help="Code Commands for Ian's Projects.")
app.add_typer(backups.app, name="backup", help="Backup Commands")


@app.command()
def version() -> None:
    """Display the installed version."""

    typer.echo("duck-tape 0.1.0")


@app.command(help="Setup duck-tape on your system. | Linux Only")
def setup() -> None:
    create_executable()


if __name__ == "__main__":
    app()
