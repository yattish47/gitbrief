from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

SYSTEM_PROMPT = """You are a helpful assistant that writes git commit messages.
Given a git diff, write a single commit message in conventional commits format.
Rules:
- Use prefixes like feat:, fix:, chore:, refactor:, docs:
- Keep the subject line under 72 characters
- Return only the commit message, nothing else
- No explanations, no markdown, just the commit message
"""

def generate_commit_message(diff):
    stream = client.chat.completions.create(
        model="llama3.2",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Write a commit message for this diff:\n\n{diff}"}
        ],
        stream=True
    )

    full_message = ""
    for chunk in stream:
        text = chunk.choices[0].delta.content or ""
        print(text, end="", flush=True)
        full_message += text

    print()
    return full_message.strip()