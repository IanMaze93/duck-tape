import os
import subprocess
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()
username = os.getenv("SSH_USERNAME")
server = os.getenv("SSH_SERVER_IP")
eight_bit_database = os.getenv("EIGHT_BIT_DATABASE")
eight_bit_database_path = os.getenv("EIGHT_BIT_DATABASE_DESTINATION_PATH")
planka_database_path = os.getenv("PLANKA_DATABASE_PATH")
planka_database = os.getenv("PLANKA_DATABASE")
server_connection = os.getenv("SERVER_CONNECTION")

console = Console()


def backup_databases():
    """
    Backup all databases.
    """

    home_path = Path.home()
    source_path = Path(home_path / eight_bit_database)

    new_date = subprocess.run(
        ["date", "+%m-%d-%y"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()

    remote__8Bit_backup_path = (
        f"{eight_bit_database_path.rstrip('/')}/backup-{new_date}"
    )
    remote_planka_backup_path = f"{planka_database_path.rstrip('/')}/backup-{new_date}"

    # Backup 8Bit database
    console.log(
        f"Backing up 8Bit database to the server: {source_path} -> {remote__8Bit_backup_path}",
        style="bold green",
    )

    eight_bit_remote_command = (
        f"docker exec {eight_bit_database} "
        f"mongodump --archive "
        f"> {remote__8Bit_backup_path}"
    )

    subprocess.run(
        [
            "ssh",
            f"{username}@{server}",
            eight_bit_remote_command,
        ],
        check=True,
    )

    # backup planka database
    console.log(
        f"Backing up Planka database to the server: {planka_database_path} -> {remote_planka_backup_path}",
        style="bold green",
    )

    plank_remote_command = (
        f"docker exec {planka_database} "
        f"pg_dumpall -U postgres "
        f"> {remote_planka_backup_path}"
    )

    subprocess.run(
        [
            "ssh",
            f"{username}@{server}",
            plank_remote_command,
        ],
        check=True,
    )
