# Issue Desk Chatbot

An AI-powered chatbot application designed to provide employees with real-time updates and summaries of technical issues reported in the **Employee Portal**. The system leverages an **MCP server** to fetch the latest issues and statistics from a connected database, allowing the chatbot to answer employee queries efficiently.

---

## Features

- **Real-time Issue Fetching:** The chatbot retrieves the most recent portal issues from the MCP server’s database.
- **Issue Summarization:** Provides concise summaries of reported issues for quick understanding.
- **Statistics Reporting:** Accesses MCP server statistics tools to show total issues, resolved tickets, and unresolved tickets.
- **AI-powered Responses:** Uses a language model to answer employee queries in a structured, context-aware manner.
- **Async and Persistent Connections:** MCP client maintains a persistent connection for fast and reliable responses.

---

## Tech Stack

- **Frontend:** React, Tailwind CSS
- **Backend:** FastAPI (Python)
- **AI Model:** Google GenAI (`gemini-2.0-flash`), FastMCP
- **Database:** MongoDB
- **Asynchronous Handling:** `asyncio` for async API calls and MCP client operations
- **Deployment:** Uvicorn ASGI server

---

## Key Components

### 1. Ask Bot Endpoint (`POST /`)

- Receives user queries.
- Returns AI-generated responses based on MCP server data.

### 2. MCP Server Tools

- **`fetch_issues()`**: Returns the latest issues from the database.
- **`fetch_stats()`**: Returns statistics including:
  - Total issues
  - Resolved tickets
  - Unresolved tickets

### 3. Summarize Issues Tool

- Generates concise summaries of the latest portal issues for easier reading.

### 4. Report Statistics Tool

- Provides insights into current issue resolution statuses using MCP server statistics.
