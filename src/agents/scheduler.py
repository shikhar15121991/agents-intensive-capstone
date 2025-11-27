from typing import Any, Dict, List
from google_adk import ToolAgent, AgentContext


class SchedulerAgent(ToolAgent):
    """Produces a schedule aligned with constraints and availability."""

    def run(self, context: AgentContext) -> Dict[str, Any]:
        prioritized: List[Dict[str, Any]] = context.get("prioritized_tasks", [])
        schedule: Dict[str, Any] = {"plan": prioritized}
        context.set("schedule", schedule)
        return schedule
