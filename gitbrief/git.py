import subprocess

def get_staged_diff():
    result = subprocess.run(
        ["git", "diff", "--staged"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise Exception("Not inside a git repo or git is not installed.")

    if not result.stdout.strip():
        raise Exception("No staged changes found. Run git add first.")

    return result.stdout