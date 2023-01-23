import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "17338150"))
    API_HASH = os.environ.get("API_HASH", "a855f783b521cbecef19e0e5dca232de")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5147058502:AAHWtjB0ZyuFOmXf_Ia9IPsaa1g4WaXsNNM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AQBnD_dUcxAnh2_FKAxkAe7I8e0BJKPZn4nDai_u3weo3EXugw5kwjd-75X6xtDvCwGL6_TILQXoJdFbi_vglOYtmzBmhsFT6Bhsdpoz55ns6Futp-3eXXs644VEHxoe0Sp9TheMAjaNxbx50Nq8mJJQ0X2AeB3jh2fYRjil3OJgEy2e6iTDbkUpW26jSk9ycP_NKoeqic3Nkh8JvKXJAkvBSNdKLguHvPTjdHBhJfSSgSyDhGriCQWbhaReaDmsjj5eA7oObOd0pWZ7-7-pyeNz_zLvGVp_XxrYDNaip0UsV7IVT15uaPGHRe7sUsZwf5d4x9whucxWm12_pmPBrnblAAAAATEeBl8A")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "v4sbot")
    SUPPORT = os.environ.get("SUPPORT", "jj8jjj8") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "cn_world") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://graph.org/file/a91e50ad6a08cc05c7ae7.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1160471152")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', False) # Change it to "True"
