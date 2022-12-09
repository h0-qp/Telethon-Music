from telethon import events, Button
from Zaid import Zaid, BOT_USERNAME
from Config import Config


btn =[
    [Button.inline("اوامر الادمن", data="admin"), Button.inline("اوامر التشغيل", data="play")],
    [Button.inline("الصفحة الرئيسية", data="start")]]

HELP_TEXT = "اهلا بك في قائمة الاوامر\n\nاختر من الازرار!"


@Zaid.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_group:
       await event.reply("ارسل لي /help في الخاص لعرض قائمة الاوامر!", buttons=[
       [Button.url("ارسال /help!","t.me/v4sbot?start=help")]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@Zaid.on(events.NewMessage(pattern="[!?/]الاوامر"))
async def help(event):
    await event.reply("""
✘ اوامر الادمنية التي يمكنهم استخدامها!

‣ `?end` - لإنهاء التشغيل.
‣ `?skip` - لتخطي الاغنية وتشغيل التي تليها.
‣ `?pause` - لإيقاف التشغيل مؤقتا.
‣ `?resume` - لإستكمال التشغيل.
‣ `?leavevc` - لمغادرة البوت من المجموعة.
‣ `?playlist` - لتشغيل بلاي لست المجموعة.

✘ الاوامر المتاحة للأعضاء!

‣ `?play` - لتشغيل اغنية بالرد على ملف صوتي او كتابة اسم الاغنية.
‣ `?vplay` -  لتشغيل فيديو (لايعمل حاليا).

اوامر الانضمام:

`?join`- مع رابط المجموعة او يوزرها

`?pjoin`- اذا كانت محموعتك خاصة ارسل هذا الامر مع الرابط

***ملاحظة مهمة: سمكن استخدام ! او / او ? في بداية الامر***.""")

@Zaid.on(events.NewMessage(pattern="^/start help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.reply(HELP_TEXT, buttons=btn)

@Zaid.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.edit(HELP_TEXT, buttons=btn)
