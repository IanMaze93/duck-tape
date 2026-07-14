
import subprocess


def git_pull(project_dir: str) -> None:
    """
    Pull the latest changes from the remote repository for the given project directory.

    Args:
        project_dir (str): The path to the project directory.
    """
    subprocess.run(
        ["git", "pull"],
        cwd=project_dir,
        check=True,
    )