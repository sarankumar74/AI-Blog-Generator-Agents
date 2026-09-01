from crewai import Agent, LLM

from tools import search_tool

from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="gemini/gemini-3.6-flash",
    temperature=0.5,
)


news_research = Agent(
    role="Senior Researcher",

    goal=(
        "Conduct in-depth research on emerging technologies in {topic} "
        "and provide a comprehensive report."
    ),

    backstory=(
        "You are an experienced technology researcher who specializes "
        "in finding accurate and useful information."
    ),

    llm=llm,

    tools=[search_tool],

    verbose=True,

    allow_delegation=False,
)


news_writer = Agent(
    role="Professional Technology Writer",

    goal=(
        "Write a compelling and informative article about {topic} "
        "using the research provided by the Researcher."
    ),

    backstory=(
        "You are an experienced technology writer who turns complex "
        "technical research into clear and engaging articles."
    ),

    llm=llm,

    verbose=True,

    allow_delegation=False,
)