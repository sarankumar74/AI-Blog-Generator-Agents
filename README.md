# 🤖 AI Blog Generator Agent Application
🔍 *Generative AI • AI Agents • LangChain • Gemini API • SERPER API • Streamlit*

## 🚀 Tech Stack & Domains
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![LangChain](https://img.shields.io/badge/Framework-LangChain-purple)
![Gemini](https://img.shields.io/badge/LLM-Gemini%20API-brightgreen)
![AI Agents](https://img.shields.io/badge/AI-Agents-orange)
![SERPER](https://img.shields.io/badge/Search-SERPER%20API-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)
![Domain](https://img.shields.io/badge/Domain-Generative%20AI%20%26%20Agent%20Automation-navy)

---

## 📘 Overview
This project is a **full-stack AI Blog Generator Agent Application** that automates blog research and content creation.

The application uses **AI agents, Gemini API, LangChain, SERPER API, tool calling, agent communication, task execution, and prompt engineering** to transform a user's blog topic into researched and structured content.

The final generated blog can also be provided as a **PDF report**.

---

## 🎯 Problem Statement
Writing a high-quality blog manually requires significant time for:

- Topic research
- Collecting relevant information
- Organizing content
- Writing and structuring the blog
- Preparing the final document

This project automates these tasks using AI agents, reducing the amount of manual research and writing required.

---

## 🎯 Project Objective
The objective is to build an AI-powered blog generation workflow where specialized AI tasks work together to:

- Understand the user's requested blog topic
- Research information from the web
- Process and organize the research
- Generate the blog content
- Produce a final structured report
- Export the generated content as a PDF

---

## 💼 Business Use Cases

| Use Case | Description |
|---------|-------------|
| ✍️ Content Creation | Automate blog research and first-draft generation |
| 📢 Digital Marketing | Generate content for marketing and online publishing |
| 📰 Research & Publishing | Reduce manual research and content preparation time |

---

## 🧠 AI Agent Architecture

### 🔎 Research Agent
- Receives the user's requested blog topic
- Uses SERPER API for web search
- Collects relevant information
- Organizes research information for the writing task

### ✍️ Writing Agent
- Receives the research information
- Uses Gemini API for content generation
- Follows system prompts and task instructions
- Generates structured blog content

### 🤝 Agent Communication
- Research task communicates relevant information to the writing task
- Tasks are executed in a defined workflow
- Final content is passed to the reporting stage

---

## 🗺️ Project Workflow

### 📝 1 — User Input
User enters the desired blog topic or content requirements through the Streamlit UI.

### 🔎 2 — AI Research
The research agent performs web searches using the **SERPER API** and collects relevant information.

### 🤖 3 — AI Writing
The writing agent processes the research information and generates the blog using the **Gemini API**.

### 📊 4 — Final Report
The generated content is organized into a structured final report.

### 📄 5 — PDF Generation
The final report is generated in **PDF format** for sharing and storage.

---

## 🛠️ Core Technologies

- **Python**
- **LangChain**
- **Gemini API**
- **SERPER API**
- **AI Agents**
- **Agent Tool Calling**
- **Agent Communication**
- **Task Implementation**
- **Prompt Engineering**
- **System Prompt Engineering**
- **Streamlit**

---


<summary>📸 Click to view Streamlit UI screenshots</summary>

#### Result Page  
![Home Page](https://github.com/user-attachments/assets/a1bc6ae6-bbe6-4387-8ae4-fc06bb1c2a41)


---

## 📁 Project Structure

```text
crewai/
│
├── __pycache__/
├── .venv/
├── .env
│
├── agents.py
├── app.py
├── convert_pdf.py
├── crew.py
├── main.py
├── task.py
├── tools.py
│
├── news_blog_post.md
├── news_blog_post.pdf
│
├── requirements.txt
└── README.md
```
---


## 🛠️ Installation & Execution

Clone Repository
```
git clone https://github.com/sarankumar74/AI-Blog-Generator-Agents.git

```

## Install Dependencies
```

pip install -r requirements.txt
```

## Configure API Keys

Create a .env file:
```
GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key
```

## 📤 Output

The application provides:

🔎 Research information
✍️ AI-generated blog content
📊 Structured final report
📄 PDF report

## 🔒 Notes

1. Built using an AI agent-based workflow
2. Uses Gemini API for AI-powered content generation
3. Uses SERPER API for web research
4. Uses LangChain for agent and tool integration
5. Streamlit provides the application UI
6. Final content can be exported as a PDF report

   
This is the **same visual README style** as the screenshot you shared and the other GitHub READMEs we've been creating.

