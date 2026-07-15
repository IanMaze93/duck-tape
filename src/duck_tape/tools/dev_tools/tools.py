from rich.console import Console
from duck_tape.tools.browser.open import open_browser
from duck_tape.tools.ide.code import launch_vscode
from duck_tape.tools.music.spotify import launch_spotify
import os
from dotenv import load_dotenv

load_dotenv()
console = Console()

portainer_url = os.getenv("PORTAINER_URL")
planka_url = os.getenv("PLANKA_URL")


def development_startup() -> None:
    """Startup development applications and windows."""

    console.print("[yellow]Starting development applications and windows...[/yellow]")

    open_browser(portainer_url)

    open_browser(planka_url)

    open_browser("https://github.com")

    launch_vscode()

    launch_spotify()

    console.print(
        "[green]Development applications and windows started successfully![/green]"
    )
