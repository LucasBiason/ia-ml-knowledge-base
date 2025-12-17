"""
OpenAI client singleton.
"""
import os
from openai import OpenAI
from app.core.config import settings

# Initialize OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def get_openai_client() -> OpenAI:
    """
    Get OpenAI client instance.
    
    Returns:
        OpenAI: Configured OpenAI client
    """
    return client





