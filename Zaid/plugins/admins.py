from telethon import events, Button
from Zaid import Zaid
from Zaid.status import *
from Config import Config
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@Zaid.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])

@Zaid.on(events.callbackquery.CallbackQuery(data="play"))
async def _(event):

    await event.edit(PLAY_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])


ADMIN_TEXT = """
**✘ اوامر الادمنية التي يمكنهم استخدامها!**

‣ `?end` - لإنهاء التشغيل.
‣ `?skip` - لتخطي الاغنية وتشغيل التي تليها.
‣ `?pause` - لإيقاف التشغيل مؤقتا.
‣ `?resume` - لإستكمال التشغيل.
‣ `?leavevc` - لمغادرة البوت من المجموعة.
‣ `?playlist` - لتشغيل بلاي لست المجموعة.
"""

PLAY_TEXT = """
**✘ الاوامر المتاحة للأعضاء!**

‣ `?play` - لتشغيل اغنية بالرد على ملف صوتي او كتابة اسم الاغنية.
‣ `?vplay` -  لتشغيل فيديو (لايعمل حاليا).
"""
