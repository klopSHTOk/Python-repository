from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.storage import FSMContext

import const # мой модуль с приватной информацией
import script # мой модуль с необходимым кодом

bot = Bot(const.BOT_TOKEN)
memory = MemoryStorage()
dp = Dispatcher(bot, storage=memory)

class Form(StatesGroup): 
    reading = State()

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Приветствую, пользователь!')
    await message.answer('При помощи команды <b>/read</b> вы можете начать работу с ботом.', parse_mode=types.ParseMode.HTML)

@dp.message_handler(commands=('read', 'r'), commands_prefix='!/')
async def save_data(message: types.Message):
    await bot.send_message(message.chat.id, 'Введите нужную информацию:')
    await Form.reading.set()

@dp.message_handler(state=Form.reading)
async def reader(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        proxy['read'] = message.text
        const.DATA.append(proxy['read'])
        await state.finish()
        await message.reply('Подождите...🕘')

        script.exact_process()
        await bot.send_message(message.chat.id, '✅ Озвученный текст отправлен!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
