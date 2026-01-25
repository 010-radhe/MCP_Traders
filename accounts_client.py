import mcp
from mcp.client.stdio import stdio_client
from mcp import StdioServerParameters
from agents import FunctionTool
import json

# Server startup configuration - tells Python how to launch the accounts server
# Command: "uv run accounts_server.py" - starts the server process
params = StdioServerParameters(command="uv", args=["run", "accounts_server.py"], env=None)


# Get list of available tools from the server
# Returns: List of tools like [buy_shares, sell_shares, get_balance, ...]
async def list_accounts_tools():
    async with stdio_client(params) as streams:  # Start server and get communication streams
        async with mcp.ClientSession(*streams) as session:  # Create MCP session
            await session.initialize()  # Handshake with server
            tools_result = await session.list_tools()  # Ask: "What tools do you have?"
            return tools_result.tools
        
# Execute a tool on the server
# Example: call_accounts_tool("buy_shares", {"name": "warren", "symbol": "AAPL", "quantity": 10})
async def call_accounts_tool(tool_name, tool_args):
    async with stdio_client(params) as streams:
        async with mcp.ClientSession(*streams) as session:
            await session.initialize()
            result = await session.call_tool(tool_name, tool_args)  # Run the tool on server
            return result
            
# Read account data as a resource (read-only)
# URI format: accounts://accounts_server/{name}
# Returns: Full account report (JSON with balance, holdings, transactions, P&L)
async def read_accounts_resource(name):
    async with stdio_client(params) as streams:
        async with mcp.ClientSession(*streams) as session:
            await session.initialize()
            result = await session.read_resource(f"accounts://accounts_server/{name}")
            return result.contents[0].text  # Extract text content from response
        
# Read trading strategy for an account
# URI format: accounts://strategy/{name}
# Returns: Strategy text (e.g., "You are Warren, a value investor...")
async def read_strategy_resource(name):
    async with stdio_client(params) as streams:
        async with mcp.ClientSession(*streams) as session:
            await session.initialize()
            result = await session.read_resource(f"accounts://strategy/{name}")
            return result.contents[0].text

# Convert MCP tools to AI-compatible FunctionTools
# This creates "remote control buttons" that AI agents can press
# When AI calls a tool, on_invoke_tool sends the request to the server
async def get_accounts_tools_openai():
    openai_tools = []
    
    # Get all tools from server and wrap each one
    for tool in await list_accounts_tools():
        # Copy schema and add strict validation (no extra fields allowed)
        schema = {**tool.inputSchema, "additionalProperties": False}
        
        # Create AI-compatible wrapper
        openai_tool = FunctionTool(
            name=tool.name,                 # Tool name: "buy_shares"
            description=tool.description,   # What it does (from docstring)
            params_json_schema=schema,      # Parameter definitions
            # Callback: when AI uses this tool, call the server
            # toolname=tool.name captures the current tool name (closure trick)
            on_invoke_tool=lambda ctx, args, toolname=tool.name: call_accounts_tool(toolname, json.loads(args))
                
        )
        openai_tools.append(openai_tool)
    
    return openai_tools