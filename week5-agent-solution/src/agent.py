from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from tools.custom_tool import ClauseClassifierTool
import os

def run_agent(query: str):
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0)
    memory = ConversationBufferMemory(memory_key="chat_history")

    tools = [
        Tool.from_function(func=ClauseClassifierTool()._run, name="ClauseClassifier", description="Classify clauses into categories"),
    ]

    agent = initialize_agent(tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, memory=memory, verbose=True)

    return agent.run(query)

if __name__ == "__main__":
    print(run_agent("Classify: Payment must be made in 30 days."))
