from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import os

load_dotenv()

@CrewBase
class MarketAnalysisFlow:
    """
    A flow for conducting market analysis using specialized agents.
    """
    def __init__(self):
        super().__init__()

    def kickoff(self):
        """Execute the crew's tasks."""
        return self.crew().kickoff()

    @agent
    def task_planner(self) -> Agent:
        """Creates the task planning agent."""
        return Agent(
            config=self.agents_config['task_planner'],
            verbose=True
        )

    @agent
    def agent_creator(self) -> Agent:
        """Creates the agent design specialist."""
        return Agent(
            config=self.agents_config['agent_creator'],
            verbose=True
        )

    @agent
    def config_writer(self) -> Agent:
        """Creates the configuration management specialist."""
        return Agent(
            config=self.agents_config['config_writer'],
            verbose=True
        )

    @task
    def planning_task(self) -> Task:
        """Creates the task planning task."""
        return Task(
            description=self.tasks_config['planning_task']['description'],
            expected_output=self.tasks_config['planning_task']['expected_output'],
            agent=self.task_planner()
        )

    @task
    def agent_creation_task(self) -> Task:
        """Creates the agent design task."""
        return Task(
            description=self.tasks_config['agent_creation_task']['description'],
            expected_output=self.tasks_config['agent_creation_task']['expected_output'],
            agent=self.agent_creator(),
            context=[self.planning_task()]
        )

    @task
    def config_writing_task(self) -> Task:
        """Creates the configuration writing task."""
        return Task(
            description=self.tasks_config['config_writing_task']['description'],
            expected_output=self.tasks_config['config_writing_task']['expected_output'],
            agent=self.config_writer(),
            context=[self.planning_task(), self.agent_creation_task()]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MarketAnalysis crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
