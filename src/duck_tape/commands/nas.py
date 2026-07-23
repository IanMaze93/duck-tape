from duck_tape.commands.nas_commands.all import backup_all
from duck_tape.commands.nas_commands.notes import backup_notes
from duck_tape.commands.nas_commands.databases import backup_databases
from duck_tape.tools.nas.check_space import check_space
import typer
from rich.console import Console

console = Console()

app = typer.Typer(
    help="NAS Commands",
    no_args_is_help=True,
)


@app.command("check-space", help="Show NAS storage details.")
def check_space_command():
    check_space()


@app.command("backup-all", help="Backup everything.")
def backup_all_command():
    backup_all()


@app.command("backup-notes", help="Backup all notes.")
def backup_notes_command():
    backup_notes()


@app.command("backup-dbs", help="Backup all databases.")
def backup_databases_command():
    backup_databases()
