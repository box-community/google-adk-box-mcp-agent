from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_session_manager import (
    SseConnectionParams,
)
from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset,
)

root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="ADK_Agent_Box_MCP",
    instruction="You are a helpful agent with access to the Box MCP server, and can help users access their Box instance",
    tools=[
        MCPToolset(
            connection_params=SseConnectionParams(
                url="http://localhost:8001/sse",
            ),
            # Optional: Filter which tools from the MCP server are exposed
            # tool_filter=['list_directory', 'read_file']
        ),
    ],
)
