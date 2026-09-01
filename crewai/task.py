from crewai import Task

from agents import news_research, news_writer


research_task = Task(
    description=(
        "Conduct in-depth research on emerging technologies in {topic} "
        "and provide a comprehensive report."
    ),

    expected_output=(
        "A detailed research report highlighting the latest advancements, "
        "potential applications, and future trends in {topic}."
    ),

    agent=news_research,
)


writer_task = Task(
    description=(
        "Craft a compelling narrative based on the research findings "
        "on {topic}."
    ),

    expected_output=(
        "An engaging article that effectively communicates the significance "
        "of the research, its implications, and potential impact on the industry."
    ),

    agent=news_writer,

    async_execution=False,

    output_file="news_blog_post.md",
)