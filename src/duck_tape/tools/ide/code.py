import subprocess

from rich.console import Console

console = Console()


def launch_vscode():
    """
    Launches Visual Studio Code in the current directory.
    """
    try:
        subprocess.run(["code"], check=True)
        console.print("[green]Visual Studio Code launched successfully![/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Failed to launch Visual Studio Code: {e}[/red]")
