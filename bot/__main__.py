import asyncio

from aiogram import Bot, Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from bot.config_reader import config
from bot.db.base import sessionmaker
from bot.handlers import callbacks, commands
from bot.middlewares import DbSessionMiddleware
from bot.ui_commands import set_ui_commands


async def main():
    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")

    # Setup dispatcher and bind routers to it
    dp = Dispatcher()
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))
    # Automatically reply to all callbacks
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    # Register handlers
    dp.include_router(commands.router)
    dp.include_router(callbacks.router)

    # Set bot commands in UI
    await set_ui_commands(bot)

    # Run bot
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
