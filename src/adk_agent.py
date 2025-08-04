from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset,
)

from google.adk.tools.mcp_tool.mcp_session_manager import (
    StdioConnectionParams,
    StdioServerParameters,
)

root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="Box Agent with MCP",
    instruction="You are a helpful agent with access to the Box MCP server, and can help users access their Box instance",
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="uv",
                    args=[
                        "--directory",
                        "/Users/rbarbosa/Documents/code/python/box/mcp-server-box",
                        "run",
                        "src/mcp_server_box.py",
                    ],
                ),
            ),
            # Optional: Filter which tools from the MCP server are exposed
            # tool_filter=['list_directory', 'read_file']
        )
    ],
)
