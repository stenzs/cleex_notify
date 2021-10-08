from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
# import keyboards as kb
import config
from database import Users


DELAY = 1800

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if Users.get_or_none(number=message.from_user.id) is None:
        Users.create(number=message.from_user.id)
    await message.answer('Вы подписаны')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)