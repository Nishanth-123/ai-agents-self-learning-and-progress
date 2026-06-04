# Day 1 — Ollama Chat Interface

Part of [ai-agents-self-learning-and-progress](../README.md).

A simple interactive chat application using Ollama and Llama 3.2, demonstrating the fundamentals of working with local Large Language Models.

## What I Learned

- How to set up and use Ollama for local LLM inference
- Basic message structure and conversation flow
- Managing conversation history for context retention
- The role of system prompts in shaping AI behavior

## Concepts Covered

- **Ollama Integration**: Using the `ollama` Python library to interact with local models
- **Message Roles**: Understanding system, user, and assistant roles in conversations
- **Conversation State**: Maintaining message history across multiple turns
- **Model Selection**: Working with Llama 3.2 model

## Files and Purpose

- `app.py`: Main chat application with conversation loop
  - Initializes system prompt
  - Handles user input
  - Manages message history
  - Displays AI responses

## Key Learnings

1. **System Prompts Matter**: The system prompt sets the tone and behavior of the AI
2. **Context is Critical**: Maintaining conversation history enables coherent multi-turn conversations
3. **Local LLMs are Accessible**: Ollama makes running powerful models locally straightforward
4. **Message Structure**: Understanding the role-based message structure is fundamental to LLM APIs

## Run Instructions

### Prerequisites

- Python 3.8+
- Ollama installed and running
- Llama 3.2 model pulled: `ollama pull llama3.2`

### Installation

```bash
pip install ollama
```

### Running the Application

```bash
python app.py
```

### Usage

1. Start the application
2. Type your message when prompted
3. The AI will respond based on conversation context
4. Continue the conversation by typing more messages
5. Press Ctrl+C to exit

## Future Improvements

- Add streaming responses for better UX
- Implement conversation persistence (save/load)
- Add support for different models
- Include conversation history management commands
- Add error handling for API failures
- Implement rate limiting for production use

## Dependencies

- `ollama`: Python library for Ollama API

## Technical Notes

- Uses Llama 3.2 model by default
- Maintains unlimited conversation history in memory
- Simple while loop for continuous interaction
- No external API keys required (local model)
