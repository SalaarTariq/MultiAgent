# MultiAgent

A small CrewAI pipeline that produces a short newsletter-style article on a
given topic. Three agents work sequentially:

1. **Researcher** — gathers facts via Serper / Google search.
2. **Writer** — turns research into a 4-paragraph markdown article.
3. **Proofreader** — polishes the article, adds sources, and writes the final file.

The output is written to `outputs/newsletter-<timestamp>.md`.

## Requirements

- Python 3.11
- [pipenv](https://pipenv.pypa.io/) (or `pip` + a virtualenv)
- A [Groq](https://console.groq.com/) API key (used for the LLM)
- A [Serper](https://serper.dev/) API key (used for web search)

## Setup

```bash
pipenv install
```

Create a `.env` file in the project root:

```
GROQ_API_KEY=your-groq-key
SERPER_API_KEY=your-serper-key
```

## Usage

```bash
# default topic ("Artificial Intelligence")
pipenv run python crew.py

# custom topic
pipenv run python crew.py "Quantum Computing"
```

The final article is written to `outputs/newsletter-<timestamp>.md` and also
printed to stdout.

## Project layout

```
crew.py     # entrypoint: builds the Crew and runs it
agent.py    # the three agent definitions
tasks.py    # task definitions wired to agents
tools.py    # shared tools (Serper search)
llm.py      # centralized LLM (Groq llama-3.1-8b-instant) configuration
```
