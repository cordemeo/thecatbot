import random
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import FSInputFile, InputMediaPhoto

API_TOKEN: str = 'your token'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЭтот бот может поднимать настроение путем отправки картинок с кошкой. А еще рассказывает факты о кошках.\n Напиши /help, чтобы увидеть список команд.')

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer("Вот список команд:\n/facts - узнать факты о кошках.\n/mf - рандомное милое фото с Фелей\n/cf - рандомное смешное фото с Фелей")

@dp.message(Command(commands=['mf']))
async def process_photo_command(message: Message, bot: Bot):

    photo = FSInputFile(r'D:/downloads/142cce5a-2065-46c9-8cee-f7deb78a5282.jpg')
    photo1 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/cutefelyaphotos/2f12677b-8bcc-425c-8fad-61c4e5f4e7b5.jpg')
    photo2 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/cutefelyaphotos/27baf7f8-27c3-4081-9e13-e0dd8f538ac1.jpg')
    photo3 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/cutefelyaphotos/30d1fb51-ea58-4488-bc31-8a9c94574a80.jpg')
    photo4 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/cutefelyaphotos/50ef3bba-5f36-4c9c-b3f7-d1c78c776d04.jpg')
    photo5 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/cutefelyaphotos/ac0de466-3e89-466d-9f00-db1b43b5214d.jpg')
    photo6 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/cutefelyaphotos/df6973ba-0b9b-444b-a945-13bfcfef8cdb.jpg')
    photo7 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/cutefelyaphotos/f2128480-4377-495b-9c47-8556150a18b7.jpg')
    arr = [photo,photo1,photo2,photo3,photo4,photo5,photo6,photo7]
    await bot.send_photo(message.chat.id, random.choice(arr))

@dp.message(Command(commands=['cf']))
async def process_photo1_command(message: Message, bot: Bot):

    f1 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/funnyfelyaphotos/0ac5a5b1-7dc7-49ea-bc56-57db482afe92.jpg')
    f2 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/funnyfelyaphotos/12a273d3-b151-462d-beca-aa599ea0f923.jpg')
    f3 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/funnyfelyaphotos/36a8ee5e-dc1a-4a83-9d63-f06f859b2432.jpg')
    f4 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/funnyfelyaphotos/342a3333-56f2-45b8-af55-41bf38951abb.jpg')
    f5 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/funnyfelyaphotos/a8ad3e2e-29b3-4023-85d6-0fef0d8e3626.jpg')
    f6 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/funnyfelyaphotos/a17ba417-224d-48a4-8db9-71b3f89370e4.jpg')
    f7 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/funnyfelyaphotos/c01edf71-0c56-4d51-a724-56cbd2aa6f8c.jpg')
    f8 = FSInputFile(r'C:/Users/Huawei/OneDrive/Изображения/funnyfelyaphotos/e9cf232b-5338-42cd-bd81-eb8b0f8f5230.jpg')
    arr1 = [f1, f2, f3, f4, f5, f6, f7, f8]
    await bot.send_photo(message.chat.id, random.choice(arr1))

@dp.message(Command(commands=['facts']))
async def process_facts_command(message: Message):
    await message.answer("1️⃣\nТакое животное, как кошка очень настойчива. Она способна мяукать без перерыва несколько часов. \n2️⃣\nВ случае опасности, кошка способна бежать со скоростью 48 км/ч.\n3️⃣\nПочки кошки способны фильтровать соль. Благодаря такой особенности, животное способно пить морскую воду.\n4️⃣\nКотенок способен видеть сон уже через одну неделю после рождения.\n5️⃣\nНос кошки уникален, так как имеет неповторимый отпечаток.\n6️⃣\nГормон роста у котенка вырабатывается только во сне.")



if __name__ == '__main__':
    dp.run_polling(bot)
