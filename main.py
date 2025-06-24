import os
import asyncio
import dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from yt_dlp import YoutubeDL

dotenv.load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def download_video(url: str) -> str:
    os.makedirs("videos", exist_ok=True)  
    ydl_opts = {
        'outtmpl': 'videos/%(title)s.%(ext)s',
        'format': 'mp4',
        'quiet': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

@dp.message()   
async def handle_video(message: Message):
    url = message.text.strip()

    if "youtube.com" in url or "youtu.be" in url or "instagram.com" in url:
        await message.reply("📥 Yuklab olinmoqda, biroz kuting...")
        try:
            path = download_video(url)
            video = FSInputFile(path)
            await bot.send_video(message.chat.id, video)
            os.remove(path) 
        except Exception as e:
            await message.reply(f"❌ Yuklab bo‘lmadi:\n{e}")
    else:
        await message.reply("🔗 Iltimos, YouTube yoki Instagram havolasini yuboring.")

async def on_startup():
    print("✅ Bot ishga tushdi!")

async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
