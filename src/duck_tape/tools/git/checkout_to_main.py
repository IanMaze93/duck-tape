
import subprocess

def checkout_to_main(project_dir: str) -> None:
    subprocess.run(
        ["git", "checkout", "main"],
        cwd=project_dir,
        check=True,
    )