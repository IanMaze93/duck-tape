import subprocess
from time import sleep

from rich.console import Console

console = Console()


def launch_spotify():
    """
    Launches Spotify in the current directory.
    """
    try:
        subprocess.Popen(["spotify"])
        sleep(2)
        subprocess.run(["playerctl", "-p", "spotify", "play"])
        console.print("[green]Spotify launched successfully![/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Failed to launch Spotify: {e}[/red]")
