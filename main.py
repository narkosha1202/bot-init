import aiogram
import asyncio 
import os
import asyncio
import dotenv

dotenv.load_dotenv()

bot = aiogram.Bot(os.getenv("BOT_TOKEN"))
dp = aiogram.Dispatcher()


def on_start():
    print("Bot Ishladi...")


async def main():
    dp.startup.register(on_start)
    await dp.start_polling(bot)

asyncio.run(main())    