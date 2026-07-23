import os
import subprocess
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()
notes_path = os.getenv("NOTES_PATH")
destination_path = os.getenv("NOTES_DESTINATION_PATH")
server_connection = os.getenv("SERVER_CONNECTION")

console = Console()


def backup_notes():
    """
    Backup all notes.
    """

    home_path = Path.home()
    source_path = Path(home_path / notes_path)

    new_date = subprocess.run(
        ["date", "+%m-%d-%y"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()

    remote_backup_path = f"{destination_path.rstrip('/')}/backup-{new_date}"
    console.log(
        f"Backing up notes to the server: {source_path} -> {server_connection}:{remote_backup_path}",
        style="bold green",
    )

    subprocess.run(
        [
            "scp",
            "-r",
            str(source_path),
            f"{server_connection}:{remote_backup_path}",
        ],
        check=True,
    )
