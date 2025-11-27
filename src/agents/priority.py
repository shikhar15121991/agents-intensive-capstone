from typing import Any, Dict, List
from google_adk import ToolAgent, AgentContext


class PriorityAgent(ToolAgent):
    """Scores and orders tasks using model-based reasoning."""

    def run(self, context: AgentContext) -> List[Dict[str, Any]]:
        tasks: List[Dict[str, Any]] = context.get("tasks", [])
        # Replace with Gemini scoring output
        ordered = tasks
        context.set("prioritized_tasks", ordered)
        return ordered
