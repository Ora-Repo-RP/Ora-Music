# © @BabiesIQ

from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from .._logging import LOGGER

class Jany(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="Jani_Music",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            # resolve peer first so pyrogram caches it (avoids ValueError on fresh sessions)
            await self.get_chat(config.LOGGER_ID)
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
                parse_mode=ParseMode.HTML,
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid, ValueError):
            LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. "
                "Make sure the bot is added to the log group/channel and LOGGER_ID is correct."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}: {ex}"
            )
            exit()

        try:
            a = await self.get_chat_member(config.LOGGER_ID, self.id)
            if a.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error(
                    "Please promote your bot as an admin in your log group/channel."
                )
                exit()
        except Exception:
            pass  # some log groups allow non-admin bots
        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()