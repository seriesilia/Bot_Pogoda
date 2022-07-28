from aiogram import types, executor, Dispatcher, Bot
import python_weather
import config

bot = Bot(config.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL, locale='ru-RU')


@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.find(message.text)
    celsius = round((weather.current.temperature - 32) / 1.8)

    resp_msg = weather.location_name + "\n"
    resp_msg += f"текущая температура: {celsius}°\n"
    resp_msg += f"состояние погоды: {weather.current.sky_text}"
    await message.answer(resp_msg)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
