import uvicorn
import threading
from server import app
from mcp_server import mcp

def start_mcp():
    mcp.run()

if __name__ == "__main__":

    mcp_thread = threading.Thread(target=start_mcp, daemon=True)
    mcp_thread.start()

    uvicorn.run(app=app, host="0.0.0.0", port=3000)
    mcp.run()

    mcp_thread.join()