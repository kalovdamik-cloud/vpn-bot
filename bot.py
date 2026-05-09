import telebot
from telebot import types
import os

TOKEN = os.getenv("8788569181:AAFBzgnke5IxamPA4qRPsKBbTlV1oq_MaGM")

bot = telebot.TeleBot(TOKEN)

users = {}

@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id
    username = message.from_user.username

    if user_id not in users:
        users[user_id] = {
            "balance": 0,
            "keys": 0
        }

    balance = users[user_id]["balance"]
    keys = users[user_id]["keys"]

    text = f"""
👤 Вы: <b>{user_id}</b>

💰 Ваш баланс: <b>{balance}₽</b>
🔐 Активных ключей: <b>{keys}</b>

<i>👇 Выберите действие:</i>
"""

    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton("🔐 Создать ключ", callback_data="create_key"))
    markup.add(types.InlineKeyboardButton("💰 Пополнить баланс", callback_data="balance"))
    markup.add(types.InlineKeyboardButton("👥 Пригласить других", callback_data="refs"))
    markup.add(types.InlineKeyboardButton("📞 Техподдержка", url="https://t.me/neptunevpn"))

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="HTML",
        reply_markup=markup
    )

print("Бот запущен")

bot.infinity_polling()
