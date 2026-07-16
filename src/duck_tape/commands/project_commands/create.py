import typer
from rich.console import Console

from duck_tape.tools.docker.deploy import docker_deploy_command
from duck_tape.tools.git.git_pull import git_pull_changes

console = Console()


def create_project(project_name: str) -> None:
    """Create a new project with the given name."""
    app = typer.Typer(
        help=f"Commands for Ian's {project_name} Project",
        no_args_is_help=True,
    )

    @app.command(
        "pull",
        help="Pull the latest changes from the remote repository to the server.",
    )
    def pull_changes_command() -> None:
        git_pull_changes(project_name)

    @app.command("deploy", help=f"Deploy the {project_name} project to the server.")
    def deploy_to_server_command() -> None:
        docker_deploy_command(project_name)

    return app
