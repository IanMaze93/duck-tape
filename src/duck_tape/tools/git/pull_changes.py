from pathlib import Path
import typer
from rich.console import Console

from duck_tape.tools.git import checkout_to_main
from duck_tape.tools.git import git_pull

app = typer.Typer()

console = Console()

def git_pull_changes_command(project: str) -> None:
    project_dir = Path.home() / "Code" / project
    console.print(f"[yellow]Moving to main branch...[/yellow]")

    checkout_to_main(project_dir)

    console.print(f"[yellow]Pulling latest changes from {project_dir}...[/yellow]")

    git_pull(project_dir)

    console.print("[green]Done![/green]")
