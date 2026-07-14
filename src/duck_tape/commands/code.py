from pathlib import Path
from duck_tape.commands.project_commands.common import display_projects
from duck_tape.commands.project_commands import web_portfolio
import typer
from rich.console import Console

app = typer.Typer(
    help="Code Commands for Ian's Projects",
    no_args_is_help=True,
)

app.add_typer(web_portfolio.app, name="web_portfolio", help="Code Commands for Ian's Web Portfolio.")

console = Console()


@app.command("display-projects", help="Display all projects in the current directory.")
def display_projects_command():
    display_projects()