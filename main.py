import random
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Словник для визначення переможця
RULES = {
    "Камінь 🪨": "Ножиці ✂️",
    "Ножиці ✂️": "Папір 📄",
    "Папір 📄": "Камінь 🪨"
}

# Початкова команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Камінь 🪨", "Ножиці ✂️", "Папір 📄"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "Привіт! Давай зіграємо у 'Камінь, ножиці, папір'. Обирай свій варіант:",
        reply_markup=reply_markup
    )

# Логіка гри
async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_choice = update.message.text
    if user_choice not in RULES.keys():
        return

    bot_choice = random.choice(list(RULES.keys()))
    
    result = ""
    if user_choice == bot_choice:
        result = "🤝 Нічия!"
    elif RULES[user_choice] == bot_choice:
        result = "🎉 Ви перемогли!"
    else:
        result = "🤖 Бот переміг!"

    response = f"Ваш вибір: {user_choice}\nВибір бота: {bot_choice}\n\n{result}"
    await update.message.reply_text(response)

def main():
    # Вставте сюди свій токен, отриманий від BotFather
    TOKEN = "відьадєф093049039длфжукдл43ж12д34ьб4"

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, play))

    print("Бот запущений...")
    application.run_polling()

if __name__ == "__main__":
    main()
