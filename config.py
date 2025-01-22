from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "26992956"
# -------------------------------------------------------------
API_HASH = "9ba740b3c2b946c837e95852a780b7f8"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "6656608288"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/yourtoofan/CHATBOT")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
SUPPORT_GRP = "kaalCarder"
UPDATE_CHNL = "SweetToxicUpdate"
OWNER_USERNAME = "WerewolfDemonInfo"
# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", "")
    
