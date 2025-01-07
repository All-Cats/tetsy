from g4f.client import Client
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os

load_dotenv()

# Создаем объекты бота и диспетчера

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()


def g4f_question(qt:str) -> str:
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"{qt}"}],
    )
    return response.choices[0].message.content


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет! Это бесплатный аналог GPT-чата! \nВыберите 1 из команд: \n /start - главное меню \n /help - помощь по боту \n /ask - чат с ботом')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Здравствуйте по любым вопросом вы можете связаться с разработчиком @SemyonWeb!'
    )

@dp.message(Command(commands=['ask']))
async def ask_command(message: Message):
    question = message.text  #Получаем текст после команды /ask
    # await message.reply("Ваш запрос обробатывается.")
    if question:
        answer = g4f_question(question)
        await message.reply(answer)
    else:
        await message.reply("Пожалуйста, задайте вопрос после команды /ask.")

if __name__ == '__main__':
    dp.run_polling(bot)
