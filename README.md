# Therapy Bot

A Telegram-based therapy chatbot powered by LLaMA 2, designed to provide conversational support and helpful responses to users. This bot offers a friendly interface for users seeking guidance or a listening ear.

## Prerequisites

- Python 3.7 or higher
- A Telegram account
- A bot token from [BotFather](https://t.me/botfather)
- LLaMA 2 model access and API setup

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/YOUR-USERNAME/therapy-bot.git
   cd therapy-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the root directory with the following variables:
   ```
   TELEGRAM_TOKEN=your_telegram_bot_token
   LLAMA_API_KEY=your_llama_api_key
   ```

2. Customize the bot's initial prompt and personality in `bot.py` if desired.

3. Adjust conversation memory settings in `main.py` to modify how much context the bot retains.

## Available Commands

The bot responds to the following commands:

- `/start` - Initiates the conversation and provides a welcome message
- `/help` - Displays available commands and usage information
- `/reset` - Resets the conversation history
- `/about` - Displays information about the bot
- `/feedback` - Allows users to submit feedback
- `/settings` - Allows users to adjust their conversation preferences

## Features

### Therapy Conversations
The bot utilizes LLaMA 2's advanced natural language processing capabilities to provide thoughtful responses to users' messages. It can offer emotional support, reflective listening, and general guidance.

### Conversation Memory
The bot maintains a conversation history to provide contextual responses, making interactions feel more natural and continuous.

### Personality Customization
The system uses a carefully crafted prompt to ensure responses are empathetic, understanding, and helpful while maintaining appropriate boundaries.

### Easter Eggs
The bot includes hidden features and fun responses that can be discovered through certain message triggers or command patterns.

### Privacy Focus
Conversation data is handled with privacy in mind, with options for users to reset their conversation history at any time.

## Usage Examples

Starting a conversation:
```
User: /start
Bot: Hello! I'm your therapy bot assistant. How are you feeling today?
```

Having a therapeutic conversation:
```
User: I've been feeling really stressed lately
Bot: I understand how challenging stress can be. Could you tell me more about what's been causing these feelings?
```

Resetting the conversation:
```
User: /reset
Bot: I've cleared our conversation history. Let's start fresh. How can I help you today?
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the developers of LLaMA 2 for providing the AI model capabilities
- The Telegram Bot API for making bot creation accessible

## This is an AI bot which uses llama and has been fine tuned using predefined prompts and prompt memory storage to make this an effective therapy bot. Some other commands has been included to make it more fun.
this is currently just a telegram bot.