from llm_factory.get_llm import get_groq_llm


def get_chat_title(model, user_query):
    client = get_groq_llm(model)
    
    title_prompt = (
        "You are a helpful assistant that generates short, clear, and catchy titles.\n\n"
        "Task:\n- Read the given user query.\n- Create a concise title (max 7 words).\n"
        "- The title should summarize the intent of the query.\n"
        "- Avoid unnecessary words, punctuation, or filler.\n"
        "- Keep it professional and easy to understand.\n\n"
        f"User Query:\n{user_query}\n\n"
        "Output:\nTitle:"
    )
    
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": title_prompt}],
    )
    return response.choices[0].message.content.strip()