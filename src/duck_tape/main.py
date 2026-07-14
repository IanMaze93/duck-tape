import typer
from duck_tape.commands import hello
app = typer.Typer(
    name="duck-tape",
    help="Personal scripts and utilities held together with questionable engineering.",
    no_args_is_help=True,
)

app.add_typer(hello.app, name="hello", help="Say hello to the world.")

@app.command()
def version() -> None:

    """Display the installed version."""

    typer.echo("duck-tape 0.1.0")


if __name__ == "__main__":
    app()