
import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to Sparta AI!\n"
        "Learn Python, C programming and trading.\n"
        "Use /help to see commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/python - Learn Python\n"
        "/c - Learn C programming\n"
        "/trading - Learn trading\n"
        "/about - About Sparta AI\n"
        "/chat - Chat mode\n"
        "/help - Show commands"
    )

async def python_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐍 Python lesson:\n"
        "name = input('Enter your name: ')\n"
        "print('Hello', name)\n\n"
        "This program asks for your name and prints a greeting."
    )

async def c_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '💻 C lesson:\n\n'
        '#include <stdio.h>\n'
        'int main(void) {\n'
        '    printf("Hello World!\\n");\n'
        '    return 0;\n'
        '}\n\n'
        "This program prints Hello World."
    )

async def trading_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 Trading education:\n"
        "Learn candlesticks, market trends, support and resistance, "
        "and risk management.\n\n"
        "Trading involves risk. This is educational content, "
        "not financial advice."
    )

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Sparta AI helps you learn Python, C programming, "
        "coding concepts and trading fundamentals."
    )

async def chat_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💬 Send a question about Python, C or trading. "
        "For intelligent AI answers, an AI model must be connected."
    )

async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I received your message. Try /python, /c, /trading or /help."
    )

def main():
    if not TOKEN:
        raise RuntimeError("Set TELEGRAM_BOT_TOKEN in your environment.")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("python", python_command))
    app.add_handler(CommandHandler("c", c_command))
    app.add_handler(CommandHandler("trading", trading_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("chat", chat_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_text))

    print("Sparta AI is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
