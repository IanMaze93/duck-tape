import subprocess
import os
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()
console = Console()

check_space_command = os.getenv("CHECK_SPACE_COMMAND")
username = os.getenv("SSH_USERNAME")
server = os.getenv("SSH_SERVER_IP")
server_project_dir = os.getenv("SERVER_PROJECT_DIR")


def check_space():
    """Check the available space on the NAS."""
    subprocess.run(
        [
            "ssh",
            f"{username}@{server}",
            f"{check_space_command}",
        ],
        check=True,
    )
