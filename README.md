<div align="center">

<!-- HEADER BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=220&section=header&text=GenAI%20Learning%20Journey&fontSize=52&fontColor=ffffff&fontAlignY=38&desc=LangChain%20%7C%20LangGraph%20%7C%20Agents%20%7C%20RAG&descAlignY=60&descSize=20&animation=fadeIn" width="100%"/>

<br/>

<!-- BADGES -->
![Status](https://img.shields.io/badge/Status-Actively%20Learning-brightgreen?style=for-the-badge&logo=statuspage&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-🦜-1C3C3C?style=for-the-badge)
![LangGraph](https://img.shields.io/badge/LangGraph-🕸️-FF6B35?style=for-the-badge)
![GenAI](https://img.shields.io/badge/GenAI-✨-8B5CF6?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)

<br/><br/>

> *"The best way to understand AI is to build with it."*

<br/>

</div>

---

## 🧠 What Is This?

This repository is my **personal learning lab** for Generative AI — built from the ground up, concept by concept. I'm exploring the full stack of modern LLM application development:

- 🦜 **LangChain** — chains, prompts, memory, tools, and retrieval
- 🕸️ **LangGraph** — stateful multi-agent workflows and graph-based orchestration
- 🤖 **Agents** — autonomous reasoning loops with tool use
- 📚 **RAG** — Retrieval-Augmented Generation pipelines
- 🔗 **LLM APIs** — OpenAI, Anthropic Claude, and more

---

## 📁 Repository Structure

```
📦 genai-learning/
├── 📂 langchain/
│   ├── 01_basics/              # Chains, prompts, output parsers
│   ├── 02_memory/              # ConversationBuffer, Summary memory
│   ├── 03_retrieval/           # RAG, vector stores, embeddings
│   └── 04_agents/              # ReAct agents, tools, toolkits
│
├── 📂 langgraph/
│   ├── 01_graphs/              # StateGraph, nodes, edges
│   ├── 02_multi_agent/         # Supervisor, worker agents
│   └── 03_advanced/            # Conditional edges, memory, checkpoints
│
├── 📂 projects/
│   ├── rag_chatbot/            # Document Q&A system
│   ├── research_agent/         # Web-browsing research agent
│   └── workflow_automator/     # Multi-agent task runner
│
├── 📂 notebooks/               # Jupyter notebooks for experiments
├── 📂 notes/                   # Concept summaries and cheatsheets
└── requirements.txt
```

---

## 🗺️ Learning Roadmap

```
Phase 1: Foundations            Phase 2: LangChain              Phase 3: LangGraph
─────────────────────           ─────────────────────           ─────────────────────
 ✅ LLM APIs & Prompting         ✅ Chains & LCEL                🔄 StateGraph Basics
 ✅ Embeddings & Vector DBs      ✅ Memory Modules                🔄 Multi-Agent Systems
 ✅ Tokenization basics          🔄 RAG Pipelines                ⬜ Human-in-the-Loop
                                 🔄 Tool Use & Agents            ⬜ LangGraph Cloud

✅ Done   🔄 In Progress   ⬜ Upcoming
```

---

## 📚 Learning Resources

<table>
<thead>
<tr>
<th>Source</th>
<th>Type</th>
<th>What I Use It For</th>
<th>Link</th>
</tr>
</thead>
<tbody>

<tr>
<td>
  <img src="https://img.shields.io/badge/Claude-Anthropic-D97706?style=flat-square&logo=anthropic&logoColor=white" />
</td>
<td>🤖 AI Assistant</td>
<td>Deep concept explanations, debugging, code walkthroughs, design patterns, and instant Q&A for any confusion that comes up</td>
<td><a href="https://claude.ai">claude.ai</a></td>
</tr>

<tr>
<td>
  <img src="https://img.shields.io/badge/ChatGPT-OpenAI-10A37F?style=flat-square&logo=openai&logoColor=white" />
</td>
<td>🤖 AI Assistant</td>
<td>Exploring OpenAI's own APIs, code generation, quick prototyping, and cross-checking explanations from a different model perspective</td>
<td><a href="https://chat.openai.com">chat.openai.com</a></td>
</tr>

<tr>
<td>
  <img src="https://img.shields.io/badge/CampusX-YouTube-FF0000?style=flat-square&logo=youtube&logoColor=white" />
</td>
<td>🎥 YouTube Channel</td>
<td>Structured, in-depth Hindi video tutorials covering GenAI, LangChain, LangGraph, and ML fundamentals — my primary video resource</td>
<td><a href="https://www.youtube.com/@campusx-official">@campusx-official</a></td>
</tr>

<tr>
<td>
  <img src="https://img.shields.io/badge/LangChain-Docs-1C3C3C?style=flat-square" />
</td>
<td>📖 Official Docs</td>
<td>API references, cookbooks, integration guides, and best practices straight from the source</td>
<td><a href="https://python.langchain.com/docs">python.langchain.com</a></td>
</tr>

<tr>
<td>
  <img src="https://img.shields.io/badge/LangGraph-Docs-FF6B35?style=flat-square" />
</td>
<td>📖 Official Docs</td>
<td>Graph concepts, agent architectures, and LangGraph-specific patterns</td>
<td><a href="https://langchain-ai.github.io/langgraph">langgraph docs</a></td>
</tr>

</tbody>
</table>

---

## ⚡ Key Concepts Covered

<details>
<summary><b>🦜 LangChain</b></summary>

<br/>

| Concept | Description |
|---|---|
| **LCEL** | LangChain Expression Language — composing chains with `\|` operator |
| **PromptTemplates** | Dynamic, reusable prompt construction |
| **Memory** | ConversationBuffer, Summary, Entity, and Vector memory |
| **Retrieval** | Document loaders, text splitters, vector stores, retrievers |
| **Agents** | ReAct loop, tool binding, AgentExecutor |
| **Tools** | Custom tools, Tavily search, Python REPL, and more |

</details>

<details>
<summary><b>🕸️ LangGraph</b></summary>

<br/>

| Concept | Description |
|---|---|
| **StateGraph** | Defining graph state with TypedDict schemas |
| **Nodes** | Python functions as graph nodes |
| **Edges** | Static and conditional edges for routing |
| **Checkpointers** | Persistent state across sessions |
| **Human-in-the-loop** | Interrupt nodes for human approval |
| **Multi-Agent** | Supervisor pattern, handoffs, and sub-graphs |

</details>

<details>
<summary><b>🔧 Tools & Tech Stack</b></summary>

<br/>

```python
# Core Stack
langchain>=0.3.0
langgraph>=0.2.0
langchain-openai
langchain-anthropic
langchain-community

# Vector Stores
chromadb
faiss-cpu
pinecone-client

# Utilities
python-dotenv
jupyter
streamlit          # For demo UIs
```

</details>

---

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/genai-learning.git
cd genai-learning

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Add your OPENAI_API_KEY, ANTHROPIC_API_KEY, etc.

# 5. Launch Jupyter for notebooks
jupyter notebook notebooks/
```

---

## 💡 Favourite Insight So Far

> LangGraph changed how I think about agents. Instead of a linear chain of calls,
> you model the problem as a **graph** — where each node is a decision or action,
> and edges define what happens next. It's AI logic that actually *looks* like logic.

---

## 📈 Progress Log

| Week | Focus | Status |
|------|-------|--------|
| Week 1 | LLM APIs, Prompt Engineering basics | ✅ Complete |
| Week 2 | LangChain LCEL, Chains, OutputParsers | ✅ Complete |
| Week 3 | Memory & Conversation Management | ✅ Complete |
| Week 4 | RAG — Embeddings, Vector DBs, Retrievers | 🔄 In Progress |
| Week 5 | LangChain Agents & Tool Use | ⬜ Upcoming |
| Week 6 | LangGraph — StateGraph & Basic Agents | ⬜ Upcoming |
| Week 7 | Multi-Agent Systems with LangGraph | ⬜ Upcoming |

---

<div align="center">

**Built with curiosity, caffeine, and a lot of `pip install`s ☕**

<br/>

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=genai-learning-journey)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer" width="100%"/>

</div>
