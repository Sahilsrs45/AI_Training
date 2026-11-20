from crewai import Task
from agents.editor_agent import editor
from agents.writer_agent import writer
from agents.researcher_agent import researcher


def create_tasks(topic):

    research_task = Task(
        description=f"""
        Research the topic: {topic}

        Gather:
        - Introduction
        - Key concepts
        - Top 5 Benefits
        - Top 5 Challenges
        - Top 5 Future trends

        You are good at:
        -Collecting information from trusted sources
        - Identifying facts and statistics
        - Comparing multiple viewpoints
        - Discovering emerging trends
        - Verifying information accuracy 
        Provide detailed notes.
        """,
        expected_output="Detailed research notes",
        agent=researcher
    )

    writing_task = Task(
        description=f"""
        Using the research findings,
        write a professional article on {topic}.

        Include:
        - Introduction
        - Main Content
        - Conclusion
        """,
        expected_output="Complete article",
        agent=writer,
        context=[research_task]
    )

    editing_task = Task(
        description="""
        Review the article.

        Improve:
        - Grammar
        - Sentence Structure
        - Readability
        - Professional Tone
        """,
        expected_output="Final polished article",
        agent=editor,
        context=[writing_task]
    )

    return [research_task, writing_task, editing_task]