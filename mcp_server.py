# mcp_server.py

from mcp.server.fastmcp import FastMCP

# Initialize your MCP server
mcp = FastMCP("SecureReport-MCP")

# Run the server
if __name__ == "__main__":
    mcp.run()