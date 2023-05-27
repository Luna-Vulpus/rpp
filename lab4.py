# подключение к библиотекам
import os  # для получения переменных
import logging  # для инициализирования
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext  # машина состояний
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # хранение данных

# получение токена
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
# создание объекта и инициализация диспетчера, хранилища
bot = Bot(token=bot_token)

dp = Dispatcher(bot, storage=MemoryStorage())


# создание формы для работы с валютами
class Form(StatesGroup):
    name = State()
    rate = State()
    check = State()
    num = State()
    stop = State()


# словарь
currencies = {}


# обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_comand(message: types.Message):
    await message.reply("Привет! Здесь вы можете сделать перевод валюты. Для начала работы введите /start,для ввода "
                        "валюты /save_currency, для конвертации /convert.")


# обработчик команды /save_currancy, фиксирование переменной name для сохранения наименования валюты в name
@dp.message_handler(commands=['save_currency'])
async def save_comand(message: types.Message):
    await Form.name.set()
    await message.reply("Введите наименование валюты")


# обработчик команды /convert для конвертации и сохранения валюты
@dp.message_handler(commands=['convert'])
async def convert_comand(message: types.Message):
    await Form.check.set()
    await message.reply("Введите наименование валюты")


# обработчики сообщений для форм
@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.reply('Сколько рублей входит в один"' + message.text + '" ?')
    await Form.rate.set()


@dp.message_handler(state=Form.rate)
async def process_rate(message: types.Message, state: FSMContext):
    rate = message.text
    name = await state.get_data()
    name_currency = name['name']
    currencies[name_currency] = rate
    await state.finish()
    print(currencies)


@dp.message_handler(state=Form.check)
async def process_check(message: types.Message, state: FSMContext):
    await state.update_data(cheack_rate=message.text)
    await message.answer("Введите сумму для перевода в рубли")
    await Form.num.set()


@dp.message_handler(state=Form.num)
async def process_convert(message: types.Message, state: FSMContext):
    num = message.text
    cheack_rate = await state.get_data()
    name_currency = cheack_rate['cheack_rate']
    result = int(currencies[name_currency]) * int(num)
    await message.reply(result)
    await state.finish()


if __name__ == '__main__':  # точка входа в систему, подключение логирования, запуск обработки сообщений
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
