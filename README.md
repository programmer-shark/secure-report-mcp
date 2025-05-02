# SecureReport-MCP 🛡️📄

[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![MCP-Compatible](https://img.shields.io/badge/MCP%20Support-FastMCP%20v1.6+-blueviolet)](https://github.com/modelcontextprotocol)
[![Built With 🦜 FastMCP](https://img.shields.io/badge/built%20with-FastMCP-yellow)](https://pypi.org/project/mcp/)

> A FastMCP server to generate password-protected PDF reports from plain text —  
> Includes a tool, resource, and prompt to demonstrate multi-modal LLM agent capabilities.

---

## 📦 Features

- 🔐 **Tool**: Create password-protected PDFs from any text input
- 📚 **Resource**: Example weekly summary (LLM-readable)
- 💬 **Prompt**: Ask for secure password suggestions
- 🧪 **Inspector-ready**: Test interactively with MCP Inspector

---

## 🚀 Setup & Run

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install "mcp[cli]" fpdf pikepdf
```

### 3. Run the MCP server

```bash
mcp dev mcp_server.py
```

This opens the MCP Inspector UI at:  
[http://127.0.0.1:6274](http://127.0.0.1:6274)

---

## 🔍 Available Components

| Type     | Name                          | Description                                        |
|----------|-------------------------------|----------------------------------------------------|
| Tool     | `generate_encrypted_pdf`      | Generates a PDF from input text and encrypts it    |
| Resource | `text://sample/weekly-summary`| Static weekly report text for LLM context          |
| Prompt   | `suggest_pdf_password`        | Generates strong password suggestions              |

---

## 💡 Example Use Cases

- Automatically generate encrypted reports with AI assistance
- Use with Claude Desktop or Cursor IDE
- Demonstrate secure agent-tool workflows in FastMCP

---

## 📜 License

MIT License • © Rajesh Polavarapu  
See [LICENSE](LICENSE) for details.
