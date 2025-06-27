import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID", "28294093"))
API_HASH = getenv("API_HASH", "f24d982c45ab2f69a6cb8c0fee9630bd")
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "6815304449:AAHzee-0xh89yMtQb7hsQ6DUoySY92iOHDU")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","ll_KSD_ll")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "riya_musiczx_bot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "RIYA MUSIC")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "itz_m3_riya")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://parice819:fOJsdMBDj7xMKVFW@cluster0.str54m7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1002302799359))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 8142003954))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ifgovtjoftibcdjpvd8nfiokbfobffob0vrb8bd/RIYA-MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  

YTPROXY_URL = getenv("YTPROXY_URL", 'https://tgapi.xbitcode.com') ## E.G https://yt.okflix.
YT_API_KEY = "xbit_000000CUTE002"
COOKIES_URL=getenv("COOKIES_URL" , "https://gist.githubusercontent.com/sparrow9616/f29fc6588086a3c72d92dd9c03773350/raw/4229f3f4aab4a6693fc0794d136d30f54d67ae85/gistfile1.txt")


# ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RiyaUpdates")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+UyhfKoAkE8w3MDhl")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "1"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BQGvu80AKyEuV1bwNDMcFR91aUgP2NSezBWuY2QW6HZAS9Sgx-Tfo_nMu_PnxUChN5YPEbasD12obyqyK84COe3xLlDMUS9d7zUmITTsWf_ljE8ML4uVRZ8btJKx-CkXVc84nClTUNFqiDgQXt_yzu5HgJAUYmNJN55AnsGG8MpWTHRS3Ycs_hLBm8PF434ai6Zwu8oEwvhvZ_pB2kJIHxQMIK6nCRBMCVXExgJjirGZb8l_suCw_0s_iD3X4rHrDZC6A_eQACJTwsoYds-DXBLXWK0iWzOrmFTOWnD9aug4n8BdpGKtG3IRUIxutISozYRjaaSIKg3rWkNW5Omq4JpIa4zrggAAAAHG-LpkAA")
STRING2 = getenv("STRING_SESSION2",  None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/b61227af05544deb76a34.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/8kifut.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"
STATS_IMG_URL = "https://files.catbox.moe/8kifut.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2vq8oz.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2vq8oz.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
