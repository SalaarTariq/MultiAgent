"""Shared tools used by agents.

The Serper-backed Google search tool requires SERPER_API_KEY in the environment.
"""
from crewai_tools import SerperDevTool

# Cap results so prompts stay within a useful size for the small Groq model.
google_search_tool = SerperDevTool(n_results=5)
