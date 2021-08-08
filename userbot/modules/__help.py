import logging

from userbot import BOT_USERNAME
from userbot.events import register

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@register(outgoing=True, pattern=r"^\.helpme")
async def yardim(event):
    try:
        tgbotusername = BOT_USERNAME
        if tgbotusername is not None:
            results = await event.client.inline_query(tgbotusername, "@Geez-Project")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        else:
            await event.edit(
                "`Botnya off gara-gara lu bego! atur Bot Token dan Username yang bener ngentod. Modul telah dihentikan.`"
            )
    except Exception:
        return await event.edit(
            "`Anda kurang ganteng sehingga tidak dapat mengirim hasil sebaris dalam obrolan ini (disebabkan oleh SendInlineBotResultRequest)`"
        )
