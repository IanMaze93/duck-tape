from pathlib import Path
import typer
from rich.console import Console

from duck_tape.tools.git.checkout_to_main import checkout_to_main
from duck_tape.tools.git.git_pull import git_pull

app = typer.Typer(
    help="Commands for Ian's Web Portfolio Project",
    no_args_is_help=True,
)

console = Console()

@app.command("pull-changes", help="Pull the latest changes from the remote repository for the web portfolio project.")
def pull_changes_command() -> None:
    project_dir = Path.home() / "Code" / "web_portfolio"
    console.print(f"[yellow]Moving to main branch...[/yellow]")

    checkout_to_main(project_dir)

    console.print(f"[yellow]Pulling latest changes from {project_dir}...[/yellow]")

    git_pull(project_dir)

    console.print("[green]Done![/green]")

@app.command("deploy-to-server", help="Deploy the web portfolio project to the server.")
def deploy_to_server_command() -> None:
    project_dir = Path.home() / "Code" / "web_portfolio"
    console.print(f"[yellow]Deploying {project_dir} to the server...[/yellow]")

    # Add your deployment logic here, e.g., using subprocess to run deployment commands

    console.print("[green]Deployment complete![/green]")