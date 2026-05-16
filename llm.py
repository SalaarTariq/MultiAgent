"""Centralized LLM configuration shared by all agents and the crew runner.

Importing this module does NOT validate the API key; that happens on first call
to `get_llm()` so tests and tooling can import agents without credentials.
"""
import os

from crewai import LLM

MODEL = "groq/llama-3.1-8b-instant"


def get_llm(temperature: float = 0) -> LLM:
    """Return a configured LLM instance. Raises if GROQ_API_KEY is missing."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Export it in your shell or put it in a .env file."
        )
    return LLM(model=MODEL, api_key=api_key, temperature=temperature)
