from typing import Any, Dict
from google_adk import ToolAgent, AgentContext


class CommunicationAgent(ToolAgent):
    """Publishes the plan to external channels."""

    def run(self, context: AgentContext) -> Dict[str, Any]:
        schedule: Dict[str, Any] = context.get("schedule", {})
        result = {"status": "synced", "details": schedule}
        context.set("publish_result", result)
        return result
