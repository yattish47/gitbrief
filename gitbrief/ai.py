from openai import OpenAI
from gitbrief.usage import save_usage

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
        stream=True,
        stream_options={"include_usage": True}
    )

    full_message = ""
    prompt_tokens = 0
    completion_tokens = 0

    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            text = chunk.choices[0].delta.content
            print(text, end="", flush=True)
            full_message += text
        
        if hasattr(chunk, "usage") and chunk.usage:
            prompt_tokens = chunk.usage.prompt_tokens
            completion_tokens = chunk.usage.completion_tokens

    print()
    save_usage(prompt_tokens, completion_tokens, "llama3.2")
    return full_message.strip()