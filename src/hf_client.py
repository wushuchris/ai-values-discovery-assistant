import os
from huggingface_hub import InferenceClient


def get_client():
    return InferenceClient(api_key=os.getenv("HF_TOKEN"))


def generate_values_statement(top_values, why, decision, living):
    client = get_client()

    system_prompt = (
        "You are an expert writing coach and values-clarification assistant. "
        "Your job is to synthesize a user's reflections into an original, polished personal values statement. "
        "Do not copy the user's wording line by line. "
        "Instead, infer themes, tighten the language, and produce a thoughtful summary in a natural human voice."
    )

    user_prompt = f"""
The user's top values are: {", ".join(top_values)}.

Here are the user's reflections:
Why these values matter:
{why}

A decision shaped by these values:
{decision}

What living these values looks like:
{living}

Write a polished personal values statement with:
1. A short title: "My Personal Values Statement"
2. One concise paragraph of 4-6 sentences
3. A second short paragraph explaining how these values guide decisions and daily behavior

Requirements:
- Sound thoughtful, warm, and professional
- Be more polished than the user's raw notes
- Do not simply repeat or list the inputs back verbatim
- Do not start with "My core values are..."
- Make the writing feel like a finished statement, not a summary dump
- Format the response in markdown
- Use this structure:

# Personal Values Statement

<1-2 strong paragraphs>

## What this means in Practice
-3-5 bullet points describing behaviors or decisions
"""

    completion = client.chat_completion(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_tokens=350,
        temperature=0.8,
    )

    print("DEBUG: using chat_completion with Llama 3.1")
    return completion.choices[0].message.content.strip()