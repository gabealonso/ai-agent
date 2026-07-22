# AI Agent with Wikipedia and Tavily Search

A conversational AI agent built with **LangChain + LangGraph** that intelligently
searches using both Wikipedia and Tavily, keeping per-conversation memory
throughout the chat session.

## 🚀 Features

- **Dual search**: the agent picks between Wikipedia and Tavily per query
- **Wikipedia**: detailed, factual info about people, places, history, concepts
- **Tavily**: current info — weather, news, and real-time data
- **Conversational memory**: a LangGraph checkpointer keeps each conversation's
  history, keyed by a `thread_id`
- **Model-agnostic**: uses `init_chat_model` (OpenAI by default; other providers
  work with their package + key)
- **Simple chat interface**: talk to it like a person

## 🧠 Tool selection

The LLM chooses the tool based on the query and each tool's description:

- **📚 Wikipedia** — biographies, historical events, scientific definitions,
  geography. *e.g. "Who was Albert Einstein?", "What is quantum physics?"*
- **🌐 Tavily** — current weather, breaking news, recent/live data.
  *e.g. "What's the weather in Buenos Aires?", "Latest news about AI"*

## 📋 Requirements

- Python 3.9+
- **Tavily API key** (required — the search tool)
- **OpenAI API key** (required for the default model `openai:gpt-4o-mini`)

## 🛠️ Installation

1. **Clone and enter the repo:**
   ```bash
   git clone <repository-url>
   cd ai-agent
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env             # then edit .env with your API keys
   ```

## 🎯 Usage

### Interactive chat
```bash
python main.py
```

Type `new` to start a fresh conversation, `quit` to exit.

### Tests
```bash
pip install -r requirements-dev.txt
pytest
```

## 💬 Example conversation

```
You: Hi, my name is Gabe and I'm 28 years old.
Agent: Hi Gabe! Nice to meet you. I'll remember that you're 28 years old.

You: What's my name?
Agent: Your name is Gabe! You introduced yourself at the beginning of our conversation.

You: What's the weather in Buenos Aires?
Agent: Let me search for current weather information in Buenos Aires...

You: Who was Albert Einstein?
Agent: Albert Einstein was a German-born theoretical physicist who developed the theory of relativity...
```

## 🏗️ How it works

### Architecture
- **LangGraph ReAct agent** (`create_react_agent`) — reasons and calls tools.
- **`init_chat_model`** — provider-agnostic model loading.
- **Wikipedia tool** — detailed, factual information.
- **Tavily tool** — current, real-time information.

### Memory
Memory is handled by a LangGraph **checkpointer** (`MemorySaver`). Each
conversation has a `thread_id`; the agent recalls that thread's history on every
turn, so it remembers what you told it. Typing `new` starts a fresh `thread_id`
(and therefore an empty conversation). Memory lives in-process for the session.

## 🔧 Configuration

`config.py` is the single source of truth for the agent's behavior — model,
search sizes, and the system prompt:

```python
DEFAULT_MODEL = "openai:gpt-4o-mini"
TAVILY_MAX_RESULTS = 5
WIKIPEDIA_MAX_RESULTS = 3
SYSTEM_PROMPT = "..."
```

### Environment variables (`.env`)
```env
TAVILY_API_KEY=your-tavily-api-key      # required
OPENAI_API_KEY=your-openai-api-key      # required for the default model
```

### Using a different model
Change `DEFAULT_MODEL` in `config.py`. Non-OpenAI providers need their package
and API key — uncomment the relevant line in `requirements.txt` and set the key:

```python
DEFAULT_MODEL = "anthropic:claude-sonnet-5"   # needs langchain-anthropic + ANTHROPIC_API_KEY
DEFAULT_MODEL = "google:gemini-1.5-pro"       # needs langchain-google-genai + GOOGLE_API_KEY
```

## 📁 Project structure

```
ai-agent/
├── agents/
│   └── ai_agent.py          # Builds the LangGraph agent (tools + memory)
├── tools/
│   ├── tavily_tool.py       # Tavily search tool
│   └── wikipedia_tool.py    # Wikipedia search tool
├── tests/                   # pytest suite (config, tools, agent)
├── main.py                  # Interactive chat app
├── config.py                # Configuration (model, search, prompt)
├── requirements.txt         # Runtime dependencies
├── requirements-dev.txt     # Test dependencies
├── .env.example             # Environment template
└── README.md
```

## 🔍 Troubleshooting

1. **"Missing required environment variables"** — copy `.env.example` to `.env`
   and fill in `TAVILY_API_KEY` and `OPENAI_API_KEY`.
2. **"No module named 'langchain_tavily'"** — run `pip install -r requirements.txt`.
3. **Agent not remembering** — memory is per `thread_id`; typing `new` starts a
   fresh conversation. History is kept in-process for the current session.

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch
3. Make your changes (and add tests)
4. Run `pytest`
5. Open a pull request

## 📄 License

MIT — see the LICENSE file.
