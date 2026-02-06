# Conversational Knowledge Bot (LangChain + Tools + Memory)

## Problem Statement
Build a conversational knowledge bot that can remember previous conversations,
search external data, and provide contextual and factual answers.

## Objective
To demonstrate integration of LangChain agents, tools, and conversational memory.

## Architecture
- LLM: OpenAI Chat Model
- Agent: ZERO_SHOT_REACT_DESCRIPTION
- Memory: ConversationBufferMemory
- Tool: DuckDuckGo Web Search
- Interface: Command-line chat loop

## Features
- Context-aware conversation
- External web search for factual queries
- Memory-based follow-up questions
- Local CLI deployment

## How Memory Works
ConversationBufferMemory stores previous user and assistant messages.
This allows the bot to resolve follow-up references such as pronouns
and continue conversations contextually.

## Setup Instructions
```bash
pip install -r requirements.txt
python main.py
