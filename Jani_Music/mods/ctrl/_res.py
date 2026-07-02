# © @BabiesIQ

from pyrogram import filters
from pyrogram.types import Message

from Jani_Music import app
from Jani_Music.engine._vclient import Jany
from Jani_Music.helpers._store import is_music_playing, music_on
from Jani_Music.helpers.wrap import AdminRightsCheck
from Jani_Music.helpers.kb import close_markup
from config import BANNED_USERS

@app.on_message(filters.command(["resume", "cresume"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await Jany.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), reply_markup=close_markup(_)
    )