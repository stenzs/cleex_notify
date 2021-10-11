from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
# import keyboards as kb
import config


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    r = requests.post('http://192.168.8.105:5000/write_tg_id', json={'number': message.from_user.id})
    print(r.json())
    await message.answer('Вы подписаны, ожидайте уведомлений')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
