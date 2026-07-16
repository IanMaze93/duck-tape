import os
import typer
from rich.console import Console
from dotenv import load_dotenv
from pathlib import Path
from duck_tape.commands.project_commands.common import display_projects
from duck_tape.tools.dev_tools.tools import development_startup
from duck_tape.commands.project_commands import create

load_dotenv()
console = Console()

projects_path = Path.home() / os.getenv("PROJECTS_PATH")

app = typer.Typer(
    help="Code Commands for Ian's Projects",
    no_args_is_help=True,
)

# Pull all projects in the specfied directory
subdirectories = [
    directory for directory in projects_path.iterdir() if directory.is_dir()
]

# Dynamically create a Typer app for each subdirectory
for subdirectory in subdirectories:
    # Create a Typer app for the subdirectory using the create_project function
    create_app = create.create_project(subdirectory.name)
    app.add_typer(
        create_app,
        name=subdirectory.name,
    )


# Other code-related commands can be added here as needed
@app.command("display-projects", help="Display all projects in the current directory.")
def display_projects_command():
    display_projects()


@app.command(help="Startup development applications and windows")
def dev_startup() -> None:
    development_startup()
