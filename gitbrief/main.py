import typer
from rich.console import Console
from gitbrief.git import get_staged_diff
from gitbrief.ai import generate_commit_message
import subprocess

app = typer.Typer()
console = Console()

@app.command()
def main():
    console.print("\n[bold cyan]gitbrief[/bold cyan] — AI commit message generator\n")

    with console.status("[cyan]Reading staged changes..."):
        try:
            diff = get_staged_diff()
        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")
            raise typer.Exit()

    console.print("[green]✓[/green] Staged changes found\n")
    console.print("[bold]Generating commit message...[/bold]\n")

    try:
        commit_message = generate_commit_message(diff)
    except Exception as e:
        console.print(f"\n[red]Error:[/red] {e}")
        raise typer.Exit()

    console.print("\n")
    confirm = typer.confirm("Use this commit message?")

    if confirm:
        subprocess.run(["git", "commit", "-m", commit_message])
        console.print("\n[green]✓ Committed successfully![/green]")
    else:
        console.print("\n[yellow]Commit cancelled.[/yellow]")

if __name__ == "__main__":
    app()