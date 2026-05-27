import telebot
from telebot import types

TOKEN = "8811500907:AAGnSrD-1duRVksn0CugYtVwsdlqDXvHOVc"

bot = telebot.TeleBot(TOKEN)

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = types.KeyboardButton("🔎 Kinoni qidirish")
btn2 = types.KeyboardButton("🔥 Trend kinolar")
btn3 = types.KeyboardButton("🎬 Janrlar")
btn4 = types.KeyboardButton("📸 Instagram")

menu.add(btn1, btn2)
menu.add(btn3, btn4)

@bot.message_handler(commands=['start'])
def start(message):
    text = """
🎬 Botimizga xush kelibsiz!

Bu yerda siz:
🔎 Istalgan kinoni qidirishingiz
🎬 Janrlar bo‘yicha kinolar topishingiz
🔥 Trend kinolarni tomosha qilishingiz mumkin

Pastdagi tugmalardan foydalaning 👇
"""
    bot.send_message(message.chat.id, text, reply_markup=menu)

@bot.message_handler(func=lambda message: message.text == "🔎 Kinoni qidirish")
def search_movie(message):
    bot.send_message(message.chat.id, "🎬 Kino kodini yuboring 👇")

@bot.message_handler(func=lambda message: message.text == "🔥 Trend kinolar")
def trend_movies(message):
    bot.send_message(message.chat.id, """
🔥 Bugungi trend kinolar:

1. Squid Game
2. Fast X
3. Interstellar
4. Wednesday
""")

@bot.message_handler(func=lambda message: message.text == "🎬 Janrlar")
def genres(message):
    bot.send_message(message.chat.id, """
🎬 Janrlar:

😍 Romantika
😂 Komediya
👻 Ujas
🚀 Fantastika
🇰🇷 Koreys drama
🇹🇷 Turk serial
""")

@bot.message_handler(func=lambda message: message.text == "📸 Instagram")
def instagram(message):
    bot.send_message(message.chat.id, "https://instagram.com/kino.box.tv")

bot.infinity_polling()
