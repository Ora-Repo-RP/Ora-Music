# © @BabiesIQ

from pyrogram import filters
from pyrogram.types import Message

from Jani_Music import app
from Jani_Music.engine._vclient import Jany

welcome = 20
close = 30

@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Jany.stop_stream_force(message.chat.id)