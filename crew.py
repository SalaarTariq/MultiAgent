from crewai import Crew, Process
from agent import researcher, writer, proof_reader
from tasks import research_task, write_task, proof_read_task
from langchain_groq import ChatGroq
import os

model = "llama-3.1-8b-instant"

from crewai import LLM
import os

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)
crew = Crew(
    agents=[researcher, writer, proof_reader],
    tasks=[research_task, write_task, proof_read_task],
    process=Process.sequential,
    llm=llm,              # 🔑 THIS LINE FIXES EVERYTHING
    verbose=True,
    memory=False, # Disable memory
    planning=False,
    max_rpm=10
)

topic = "Artificial Intelligence"
result = crew.kickoff(inputs={"topic": topic})

print(result)
