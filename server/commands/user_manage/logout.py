import pickle
import config
import tools
from base import bot, db, db_privilege
from telebot.types import ReplyKeyboardRemove


@bot.message_handler(commands=["logout"], is_private_chat=True)
def start_logout(message):
    bot.send_message(
        message.chat.id,
        (
        "This command has been disabled.\n该指令已被禁用。\n",
        f"If you need to peer with me, please go to the {config.CONTACT} channel and use the direct messaging feature to get in touch.\n"
        f"如需与我peer，请到 {config.CONTACT} 频道使用直通消息功能进行联系。"
        ),
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove(),
    )
    return
    if message.chat.id not in db:
        tools.gen_login_message(message)
        return
    text = (
        f"You have logged out as `{tools.get_asn_mnt_text(db[message.chat.id])}`.\n"
        f"你已经退出 `{tools.get_asn_mnt_text(db[message.chat.id])}` 身份。"
    )
    db.pop(message.chat.id)
    if message.chat.id in db_privilege:
        db_privilege.remove(message.chat.id)
        text = "*[Privilege]*\n" + text
    with open("./user_db.pkl", "wb") as f:
        pickle.dump((db, db_privilege), f)
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=ReplyKeyboardRemove())
