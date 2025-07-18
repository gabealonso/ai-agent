# AI Agent with Wikipedia and Web Search

A conversational AI agent that can search for information using Wikipedia and DuckDuckGo web search. The agent maintains conversation memory and can remember user information across interactions.

## Features

- **Conversational Memory**: Remembers user information and conversation context
- **Wikipedia Search**: Access to factual, encyclopedia-style information
- **Web Search**: Real-time information, weather, news, and current events
- **Smart Tool Selection**: Automatically chooses the most appropriate search tool
- **Interactive Chat Interface**: Clean console-based chat experience

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

## Usage

Run the agent:
```bash
python main.py
```

### Example Interactions

```
You: Hi, my name is Gabe
AI: Hi Gabe! How can I assist you today?

You: What is my name?
AI: Your name is Gabe.

You: What is the weather in New York?
AI: Web: [Current weather information]

You: Tell me about cats
AI: Wikipedia: [Information about cats]
```

## Project Structure

```
ai-agent/
├── main.py                 # Main application entry point
├── agents/
│   └── ai_agent.py        # Agent configuration and setup
├── tools/
│   ├── wikipedia_tool.py  # Wikipedia search tool
│   └── duckduckgo_tool.py # Web search tool
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Architecture

- **Agent**: Uses LangGraph with GPT-4o-mini model
- **Tools**: Wikipedia and DuckDuckGo search integration
- **Memory**: Simple conversation memory system
- **Interface**: Console-based chat with thread management

## Configuration

- **Model**: GPT-4o-mini (configurable in `agents/ai_agent.py`)
- **Temperature**: 0 (deterministic responses)
- **Memory**: Thread-based conversation memory
- **Tools**: Wikipedia and DuckDuckGo with smart selection

## License

MIT License - see LICENSE file for details. 