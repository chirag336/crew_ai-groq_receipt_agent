from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import PDFSearchTool
from src.ai_pdf_total_price_extraction_agent.tools.custom_tool import MyCustomTool

@CrewBase
class AiPdfTotalPriceExtractionAgentCrew():
    """AiPdfTotalPriceExtractionAgent crew"""

    @agent
    def pdf_reader(self) -> Agent:
        return Agent(
            config=self.agents_config['price_extractor'],
            tools=[],
        )

    @agent
    def data_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['receipt_categorizer'],
            tools=[],
        )



    @task
    def read_pdf_task(self) -> Task:
        return Task(
            config=self.tasks_config['read_pdf_task'],
            tools=[MyCustomTool()],
        )

    @task
    def extract_price_task(self) -> Task:
        return Task(
            config=self.tasks_config['extract_type'],
            tools=[MyCustomTool()],
        )



    @crew
    def crew(self) -> Crew:
        """Creates the AiPdfTotalPriceExtractionAgent crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
