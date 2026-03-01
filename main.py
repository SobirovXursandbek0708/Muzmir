import os
from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer(
        "👋 Salom!\n"
        "NavoMir bot ishlayapti ✅"
    )

@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(
        f"📝 Siz yozdingiz:\n{message.text}"
    )

if __name__ == "__main__":
    executor.start_polling(dp)
