import typer
from rich.console import Console

from duck_tape.tools.docker.deploy import docker_deploy_command
from duck_tape.tools.git.git_pull import git_pull_changes

app = typer.Typer(
    help="Commands for Ian's 8Bit Backend Project",
    no_args_is_help=True,
)

project = "8Bit-Backend"
console = Console()


@app.command(
    "pull-changes-to-server",
    help="Pull the latest changes from the remote repository for the 8Bit Backend project.",
)
def pull_changes_command() -> None:
    git_pull_changes(project)


@app.command("deploy-to-server", help="Deploy the 8Bit Backend project to the server.")
def deploy_to_server_command() -> None:
    docker_deploy_command(project)
