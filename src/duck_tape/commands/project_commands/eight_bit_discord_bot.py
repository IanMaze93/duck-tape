import typer
from rich.console import Console

from duck_tape.tools.docker.deploy import docker_deploy_command
from duck_tape.tools.git.git_pull import git_pull_changes

app = typer.Typer(
    help="Commands for Ian's 8Bit Discord Bot Project",
    no_args_is_help=True,
)

project = "8Bit-Bot"
console = Console()


@app.command(
    "pull",
    help="Pull the latest changes from the remote repository to the server.",
)
def pull_changes_command() -> None:
    git_pull_changes(project)


@app.command("deploy", help="Deploy the 8Bit Discord Bot project to the server.")
def deploy_to_server_command() -> None:
    docker_deploy_command(project)
