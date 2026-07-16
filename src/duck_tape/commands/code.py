from duck_tape.commands.project_commands.common import display_projects
from duck_tape.tools.dev_tools.tools import development_startup
from duck_tape.commands.project_commands import data_pulse, web_portfolio
from duck_tape.commands.project_commands import eight_bit_backend, eight_bit_discord_bot
import typer
from rich.console import Console

console = Console()

app = typer.Typer(
    help="Code Commands for Ian's Projects",
    no_args_is_help=True,
)

# Add the project-specific commands under code
app.add_typer(
    web_portfolio.app,
    name="web_portfolio",
    help="Code Commands for Ian's Web Portfolio.",
)
app.add_typer(
    eight_bit_backend.app,
    name="8bit-backend",
    help="Code Commands for Ian's 8Bit Backend Project.",
)
app.add_typer(
    eight_bit_discord_bot.app,
    name="8bit-discord-bot",
    help="Code Commands for Ian's 8Bit Discord Bot Project.",
)
app.add_typer(
    data_pulse.app,
    name="data-pulse",
    help="Code Commands for Ian's DataPulse HomeLab Project.",
)


# Other code-related commands can be added here as needed
@app.command("display-projects", help="Display all projects in the current directory.")
def display_projects_command():
    display_projects()


@app.command(help="Startup development applications and windows")
def dev_startup() -> None:
    development_startup()
