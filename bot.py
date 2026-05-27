from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8811500907:AAGnSrD-1duRVksn0CugYtVwsdlqDXvHOVc"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

menu = ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = KeyboardButton("🔎 Kinoni qidirish")
btn2 = KeyboardButton("🔥 Trend kinolar")
btn3 = KeyboardButton("🎬 Janrlar")
btn4 = KeyboardButton("📸 Instagram")

menu.add(btn1, btn2)
menu.add(btn3, btn4)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = """
🎬 Botimizga xush kelibsiz!

Bu yerda siz:
🔎 Istalgan kinoni qidirishingiz
🎬 Janrlar bo‘yicha kinolar topishingiz
🔥 Trend kinolarni tomosha qilishingiz mumkin

Pastdagi tugmalardan foydalaning 👇
"""
    await message.answer(text, reply_markup=menu)

@dp.message_handler(lambda message: message.text == "🔎 Kinoni qidirish")
async def search_movie(message: types.Message):
    await message.answer("🎬 Kino kodini yuboring 👇")

@dp.message_handler(lambda message: message.text == "🔥 Trend kinolar")
async def trend_movies(message: types.Message):
    await message.answer("""
🔥 Bugungi trend kinolar:

1. Squid Game
2. Fast X
3. Interstellar
4. Wednesday
""")

@dp.message_handler(lambda message: message.text == "🎬 Janrlar")
async def genres(message: types.Message):
    await message.answer("""
🎬 Janrlar:

😍 Romantika
😂 Komediya
👻 Ujas
🚀 Fantastika
🇰🇷 Koreys drama
🇹🇷 Turk serial
""")

@dp.message_handler(lambda message: message.text == "📸 Instagram")
async def instagram(message: types.Message):
    await message.answer("https://instagram.com/kino.box.tv")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)