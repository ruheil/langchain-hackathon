import os
from dotenv import load_dotenv
load_dotenv()
#os.environ["LANGCHAIN_TRACING"] = "true"

from langchain import OpenAI, ConversationChain
from langchain.tools import Tool
from langchain.prompts import PromptTemplate
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from langchain.memory import ConversationBufferWindowMemory
from ticket import *
from customer import *

        
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo") 


search = SerpAPIWrapper()
tools = [
    StructuredTool.from_function(openTicket),
    Tool.from_function(
        func=search.run,
        name = "Search",
        description="useful for when you need to answer questions. search for a solution to a problem",
    ),
    StructuredTool.from_function(getCustomerData),
    StructuredTool.from_function(viewCustomersData),
    StructuredTool.from_function(createCustomer),
    StructuredTool.from_function(viewTickets),
]


# Initialize the agent with the tools and language model
agent = initialize_agent(tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

memory = ConversationBufferWindowMemory(memory_key="chat_history", k=3)

# Run the agent with user input
while True:
    user_input = input("User: ")
    try:
        response = agent.run(user_input)
    
    # Use normal LLM to generate a response
    except Exception as e:
        openai_llm = OpenAI(temperature=0)
        response = openai_llm(user_input)

    print(response)
    memory.chat_memory.add_user_message(user_input)
    memory.chat_memory.add_ai_message(response)
    #print(memory.chat_memory.messages)