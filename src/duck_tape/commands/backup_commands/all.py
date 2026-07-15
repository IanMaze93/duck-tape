from rich.console import Console

from duck_tape.commands.backup_commands.databases import backup_databases
from duck_tape.commands.backup_commands.notes import backup_notes


console = Console()


def backup_all():
    """
    Backup all notes, and databases.
    """

    backup_notes()

    backup_databases()
