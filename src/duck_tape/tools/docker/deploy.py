import os
import subprocess

from dotenv import load_dotenv
from rich.console import Console

load_dotenv()
console = Console()

username = os.getenv("SSH_USERNAME")
server = os.getenv("SSH_SERVER_IP")
server_project_dir = os.getenv("SERVER_PROJECT_DIR")


def docker_deploy(project: str) -> None:
    remote_command = (
        f"cd {server_project_dir}/{project} && docker compose up --build -d"
    )

    subprocess.run(
        [
            "ssh",
            f"{username}@{server}",
            remote_command,
        ],
        check=True,
    )


def docker_deploy_command(project: str) -> None:
    """
    Command to deploy the project using Docker.

    Args:
        project (str): The name of the project directory.
    """
    console.print(f"[yellow]Deploying {project} to the server using Docker...[/yellow]")
    docker_deploy(project)
    console.print("[green]Deployment complete![/green]")
