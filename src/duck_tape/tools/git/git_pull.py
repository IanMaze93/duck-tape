
import subprocess

from rich.console import Console
import os
from dotenv import load_dotenv

from rich.console import Console

load_dotenv()
console = Console()

username = os.getenv("SSH_USERNAME")
server = os.getenv("SSH_SERVER_IP")
server_project_dir = os.getenv("SERVER_PROJECT_DIR")

def git_pull(project: str) -> None:
    subprocess.run(
    [
        "ssh",
        f"{username}@{server}",
        f"cd {server_project_dir}/{project} && git pull origin main"
    ],
    check=True,
)

def git_pull_changes(project: str) -> None:
    console.print(f"[yellow]Moving to main branch...[/yellow]")

    console.print(f"[yellow]Pulling latest changes from {project}...[/yellow]")

    git_pull(project)

    console.print("[green]Done![/green]")