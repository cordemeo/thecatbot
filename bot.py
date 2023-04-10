print("a file")
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

API_TOKEN: str = 'your token here'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет\nНапиши мне что-нибудь')

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer("Привет! хочешь узнать кто ты из кошачьего сквада сегодня? Напиши help. facts - узнать факты о кошках.")

@dp.message(Command(commands=['facts']))
async def process_help_command(message: Message):
    await message.answer("Такое животное, как кошка очень настойчива. Она способна мяукать без перерыва несколько часов.В случае опасности, кошка способна бежать со скорость 48 км/ч.Почки кошки способны фильтровать соль. Благодаря такой особенности, животное способно пить морскую воду.Котенок способен видеть сон уже через одну неделю после рождения.Нос кошки уникален, так как имеет неповторимый отпечаток.Гормон роста у котенка вырабатывается только во сне.")


#@dp.message()
#async def send_echo(message: Message):
    #await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)