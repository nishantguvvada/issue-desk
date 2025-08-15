from fastmcp import Client
import asyncio
from mcp_server import mcp

# Create a FastMCP client and point at the server object

mcp_client = Client(mcp)

# Tool call

async def greet(name: str):
    async with mcp_client:
        result = await mcp_client.call_tool("greet", {"name": name})
        print(result)

if __name__ == "__main__":
    asyncio.run(greet("Kim Jong Un"))