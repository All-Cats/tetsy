from g4f.client import Client
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


def g4f_question(qt:str) -> str:
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"{qt}"}],
    )
    return response.choices[0].message.content


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = '8152673025:AAHK2TNUuyKmHrNxj4fQiyWu2lJbr3svn84'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()т

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )

@dp.message()
async def ask_command(message: Message):
    question = message.text  #Получаем текст после команды /ask
    if question:
        answer = g4f_question(question)
        await message.reply(answer)
    else:
        await message.reply("Пожалуйста, задайте вопрос после команды /ask.")

if __name__ == '__main__':
    dp.run_polling(bot)
