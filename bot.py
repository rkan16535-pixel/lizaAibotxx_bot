import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

bot = Bot(TOKEN)
dp = Dispatcher()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🤖 AI-бот запущен!\n\n"
        "Напиши мне любой вопрос."
    )


@dp.message()
async def ai_chat(message: types.Message):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
