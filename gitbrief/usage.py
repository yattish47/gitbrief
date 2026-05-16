from pathlib import Path
from datetime import datetime
import json

USAGE_FILE = Path.home() / ".gitbrief" / "usage.log"

def save_usage(prompt_tokens, completion_tokens, model):
    USAGE_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "model": model,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": prompt_tokens + completion_tokens
    }

    with open(USAGE_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

def print_stats():
    if not USAGE_FILE.exists():
        print("No usage data yet. Run gitbrief first.")
        return

    entries = []
    with open(USAGE_FILE, "r") as f:
        for line in f:
            entries.append(json.loads(line))

    total_runs = len(entries)
    total_tokens = sum(e["total_tokens"] for e in entries)
    total_prompt = sum(e["prompt_tokens"] for e in entries)
    total_completion = sum(e["completion_tokens"] for e in entries)

    print(f"\n📊 gitbrief usage stats")
    print(f"─────────────────────────")
    print(f"Total runs:         {total_runs}")
    print(f"Prompt tokens:      {total_prompt}")
    print(f"Completion tokens:  {total_completion}")
    print(f"Total tokens:       {total_tokens}")
    print(f"Last used:          {entries[-1]['date']}\n")