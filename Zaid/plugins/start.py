from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
مرحبا بك يا {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **انا بوت بوت بسيط لمكالكات المجموعات**.
‣ **يمكنني تشغيل الاغاني في مجموعتك**.
‣ **أمتلك جميع مقومات بوتات الاغاني فلا تحتاج لهم**
‣ **هذا البوت مطور من قبل @jj8jjj8 زسيتوقف في أي لحظة**!
‣ **لدي بعض الاوامر الاخرى أكتشفها**.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **اختر ماتريد من الازرار ادناه 🔘 للمزيد من المعلومات ℹ️**.
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", "https://github.com/dyler2/Telethon-Music")],
        [Button.url("🗣️ ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ! ɪ'ᴍ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ ✅**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", "https://github.com/dyler2/Telethon-Music")],
        [Button.url("🗣️ ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return
