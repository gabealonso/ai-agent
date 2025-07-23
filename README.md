# AI Agent with Wikipedia and Tavily Search

A conversational AI agent built with LangChain that intelligently searches using both Wikipedia and Tavily, maintaining conversational memory throughout the chat session.

## 🚀 Features

- **Dual Search System**: Intelligently chooses between Wikipedia and Tavily based on query type
- **Wikipedia Search**: For detailed, factual information about people, places, historical events, and concepts
- **Tavily Search**: For current information, weather, news, and real-time data
- **Conversational Memory**: Maintains context and remembers user information throughout the chat
- **Multiple Models**: Support for OpenAI, Anthropic, Google, and other models
- **Natural Chat Interface**: Simple conversation format like chatting with a person
- **Smart Tool Selection**: Automatically selects the most appropriate search tool for each query

## 🧠 Intelligent Tool Selection

The agent automatically decides which search tool to use:

### 📚 Wikipedia Tool
- **Best for**: Biographies, historical events, scientific definitions, geographical information
- **Examples**: "Who was Albert Einstein?", "What is quantum physics?", "Tell me about the Roman Empire"

### 🌐 Tavily Tool  
- **Best for**: Current weather, breaking news, recent events, live information
- **Examples**: "What's the weather in Buenos Aires?", "Latest news about AI", "Current stock prices"

## 📋 Requirements

- Python 3.9+
- Tavily API key (required)
- OpenAI API key (optional but recommended)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ai-agent
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv ai-agent
   source ai-agent/bin/activate  # On Windows: ai-agent\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Copy `env.example` to `.env` and add your API keys:
   ```bash
   cp env.example .env
   # Edit .env file with your API keys
   ```

## 🎯 Usage

### Interactive Chat
```bash
python main.py
```

### Testing
```bash
python test_agent.py
```

## 💬 Example Conversations

```
You: Hi, my name is Gabe and I'm 28 years old.
Agent: Hi Gabe! Nice to meet you. I'll remember that you're 28 years old.

You: What's my name?
Agent: Your name is Gabe! You introduced yourself at the beginning of our conversation.

You: What's the weather in Buenos Aires?
Agent: Let me search for current weather information in Buenos Aires...

You: Who was Albert Einstein?
Agent: Albert Einstein was a German-born theoretical physicist who developed the theory of relativity...

You: What's my age again?
Agent: You're 28 years old, Gabe! You told me that when we first started chatting.
```

## 🏗️ How It Works

### Core Architecture
- **LangChain**: Core framework for building LLM applications
- **OpenAI Functions Agent**: Uses function calling for tool selection
- **ConversationBufferMemory**: Maintains chat history and context
- **Wikipedia Tool**: For detailed, factual information
- **Tavily Tool**: For current, real-time information

### Memory System
The agent uses `ConversationBufferMemory` to maintain the entire conversation history. This allows it to:
- Remember user information (name, age, location, preferences)
- Maintain context across multiple messages
- Provide personalized responses based on previous interactions

### Tool Selection Logic
The agent automatically chooses between Wikipedia and Tavily based on the query content:
- **Wikipedia**: For historical facts, biographies, definitions, educational content
- **Tavily**: For current events, weather, news, real-time information

## 🔧 Configuration

### Environment Variables
Create a `.env` file with your API keys:

```env
# Required
TAVILY_API_KEY=your-tavily-api-key-here

# Optional (for better performance)
OPENAI_API_KEY=your-openai-api-key-here
```

### Model Selection
You can change the language model in `agents/ai_agent.py`:

```python
# OpenAI models
agent_executor, memory = create_agent("openai:gpt-4o-mini")
agent_executor, memory = create_agent("openai:gpt-4o")

# Anthropic models
agent_executor, memory = create_agent("anthropic:claude-3-5-sonnet-20241022")

# Google models
agent_executor, memory = create_agent("google:gemini-1.5-flash")
```

### Search Configuration
Modify search parameters in the tool files:

**Tavily** (`tools/tavily_tool.py`):
```python
tavily_tool = create_tavily_tool(max_results=5)  # Number of search results
```

**Wikipedia** (`tools/wikipedia_tool.py`):
```python
wikipedia_tool = create_wikipedia_tool(max_results=3)  # Number of articles
```

## 📁 Project Structure

```
ai-agent/
├── agents/
│   └── ai_agent.py          # Agent configuration with dual tools
├── tools/
│   ├── tavily_tool.py       # Tavily search tool
│   └── wikipedia_tool.py    # Wikipedia search tool
├── main.py                  # Main chat application
├── test_agent.py           # Test suite
├── config.py               # Configuration management
├── requirements.txt        # Dependencies
├── env.example             # Environment template
└── README.md              # This file
```

## 🔍 Troubleshooting

### Common Issues

1. **"TAVILY_API_KEY environment variable is required"**
   - Solution: Add your Tavily API key to the `.env` file
   - Get your free API key from [Tavily](https://tavily.com/)

2. **"No module named 'langchain_tavily'"**
   - Solution: Run `pip install langchain-tavily`

3. **Agent not remembering information**
   - Make sure you're using the same conversation session
   - Type 'new' to start a fresh conversation if needed
   - The agent remembers information within a single session

4. **Agent not responding**
   - Check your internet connection
   - Verify your API keys are valid
   - Try different search terms

### Tool Selection Tips

- **For historical/factual queries**: The agent will use Wikipedia
- **For current/real-time queries**: The agent will use Tavily
- **For personal questions**: The agent will respond from memory

### Memory Management

- **Session Memory**: Information is remembered throughout the chat session
- **New Conversation**: Type 'new' to start fresh and clear memory
- **Exit**: Type 'quit' to exit the application

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up API keys**


3. **Start chatting:**
   ```bash
   python main.py
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
