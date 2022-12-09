
import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Zaid import *
from Zaid.status import *



@Zaid.on(events.NewMessage(pattern="^[!?/]join ?(.*)"))
@Zaid.on(events.NewMessage(pattern="^[!?/]userbotjoin ?(.*)"))
@is_admin
async def _(e, perm):
    chat_id = e.chat_id
    usage = "اوامر الانضمام\n\nالاوامر:\n\n/join <رابط المجموعة / يوزر المجموعة> اذا كانت مجموعتك خاصة ارسل هذا الامر !pjoin <رابط المجموعة>"
    if e.is_group:
        umm = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = umm[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("تم الانضمام بنجاح إذا لم ينضم الحساب المساعد فأرسل !pjoin ورابط مجموعتك")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@Zaid.on(events.NewMessage(pattern="^[!?/]pjoin ?(.*)"))
@is_admin        
async def _(e, perm):
    chat_id = e.chat_id
    usage = "اوامر الانضمام الخاص:\n\nالامر:\n\n!pjoin <وايدي رابط مجموعتك>\n\nمثال :\nالرابط = https://t.me/joinchat/Ihsvig1907226#\n\n!pjoin Ihsvig1907226"
    if e.is_group:
        umm = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            invitelink = umm[0]
            text = "جار الانضمام..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await client(ImportChatInviteRequest(invitelink))
                await event.edit("تم بنجاح ✅️")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
    
