import config
from base import bot
from telebot.types import ReplyKeyboardRemove


@bot.message_handler(commands=["help"], is_private_chat=True)
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        (
            f"{config.WELCOME_TEXT}"
            "\n"
            "The command list is in the next message.\n"
            "指令列表在下一条消息中。\n"
            "\n"
            "You can always use /cancel to interrupt current operation.\n"
            "你始终可以使用 /cancel 终止当前正在进行的操作。\n"
            "\n"
            f"If you need to peer with me, please go to the {config.CONTACT} channel and use the direct messaging feature to get in touch.\n"
            f"如需与我peer，请到 {config.CONTACT} 频道使用直通消息功能进行联系。\n"
            "\n"
            f"When something unexpected occurs, or the bot cannot meet your needs, please go to the channel {config.CONTACT} and use the direct messaging feature to get in touch.\n"
            f"当出现了什么意料之外的，或者机器人无法满足你的需求，请到频道 {config.CONTACT} 使用直通消息功能进行联系。\n"
            "\n"
            f"The administrator is {config.CONTACT_MASTER}. Unless necessary, please do not contact the administrator directly. Instead, go to the {config.CONTACT} channel and use the direct messaging feature to get in touch.\n"
            f"管理员为 {config.CONTACT_MASTER} 。非必要请不要直接联系管理员，请到频道 {config.CONTACT} 使用直通消息功能进行联系。"
        ),
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove(),
    )
    bot.send_message(
        message.chat.id,
        (
            "Command List 指令列表\n"
            "```Commands\n"
            "Tools:\n"
            "  - /ping [ip/domain]\n"
            "  - /tcping [ip/domain] {port}\n"
            "  - /trace [ip/domain]\n"
            "  - /route [ip/domain]\n"
            "  - /path [ip/domain]\n"
            "  - /whois [something]\n"
            "  - /dig [domain] {type}\n"
            "\n"
 #           "User Manage:\n"
 #           "  - /login\n"
 #           "    Login to verify your ASN\n"
 #           "    登录以验证你的 ASN\n"
 #           "  - /logout\n"
 #           "    Logout current logged ASN\n"
 #           "    退出当前登录的 ASN\n"
 #           "  - /whoami\n"
 #           "    Get current login user\n"
 #           "    获取当前登录用户\n"
 #           "\n"
 #           "Peer:\n"
 #           "  - /peer\n"
 #           "    Set up a peer\n"
 #           "    设置一个 Peer\n"
 #           "  - /modify\n"
 #           "    Modify peer information\n"
 #           "    修改 Peer 信息\n"
 #           "  - /remove\n"
 #           "    Remove a peer\n"
 #           "    移除一个 Peer\n"
 #           "  - /info\n"
 #           "    Show your peer info and status\n"
 #           "    查看你的 Peer 信息及状态\n"
 #           "  - /restart\n"
 #           "    Restart tunnel and Bird session\n"
 #           "    重启隧道及 Bird 会话\n"
 #           "\n"
            "Statistics:\n"
            "  - /rank\n"
            "    Show DN42 global ranking\n"
            "    显示 DN42 总体排名\n"
            "  - /stats [asn]\n"
            "    Show DN42 user basic info & statistics\n"
            "    显示 DN42 用户基本信息及数据\n"
            "  - /peer_list [asn]\n"
            "    Show the peer situation of a user\n"
            "    显示某 DN42 用户的 Peer 情况\n"
            "```"
        ),
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove(),
    )


@bot.message_handler(commands=["chatid"], is_private_chat=True)
def get_chatid(message):
    bot.send_message(
        message.chat.id,
        (
            f"Your chat ID is `{message.chat.id}`.\n"
            f"你的聊天 ID 是 `{message.chat.id}`。\n"
            "You can use this ID to report issues or for other purposes.\n"
            "你可以使用这个 ID 来报告问题或其他用途。"
        ),
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove(),
    )
