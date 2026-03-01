from groq import Groq as GroqClient

from config.settings import Settings

settings = Settings()
GROQ_API_KEY = settings.GROQ_API_KEY

_client = None
_current_model_name = None


def get_groq_client():
    """Get or create a Groq client instance."""
    global _client
    if _client is None:
        _client = GroqClient(api_key=GROQ_API_KEY)
    return _client


def get_groq_llm(model_name: str):
    """Get a Groq client configured for the given model."""
    global _current_model_name
    _current_model_name = model_name
    return get_groq_client()


# Keep old name for backward compatibility
def get_ollama_llm(model_name: str):
    """Deprecated: use get_groq_llm instead."""
    return get_groq_llm(model_name)