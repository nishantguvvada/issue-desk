import uvicorn
from server import app
from mcp_server import mcp

def main():
    uvicorn.run(app=app, host="0.0.0.0", port=3000)
    mcp.run()

if __name__ == "__main__":
    main()