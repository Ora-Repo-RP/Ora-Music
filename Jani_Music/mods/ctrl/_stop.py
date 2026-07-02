# © @BabiesIQ

from pyrogram import filters
from pyrogram.types import Message

from Jani_Music import app
from Jani_Music.engine._vclient import Jany
from Jani_Music.helpers._store import set_loop
from Jani_Music.helpers.wrap import AdminRightsCheck
from Jani_Music.helpers.kb import close_markup
from config import BANNED_USERS

@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Jany.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )