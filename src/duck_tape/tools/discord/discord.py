import subprocess


def launch_discord():
    """
    Starts Discord.
    """

    subprocess.Popen(
        ["discord"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        start_new_session=True,
    )
