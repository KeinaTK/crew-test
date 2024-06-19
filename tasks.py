from crewai import Task
from textwrap import dedent


class Tasks():

  def review_code_task(self, agent, code):
    return Task(
      description=dedent(
        f"""
          Review the code for production deployment, providing detailed feedback
          on necessary changes, focusing on syntax and style. Identifying potential bugs.
          Ensure consistent indentation, proper use of spaces, appropriate line
          lengths, meaningful naming conventions. Identify potential issues such as
          null pointer dereferences, off-by-one errors, proper exception handling,
          and correct resource management.

          Your final answer must be a detailed review of the code provided. Showing
          code snippets and what should be changed. May use bullet points or other 
          methods of organize the changes. 

          Analize code: {code}
        """
      ),
      agent=agent, 
      expected_output='A comprehensive report on the review of the code.'
    )
  
  def qa_task(self, agent, code):
    return Task(
      description=dedent(
        f"""
          Test the code looking for bugs and possible security vulnerabilities.
          Conduct code analysis to detect common security issues such as SQL 
          injection, cross-site scripting (XSS), buffer overflows and improper 
          authentication and authorization.

          By conducting comprehensive performance and security reviews, QA ensure
          that software systems not only function correctly but also perform 
          optimally under varying conditions and remain resilient against potential 
          security threats.

          Your final answer must be a detailed review of the code provided. Showing
          code snippets and what should be changed. May use bullet points or other 
          methods of organize the changes. 

          Analize code: {code}
        """
      ),
      expected_output='A comprehensive report on the qa of the code',
      agent=agent
    )
  
  def documentation_task(self, agent, code):
    return Task(
      description=dedent(
        f"""
          Write a overview of the code with a few words in one or two paragraphs. 

          Your final answer must be a small documentation of the code provided.

          Analize code: {code}
        """
      ),
      expected_output='A comprehensive report on the documentation of the code',
      agent=agent
    )
