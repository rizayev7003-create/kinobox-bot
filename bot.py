import telebot
from telebot import types

TOKEN = "8811500907:AAGnSrD-1duRVksn0CugYtVwsdlqDXvHOVc"

bot = telebot.TeleBot(TOKEN)

# ====== KANAL ======
CHANNEL_USERNAME = "@kino_box_tv"

# ====== ASOSIY MENU ======
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = types.KeyboardButton("🔎 Kinoni qidirish")
btn2 = types.KeyboardButton("🔥 Trend kinolar")
btn3 = types.KeyboardButton("🎬 Janrlar")
btn4 = types.KeyboardButton("📸 Instagram")

menu.add(btn1, btn2)
menu.add(btn3, btn4)

# ====== START ======
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

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=menu
    )

# ====== KINO QIDIRISH ======
@bot.message_handler(func=lambda message: message.text == "🔎 Kinoni qidirish")
def search_movie(message):

    try:

        user_status = bot.get_chat_member(
            CHANNEL_USERNAME,
            message.from_user.id
        ).status

        if user_status in ["member", "administrator", "creator"]:

            bot.send_message(
                message.chat.id,
                "🎬 Kino kodini yuboring 👇"
            )

        else:

            markup = types.InlineKeyboardMarkup()

            btn = types.InlineKeyboardButton(
                "📢 Kanalga obuna bo‘lish",
                url="https://t.me/kanalingiz"
            )

            markup.add(btn)

            bot.send_message(
                message.chat.id,
                "❌ Botdan foydalanish uchun kanalga obuna bo‘ling!",
                reply_markup=markup
            )

    except:

        bot.send_message(
            message.chat.id,
            "❌ Botni kanalga admin qiling!"
        )

# ====== TREND ======
@bot.message_handler(func=lambda message: message.text == "🔥 Trend kinolar")
def trend_movies(message):

    bot.send_message(message.chat.id, """
🔥 Bugungi trend kinolar:

1. Squid Game
2. Fast X
3. Interstellar
4. Wednesday
""")

# ====== JANRLAR ======
@bot.message_handler(func=lambda message: message.text == "🎬 Janrlar")
def genres(message):

    genre_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("🎥 Marvel")
    btn2 = types.KeyboardButton("👻 Ujas")
    btn3 = types.KeyboardButton("🚀 Fantastika")
    btn4 = types.KeyboardButton("🔙 Orqaga")

    genre_menu.add(btn1, btn2)
    genre_menu.add(btn3)
    genre_menu.add(btn4)

    bot.send_message(
        message.chat.id,
        "🎬 Janr tanlang 👇",
        reply_markup=genre_menu
    )

# ====== ORQAGA ======
@bot.message_handler(func=lambda message: message.text == "🔙 Orqaga")
def back_menu(message):

    bot.send_message(
        message.chat.id,
        "🏠 Asosiy menu",
        reply_markup=menu
    )

# ====== INSTAGRAM ======
@bot.message_handler(func=lambda message: message.text == "📸 Instagram")
def instagram(message):

    bot.send_message(
        message.chat.id,
        "https://instagram.com/kino.box.tv"
    )

# ====== BOT ======
bot.infinity_polling()
