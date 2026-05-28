import telebot
from telebot import types

TOKEN = "8811500907:AAGnSrD-1duRVksn0CugYtVwsdlqDXvHOVc"

bot = telebot.TeleBot(TOKEN)

# =========================
# KANALLAR
# =========================

CHANNELS = [
    "https://t.me/+4ItSLWyrtL81YzRi",
    "https://t.me/+65VNr7lvVmNiYTZi",
    "https://t.me/+0HJGGGlBuZxhMjMy"
]

# =========================
# KINO BAZA
# =========================

movies = {
    "101": "https://t.me/kanalingiz/5",
    "102": "https://t.me/kanalingiz/8",
    "103": "https://t.me/kanalingiz/12"
}

# =========================
# ASOSIY MENU
# =========================

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = types.KeyboardButton("🔎 Kino qidirish")
btn2 = types.KeyboardButton("🎬 Janrlar")
btn3 = types.KeyboardButton("🔥 Trend kinolar")
btn4 = types.KeyboardButton("📸 Instagram sahifamiz")

menu.add(btn1, btn2)
menu.add(btn3, btn4)

# =========================
# START
# =========================

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

# =========================
# OBUNA TEKSHIRISH
# =========================

def check_sub(user_id):

    for channel in CHANNELS:

        try:
            member = bot.get_chat_member(channel, user_id)

            if member.status not in ["member", "administrator", "creator"]:
                return False

        except:
            return False

    return True

# =========================
# KINO QIDIRISH
# =========================

@bot.message_handler(func=lambda message: message.text == "🔎 Kino qidirish")
def movie_search(message):

    if check_sub(message.from_user.id):

        msg = bot.send_message(
            message.chat.id,
            "🎬 Kino kodini yuboring 👇"
        )

        bot.register_next_step_handler(msg, get_movie)

    else:

        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True
        )

        btn1 = types.KeyboardButton("✅ Obuna bo‘ldim")
        btn2 = types.KeyboardButton("🔙 Orqaga")

        markup.add(btn1)
        markup.add(btn2)

        text = """
Kinoni qidirish uchun ushbu kanallarimizga obuna bo'lgan bo'lishingiz kerak 😊

🎬 Kanal 1 - https://t.me/+4ItSLWyrtL81YzRi
🎬 Kanal 2 - https://t.me/+65VNr7lvVmNiYTZi
🎬 Kanal 3 - https://t.me/+0HJGGGlBuZxhMjMy
"""

        bot.send_message(
            message.chat.id,
            text,
            reply_markup=markup
        )

# =========================
# OBUNA BO‘LDIM
# =========================

@bot.message_handler(func=lambda message: message.text == "✅ Obuna bo‘ldim")
def subscribed(message):

    if check_sub(message.from_user.id):

        msg = bot.send_message(
            message.chat.id,
            "🎬 Kino kodini yuboring 👇"
        )

        bot.register_next_step_handler(msg, get_movie)

    else:

        bot.send_message(
            message.chat.id,
            "❌ Siz hali barcha kanallarga obuna bo‘lmagansiz!"
        )

# =========================
# KINO CHIQARISH
# =========================

def get_movie(message):

    code = message.text

    if code in movies:

        bot.send_message(
            message.chat.id,
            f"🎬 Kino havolasi:\n\n{movies[code]}"
        )

    else:

        bot.send_message(
            message.chat.id,
            "❌ Bunday kino topilmadi!"
        )

# =========================
# JANRLAR
# =========================

@bot.message_handler(func=lambda message: message.text == "🎬 Janrlar")
def genres(message):

    genre_menu = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    btn1 = types.KeyboardButton("😍 Romantika")
    btn2 = types.KeyboardButton("😂 Komediya")
    btn3 = types.KeyboardButton("👻 Ujas")
    btn4 = types.KeyboardButton("🚀 Fantastika")
    btn5 = types.KeyboardButton("🇰🇷 Koreys drama")
    btn6 = types.KeyboardButton("🇹🇷 Turk serial")
    btn7 = types.KeyboardButton("🔙 Orqaga")

    genre_menu.add(btn1, btn2)
    genre_menu.add(btn3, btn4)
    genre_menu.add(btn5, btn6)
    genre_menu.add(btn7)

    bot.send_message(
        message.chat.id,
        "🎬 Janr tanlang 👇",
        reply_markup=genre_menu
    )

# =========================
# ORQAGA
# =========================

@bot.message_handler(func=lambda message: message.text == "🔙 Orqaga")
def back(message):

    bot.send_message(
        message.chat.id,
        "🏠 Asosiy menu",
        reply_markup=menu
    )

# =========================
# TREND KINOLAR
# =========================

@bot.message_handler(func=lambda message: message.text == "🔥 Trend kinolar")
def trend(message):

    bot.send_message(
        message.chat.id,
        """
🔥 Bugungi trend kinolar:

1. Squid Game
2. Fast X
3. Wednesday
4. Interstellar
"""
    )

# =========================
# INSTAGRAM
# =========================

@bot.message_handler(func=lambda message: message.text == "📸 Instagram sahifamiz")
def instagram(message):

    bot.send_message(
        message.chat.id,
        "https://instagram.com/kino.box.tv"
    )

# =========================
# BOTNI ISHGA TUSHIRISH
# =========================

print("Bot ishga tushdi...")

bot.infinity_polling()
