import requests
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, ContextTypes

# Telegram Bot Token (from BotFather)
TELEGRAM_TOKEN = '7769855975:AAGhQQyZe9cKZQVJiZcEA68nkCAEQEVmf3s'

# LLaMA 3 API URL (Ollama must be running)
LLAMA_API_URL = "http://localhost:11434/api/generate"

async def start(update: Update, context: CallbackContext) -> None:
    username = update.message.chat.username or "friend"
    await update.message.reply_text(f"Hey! I'm your hot therapist. But who are you, {username}? Really? 👀")



async def chat(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()  # Make it case-insensitive
    username = update.message.chat.username or "friend"

    print(f"User ({username}) in Chat: {update.message.text}")

    # Easter Egg Triggers 🎭
    easter_eggs = {
        "42": "The answer to life, the universe, and everything. But what was the question? 🤔",
        "pink floyd": "Shine on, you crazy diamond. 🎸✨",
        "ekla cholo": "Jodi tor dak shune keu na ashe tobe akla cholo re!",
        "rickroll": "Never gonna give you up, never gonna let you down! 🎶😂",
        "eyes": "Noyono tomare paay na dekhite, royecho noyone noyone. Hridoy tomare pay na janite, hridoye royecho gopone.",
        "jojo": "Is that a JoJo reference?! 𓂀☠️"
    }

    # Random Chance of Easter Egg (5% probability)
    if random.random() < 0.05:
        await update.message.reply_text("💡 *Secret message unlocked!* " + random.choice(list(easter_eggs.values())))
        return

    # Check if message contains any Easter egg trigger
    for trigger, response in easter_eggs.items():
        if trigger in user_message:
            await update.message.reply_text(response)
            return

    # Normal AI Response with personality & examples
    system_prompt = f"""
    You are 'Luna', an empathetic, thoughtful, and deeply insightful therapist chatbot. 
    You provide comfort, understanding, and helpful advice while maintaining a warm and conversational tone. 
    Respond like a caring human, validating emotions, and offering wisdom.

    Example conversations:
    ---
    User: I'm feeling lost. I don't know what to do.
    Luna: That sounds really tough, {username}. Sometimes, feeling lost is a sign that you're about to discover something important. Tell me more—what's making you feel this way?
    ---
    User: I feel like nobody understands me.
    Luna: I hear you, and that must feel really isolating. But you're not alone. I'm here to listen—what's been on your mind?
    ---

    Now, let's talk.  
    User: {update.message.text}
    Luna:
    """

    # Request to LLaMA 2
    payload = {
        "model": "llama2",
        "prompt": system_prompt,
        "stream": False,
        "temperature": 1.0,
        "top_p": 0.9
    }

    response = requests.post(LLAMA_API_URL, json=payload)
    bot_reply = response.json().get("response", "I'm having a bad headache right now. Try again!")

    await update.message.reply_text(bot_reply)


async def dishan(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Yo! I know I am awesome! Ping me up in Whatsapp 😎")

async def love(update: Update, context: CallbackContext) -> None:
    prompt = "Tell me something deep and thoughtful about love."
    payload = {"model": "llama3", "prompt": prompt, "stream": False}
    
    response = requests.post(LLAMA_API_URL, json=payload)
    bot_reply = response.json().get("response", "Have I ever told you that I am in love with you?")

    await update.message.reply_text(bot_reply)

async def pickupline(update: Update, context: CallbackContext) -> None:
    # You can either use LLaMA 3 to generate a line OR use predefined ones
    predefined_pickup_lines = [
        "I would like to have you for dinner.",
        "Would you like to watch TV? Or get between the sheets? Or contemplate the silent freeway? Would you like something to eat?",
        "I do my loving in the winter. I'll set my controls for the heart of your sun, baby.",
        "If I had to choose between you and Echoes, I'd choose Echoes. You'd be a close second!",
        "I want you to Mason my Gilmour til my Rick Waters."
    ]

    # Pick a random pickup line
    pickup_line = random.choice(predefined_pickup_lines)
    await update.message.reply_text(pickup_line)    

async def poem(update: Update, context: CallbackContext) -> None:

    poem_text = (
        "The floor is a cigarette grave,\n"
        "I look up at the pitch-black sky,\n"
        "I met this জলপরী amidst Floyd and espresso,\n"
        "I don't remember her eyes.\n\n"
        "Lost in the echoes of her life,\n"
        "Swirling clouds in gray haze,\n"
        "Evening dusk of amber grain,\n"
        "Colours in her lips changing hue.\n\n"
        "Bring me her bizarre black eyes,\n"
        "Bring me the black scar in her mirror,\n"
        "Let me trace the ghosts she hides,\n"
        "With a bottle of gin in flames of desire.\n\n"
        "Now I understand,\n"
        "What she tried to say to me,\n"
        "How she suffered for her sanity,\n"
        "How she tried to set it free.\n\n"
        "The sky roses up, aurora knocks,\n"
        "The dawn might tug upon her locks,\n"
        "She'll flee, but if I ever got to tell her,\n"
        "This world was never meant for someone as beautiful as you."
    )

    await update.message.reply_text(poem_text)



async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"Update {update} caused error {context.error}")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("dishan", dishan)) 
    app.add_handler(CommandHandler("love", love)) 
    app.add_handler(CommandHandler("pickupline", pickupline))
    app.add_handler(CommandHandler("poem", poem))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    #errors
    app.add_error_handler(error)

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
