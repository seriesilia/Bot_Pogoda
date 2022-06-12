from aiogram import types, executor, Dispatcher, Bot


bot = Bot(token='1207505213:AAF7OIYoL4tJ8nQjgZKYZJu9WRbDOWQRLec')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)