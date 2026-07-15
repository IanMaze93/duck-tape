import subprocess
from time import sleep


def open_browser(url):
    """Open a web browser with the specified URL."""
    subprocess.run(["xdg-open", url])
    sleep(1)
