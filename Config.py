import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "17338150"))
    API_HASH = os.environ.get("API_HASH", "a855f783b521cbecef19e0e5dca232de")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5147058502:AAHWtjB0ZyuFOmXf_Ia9IPsaa1g4WaXsNNM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzYBu4MXAEuLyH-Ci8bW6sh1kwK33ozEZ6fdWeD06Hle2BqhuvnMAfM-yGd6BFmnd2GvzvIXhsPu2OYUUdsdGZ-63saIap46nWHOaQRWDr7v-HlLF6JKLb7TNk17ZCpT7LNmGg1QvsP4IPf1VcIdZLd2X_o7wpGDhw0PVG5eiyKn_tVb6hJck7LpfoC4nxujL-yMB8w1DUyB3NtrkvMNcGEFpFu2acN0JX4qxLunIwXW-KwOqfPaGXLH2tnU6A-Kw4l1-sDJ3_qul0GsfiecLfljmgMed7pu8TNxlUzB8n-qirjfek9zGGQc6wEN28xneL9OQuhpJ5lomgiwJQcm_qZU8Y4=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "v4sbot")
    SUPPORT = os.environ.get("SUPPORT", "jj8jjj8") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "cn_world") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://graph.org/file/a91e50ad6a08cc05c7ae7.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1160471152")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
