import os

from pyrogram import Client
from pyrogram import idle


from app.libs.logs import logger
from app.config import setting


os.environ["TZ"] = "Asia/Shanghai"

user: Client = None
bot: Client = None
if setting["proxy"]["enable"]:
    logger.info("proxy start")
    proxy = {
        "scheme": "http",
        "hostname": setting["proxy"]["ip"],
        "port": setting["proxy"]["port"],
        "username": setting["proxy"]["username"],
        "password": setting["proxy"]["password"],
    }
else:
    proxy = None


async def start_app():

    global user, bot
    user = Client(
        "sessions/user",
        api_id=setting["tg"]["api_id"],
        api_hash=setting["tg"]["api_hash"],
        proxy=proxy,
        plugins=dict(root="app.user_scripts"),
    )
    bot = Client(
        "sessions/bot",
        api_id=setting["tg"]["api_id"],
        api_hash=setting["tg"]["api_hash"],
        bot_token=setting["tg"]["bot_token"],
        proxy=proxy,
    )
    logger.info("启动主程序")
    await user.start()
    logger.info("监听主程序")
    await bot.start()
    logger.info("监听机器人")
    await idle()
    await user.stop()
    await bot.stop()
    logger.info("关闭主程序")


def get_bot():
    global bot
    return bot
