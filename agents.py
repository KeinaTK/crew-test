from crewai import Agent
from tools.search_tools import SearchTools


class Agents():

  def review_agent(self):
    return Agent(
        role='Senior Backend Developer',
        goal='Review the code for production deployment, providing detailed feedback \
            on necessary changes, focusing on syntax and style. Identifying potential bugs. \
            Ensure consistent indentation, proper use of spaces, appropriate line \
            lengths, meaningful naming conventions. Identify potential issues such as \
            null pointer dereferences, off-by-one errors, proper exception handling, \
            and correct resource management.',
        backstory='An expert backend developer in analyzing and writing code',
        tools=[
            SearchTools.search_internet
        ],
        verbose=True
    )

  def qa_agent(self):
    return Agent(
        role='Quality Assurance',
        goal='Test the code and garantee it has no bugs and invunerabilities after \
            the conclusion of the revision of the code',
        backstory='You are a quality assurance expert that always tests every code',
        tools=[
            SearchTools.search_internet,
        ],
        verbose=True
    )

  def documentation_agent(self):
    return Agent(
        role='Expert in documenting code',
        goal='Write the documentation of the code. After the code finish being reviewed \
            and tested, you are responsible for documenting what the code does. ',
        backstory='You are a previus backend developer and now document the code',
        tools=[
            SearchTools.search_internet,
        ],
        verbose=True
    )
