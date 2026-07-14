from pathlib import Path
from duck_tape.commands.project_commands.common import display_projects
from duck_tape.commands.project_commands import data_pulse, web_portfolio
from duck_tape.commands.project_commands import eight_bit_backend
import typer
from rich.console import Console
from duck_tape.commands.project_commands import data_pulse

app = typer.Typer(
    help="Code Commands for Ian's Projects",
    no_args_is_help=True,
)

# Add the project-specific commands under code
app.add_typer(
    web_portfolio.app, 
    name="web_portfolio", 
    help="Code Commands for Ian's Web Portfolio."
)
app.add_typer(
    eight_bit_backend.app, 
    name="8bit-backend", 
    help="Code Commands for Ian's 8Bit's Backend Project."
)
app.add_typer(
    data_pulse.app, 
    name="data-pulse", 
    help="Code Commands for Ian's DataPulse HomeLab Project."
)

console = Console()
@app.command("display-projects", help="Display all projects in the current directory.")
def display_projects_command():
    display_projects()