from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await Client.send_photo(
        chat_id=msg.chat.id,
        photo="https://telegra.ph/file/8220ee57eb0bfe0b6bc91.jpg",
        caption=f"""Hᴇʏ {msg.from_user.mention}🦋,

Tʜɪs ɪs {me2},
A  sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.🎈

Mᴀᴅᴇ ᴡɪᴛʜ ❤ ʙʏ : [ꜱᴛᴀʀʟᴇʏ](https://t.me/cv_official_channel) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ɢᴇɴ", callback_data="generate")
                ]
            ]
        ),
    )
