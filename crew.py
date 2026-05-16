"""Entry point: run the research → write → proofread crew on a given topic.

Usage:
    python crew.py "Artificial Intelligence"
    python crew.py            # defaults to "Artificial Intelligence"

Requires GROQ_API_KEY and SERPER_API_KEY in the environment (or in a .env file).
"""
import os
import sys

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    # python-dotenv is optional; env vars can still be exported manually.
    pass

from crewai import Crew, Process

from agent import researcher, writer, proof_reader
from llm import get_llm
from tasks import research_task, write_task, proof_read_task

DEFAULT_TOPIC = "Artificial Intelligence"


def _require_env(*names: str) -> None:
    missing = [n for n in names if not os.getenv(n)]
    if missing:
        raise SystemExit(
            f"Missing required env var(s): {', '.join(missing)}. "
            "Export them in your shell or add them to a .env file."
        )


def build_crew() -> Crew:
    return Crew(
        agents=[researcher, writer, proof_reader],
        tasks=[research_task, write_task, proof_read_task],
        process=Process.sequential,
        llm=get_llm(),
        verbose=True,
        memory=False,
        planning=False,
        max_rpm=30,
    )


def main(topic: str = DEFAULT_TOPIC) -> None:
    _require_env("GROQ_API_KEY", "SERPER_API_KEY")
    crew = build_crew()
    result = crew.kickoff(inputs={"topic": topic})
    print(result)


if __name__ == "__main__":
    topic = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TOPIC
    main(topic)
