from crewai import Crew, Process

from agents import news_research, news_writer
from task import research_task, writer_task


blog_crew = Crew(
    agents=[
        news_research,
        news_writer
    ],

    tasks=[
        research_task,
        writer_task
    ],

    process=Process.sequential,

    verbose=True,

    memory=False,
)