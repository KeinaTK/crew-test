from crewai import Crew
from agents import Agents
from tasks import Tasks

from dotenv import load_dotenv, find_dotenv
from textwrap import dedent


load_dotenv(find_dotenv())

class ReviewCodeCrew:

  def __init__(self, code):
    self.code = code

  def run(self):
    agents = Agents()
    tasks = Tasks()

    review_agent = agents.review_agent()
    qa_agent = agents.qa_agent()
    documentation_agent = agents.documentation_agent()

    review_code_task = tasks.review_code_task(review_agent, self.code)
    qa_task = tasks.qa_task(qa_agent, self.code)
    documentation_task = tasks.documentation_task(documentation_agent, self.code)

    crew = Crew(
      agents=[review_agent, qa_agent, documentation_agent],
      tasks=[review_code_task, qa_task, documentation_task],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Code Review")
  print('-------------------------------')
  code = input(dedent("Inform the code for revision\n"))
  
  result = ReviewCodeCrew(code).run()
  print("\n\n########################")
  print("## Here is you code reviewed")
  print("########################\n")
  print(result)
