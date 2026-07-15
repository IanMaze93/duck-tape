from pathlib import Path

import typer


def create_executable() -> None:
    """Create a desktop launcher for duck-tape."""

    desktop_file = Path.home() / ".local/share/applications/duck-tape.desktop"

    desktop_file.parent.mkdir(parents=True, exist_ok=True)

    repo_path = Path(__file__).parent.parent.parent.parent.resolve()

    desktop_file.write_text(
        f"""
        [Desktop Entry]
        Version=1.0
        Type=Application
        Name=Duck Tape
        Comment=Personal development utilities
        Exec=gnome-terminal -- bash -c "cd {repo_path} && poetry run duck-tape; exec bash"
        Icon={repo_path}/duck_tape/images/duck-tape_logo.png
        Terminal=false
        Categories=Development;Utility;
        """,
        encoding="utf-8",
    )

    desktop_file.chmod(0o755)

    typer.echo(f"Created {desktop_file}")
