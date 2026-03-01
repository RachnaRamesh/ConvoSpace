def get_ollama_models_list():
    # Groq API models available for this app.
    # Return list because the rest of the app expects an iterable for selectbox.
    return [
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile",
        "openai/gpt-oss-120b",
    ]


# Example usage
# check_ollama_models = get_ollama_models_list()
# print(type(check_ollama_models))   # <class 'list'>
# print(check_ollama_models)         # ['qwen3:4b', 'qwen3:4b', 'llama3:latest']