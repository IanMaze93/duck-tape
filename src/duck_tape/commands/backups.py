from duck_tape.commands.backup_commands.all import backup_all
from duck_tape.commands.backup_commands.notes import backup_notes
from duck_tape.commands.backup_commands.databases import backup_databases
import typer
from rich.console import Console

console = Console()

app = typer.Typer(
    help="Backup Commands",
    no_args_is_help=True,
)


@app.command("backup-all", help="Backup everything.")
def backup_all_command():
    backup_all()


@app.command("backup-notes", help="Backup all notes.")
def backup_notes_command():
    backup_notes()


@app.command("backup-dbs", help="Backup all databases.")
def backup_databases_command():
    backup_databases()
