from llama_index.core.llms import ChatMessage, MessageRole

from llm_factory.get_llm import get_groq_llm, _current_model_name

def get_answer(model_name, chat_history):
    client = get_groq_llm(model_name)
    
    # Prepare messages for Groq API
    messages = [
        {"role": "system", "content": "You are a helpful chat assistant."},
    ]
    
    # Add chat history
    for msg in chat_history:
        messages.append({"role": msg["role"], "content": msg["content"]})
    
    # Call Groq API
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
    )
    return response.choices[0].message.content


# example usage
# model_name = "llama3:latest"
# chat_history = [
#     {"role": "user", "content": "What is Artificial Intelligence?"}
# ]
# response = get_answer(model_name, chat_history)
# print(response)