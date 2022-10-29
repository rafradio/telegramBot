import asyncio
import logging
from aiogram import Bot, Dispatcher, types
import sqlBot

pasword = input("Введите mysql пароль: ")
sqlObg = sqlBot.FormToMSQLQuery(pasword)
sqlQuery = "SELECT * FROM database3.bot_commands;"
sqlObg.MySQLCommands(sqlQuery)
commandsSQL = list(sqlObg.commands)

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="")
# Диспетчер
dp = Dispatcher(bot)

# Хэндлер на команду /start
@dp.message_handler(commands=["start", 'Hello'])
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message_handler(commands=["Name", 'name'])
async def cmd_name(message: types.Message):
    x = await sum(6, 8, 7)
    y = message["text"]
    print(y)
    
    await message.answer(x)
    await message.answer("My name is Bot!")

# handler для команд

@dp.message_handler(commands = commandsSQL)
async def cmd_sqlBD(message: types.Message):
    textTelega = message["text"][1:]
    answer = await findAnswer(textTelega)
    await message.answer(answer)

async def findAnswer(textTelega):
    sqlQuery = "SELECT * FROM database3.bot_commands WHERE database3.bot_commands.name = '" + str(textTelega) + "';"
    sqlObg.MySQLFindAnswer(sqlQuery)
    return sqlObg.answer

# handler для простого общения бота

@dp.message_handler()
async def just_talk(message: types.Message):
    textTelega = message["text"]
    answer = await findAnswer(textTelega)
    await message.answer(answer)

async def sum(*args):
    sum = 0
    for arg in args: sum +=arg
    return sum

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    # pasword = input("Введите mysql пароль: ")
    # sqlObg = sqlBot.FormToMSQLQuery(pasword)
    # sqlQuery = "SELECT * FROM database3.bot_commands;"
    # sqlObg.MySQLCommands(sqlQuery)
    # commandsSQL = list(sqlObg.commands)
    # print(sqlObg.commands)
    asyncio.run(main())
