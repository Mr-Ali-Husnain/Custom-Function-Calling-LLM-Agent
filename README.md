# Custom Function-Calling LLM Agent (Structured)

A highly modular and extensible **LLM Agent Framework** that supports *structured function calling*, automatic tool execution, and an infinite conversational loop.  
Built with a clean architecture, configurable environment variables, and support for Gemini’s API.

---

## 📌 Table of Contents

1. [Features](#-features)  
2. [Project Structure](#-project-structure)  
3. [Installation](#-installation)  
4. [Environment Setup](#-environment-setup)  
5. [Running the Application](#️-running-the-app)  
6. [Tool Function Architecture](#-tool-function-architecture)  
7. [API Key Security](#-api-key-security)  
8. [Requirements](#-requirements)  
9. [Contributing](#-contributing)  
10. [License](#-license)  

---

## 🚀 Features

- 🔧 **Structured Function Calling** — similar to OpenAI & Gemini tools  
- 🔁 **Continuous conversation loop** with memory-aware prompts  
- 🧩 **Plugin-style tool functions** (5+ ready-to-extend modules)  
- 🔐 **Secure API key loading via `.env`**  
- 📦 **Scalable project architecture**  
- ⚙️ **Easy integration with new tools and APIs**

---

## 📁 Project Structure

```
project/
│
├── app.py                      # Main application entry point
├── .env                        # Environment variables (NOT pushed to GitHub)
├── .gitignore                  # Ignore sensitive files
├── requirements.txt            # Package versions
│
├── tools/                      # Folder for custom tool functions
│   ├── tool_1.py
│   ├── tool_2.py
│   ├── tool_3.py
│   ├── tool_4.py
│   └── tool_5.py
│
└── README.md
```

---

## 🛠 Installation

### 1️⃣ Create and activate a virtual environment

#### Windows:
```
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file inside the project root:

```
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ **Never hard-code your API key into the codebase. Always use environment variables.**

---

## ▶️ Running the App

Start the LLM agent:

```
python app.py
```

The agent will begin an infinite interactive session and call tools automatically when needed.

---

## 🧪 Tool Function Architecture

Each tool function includes:

✔ A structured JSON schema  
✔ A callable Python function  
✔ A description for the LLM  
✔ Automatic binding for function calling  

Example tool structure:

```python
def add_numbers(a: int, b: int) -> int:
    return a + b

tool_schema = {
    "name": "add_numbers",
    "description": "Add two integers and return the result.",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "integer"},
            "b": {"type": "integer"}
        },
        "required": ["a", "b"]
    }
}
```

---

## 🔐 API Key Security

To protect sensitive credentials:

### ✔ Add `.env` to `.gitignore`  
```
.env
*.env
```

### ✔ Never commit `.env` files  
```
git rm --cached .env
git commit -m "Removed sensitive files"
```

### ✔ Rotate keys if leaked  
Delete old key → generate a new one.

---

## 📌 Requirements

All dependencies are included with **explicit version numbers** in:

```
requirements.txt
```

---

## 🤝 Contributing

PRs, issues, and feature suggestions are always welcome!  
Make sure to follow the project’s folder structure and coding style when adding tools.

---

## 📄 License

This project is licensed under the **MIT License**, allowing commercial and personal use.

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub!

Happy Coding! 🚀
