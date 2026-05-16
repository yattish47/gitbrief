# gitbrief

AI-powered commit message generator that runs entirely on your machine. Stage your changes, run `gitbrief`, and get a clean conventional commit message generated from your actual code diff — no cloud, no API costs, just your local LLM.

---

## How it works

1. You stage your changes with `git add`
2. Run `gitbrief` in your terminal
3. It reads your staged diff with `git diff --staged`
4. Sends the diff to your local `llama3.2` model via Ollama
5. Streams back a commit message in conventional commits format
6. Asks you to confirm — if yes, it commits for you automatically

---

## Use case

Tired of writing vague commit messages like `"fixed stuff"` or `"updates"`? gitbrief reads exactly what changed in your code and writes a descriptive, properly formatted commit message for you. It runs 100% locally using Ollama so your code never leaves your machine.

---

## Prerequisites

- Python 3.11+
- [Ollama](https://ollama.com) installed and running
- `llama3.2` model pulled locally

```bash
ollama pull llama3.2
```

---

## Installation

Clone the repo and install it as a CLI tool:

```bash
git clone https://github.com/YOURUSERNAME/gitbrief.git
cd gitbrief
uv tool install .
```

---

## Usage

Stage your files and run:

```bash
git add .
gitbrief
```

Example output:

```
gitbrief — AI commit message generator

✓ Staged changes found

Generating commit message...

feat: add streaming response and usage tracking to ai module

Use this commit message? [y/n]: y
✓ Committed successfully!
```

Check your token usage stats:

```bash
gitbrief stats
```

Example output:

```
📊 gitbrief usage stats
─────────────────────────
Total runs:         12
Prompt tokens:      8,420
Completion tokens:  312
Total tokens:       8,732
Last used:          2026-05-16 10:24:01
```

---

## Commit message format

gitbrief follows the [Conventional Commits](https://www.conventionalcommits.org) spec:

| Prefix | When to use |
|---|---|
| `feat:` | A new feature |
| `fix:` | A bug fix |
| `chore:` | Maintenance, dependencies |
| `refactor:` | Code restructure, no feature change |
| `docs:` | Documentation changes |

---

## Project structure

```
gitbrief/
├── pyproject.toml
├── README.md
└── gitbrief/
    ├── __init__.py
    ├── main.py        # CLI entry point
    ├── git.py         # reads staged diff
    ├── ai.py          # calls Ollama via OpenAI-compatible API
    └── usage.py       # tracks and displays token usage
```

---

## Built with

- [Ollama](https://ollama.com) — local LLM runtime
- [llama3.2](https://ollama.com/library/llama3.2) — the model doing the thinking
- [Typer](https://typer.tiangolo.com) — CLI framework
- [Rich](https://rich.readthedocs.io) — terminal output
- [uv](https://astral.sh/uv) — Python package manager