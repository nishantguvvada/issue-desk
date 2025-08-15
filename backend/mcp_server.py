from fastmcp import FastMCP
from db import database_request

mcp = FastMCP("Portal Complaint Server", debug=True)

# Adding a tool

@mcp.tool
def fetch_issues() -> str:
    """Use the tool to fetch description of employee portal issues from the database."""
    return database_request()

@mcp.tool
def fetch_stats() -> str:
    """
        Use the tool to retrieve total number of resolutions, issues and unresolved tickets statistics around employee portal issues.
        The statistics include:
        - Total Issues: the total number of employee portal issues recorded.
        - Total Resolutions: the total number of issues resolved.
        - Total Unresolved Ticketes: the total number of issue tickets pending resolution.
    """
    return {
        "total issues": 537,
        "total resolutions": 470,
        "total unresolved tickets": 67
    }

if __name__ == "__main__":
    mcp.run()