from typing import Any, Dict, List
from google_adk import ToolAgent, AgentContext


class ExtractorAgent(ToolAgent):
    """Parses raw inputs and yields normalized task objects."""

    def run(self, context: AgentContext) -> List[Dict[str, Any]]:
        input_data = context.get("input_data")
        tasks = [
            {"title": "Draft status update", "deadline": None, "metadata": {"source": "text"}},
            {"title": "Organize deck", "deadline": None, "metadata": {"source": "text"}},
        ]
        context.set("tasks", tasks)
        return tasks
