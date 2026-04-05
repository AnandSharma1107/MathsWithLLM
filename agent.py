from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent

# Creating Wikipedia, Mathematics and Reasoning tool
import math

def safe_calculator(expression: str):
    try:
        return str(eval(expression, {"__builtins__": {}}, vars(math)))
    except Exception as e:
        return f"Error: {str(e)}"
    

def create_tools(llm):
    # Creating Wikipedia tool
    wikipedia_wrapper=WikipediaAPIWrapper()
    wikipedia_tool=Tool(
        name="Wikipedia",
        func=wikipedia_wrapper.run,
        description="This is a tool for searching through the internet to find the information about the topics which are asked by user"

    )


    #Creating Mathematics Tool
    calculator=Tool(
        name="Calculator",
        func=safe_calculator,
        description="""
        Useful for solving mathematical expressions.
        Input must be a valid Python math expression.
        Examples:
        - 2+2
        - sqrt(16)
        - 10/5
         Do NOT include words.
        """
    ) 

    #Creating custom prompt for reasoning tool
    prompt="""
    Your a agent tasked for solving users mathemtical question. Logically arrive at the solution and provide a detailed explanation
    and display it point wise for the question below
    Question:{question}
    Answer:
    """
    
    prompt_template = PromptTemplate(
        input_variables=["question"],
        template=prompt
    )
    

    #creating a chain for conveniently running reasoning tool
    chain=LLMChain(llm=llm,prompt=prompt_template)

    # Creating Reasoning tool
    reasoning_tool=Tool(
        name="reasoning_tool",
        func=chain.run,
        description="A tool for answering logic-based and reasoning questions."
    )

    return [wikipedia_tool, calculator, reasoning_tool]

#Creating Agent
def create_agent(api_key : str):

    #Initializing LLM model
    llm=ChatGroq(model="openai/gpt-oss-120b",groq_api_key=api_key,temperature=0)

    assistant_agent=initialize_agent(
    tools=create_tools(llm),
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=False,
    handle_parsing_errors=True
    )
    return assistant_agent
