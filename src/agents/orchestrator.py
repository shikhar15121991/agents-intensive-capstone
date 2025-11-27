from google.adk.agents import SequentialAgent, LoopAgent, AgentContext
from src.agents.extractor import ExtractorAgent
from src.agents.priority import PriorityAgent
from src.agents.scheduler import SchedulerAgent
from src.agents.reflection import ReflectionAgent
from src.agents.communication import CommunicationAgent
from src.memory import FAISSMemory
from src.utils import configure_gemini

class Orchestrator:
    def __init__(self):
        configure_gemini()
        self.memory = FAISSMemory()
        self.context = AgentContext()
        self.extractor = ExtractorAgent()
        self.priority = PriorityAgent()
        self.scheduler = SchedulerAgent()
        self.reflection = ReflectionAgent()
        self.communication = CommunicationAgent()

        self.workflow = SequentialAgent(
            agents=[
                self._extract_step,
                self._priority_step,
                self._schedule_step,
                LoopAgent(agent=self._reflection_step, max_iterations=2),
                self._communication_step
            ]
        )

    def _extract_step(self, ctx):
        tasks = self.extractor.run(ctx["input_text"])
        for t in tasks:
            self.memory.store(t)
        ctx["tasks"] = tasks
        return ctx

    def _priority_step(self, ctx):
        context = self.memory.retrieve("prioritize tasks")
        ctx["prioritized"] = self.priority.run(ctx["tasks"], context)
        return ctx

    def _schedule_step(self, ctx):
        ctx["schedule"] = self.scheduler.run(ctx["prioritized"])
        return ctx

    def _reflection_step(self, ctx):
        ctx["schedule"] = self.reflection.run(ctx["schedule"])
        return ctx

    def _communication_step(self, ctx):
        ctx["final"] = self.communication.run(ctx["schedule"])
        return ctx

    def run(self, input_text):
        self.context["input_text"] = input_text
        final_context = self.workflow.run(self.context)
        return final_context["final"]

if __name__ == "__main__":
    sample_text = "Prepare Kaggle notebook, write README, build Streamlit UI, test FAISS memory."
    orchestrator = Orchestrator()
    result = orchestrator.run(sample_text)
    print(result)
