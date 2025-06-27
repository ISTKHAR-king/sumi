import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", "28294093"))

API_HASH = getenv("API_HASH", "f24d982c45ab2f69a6cb8c0fee9630bd")

BOT_TOKEN = getenv("BOT_TOKEN", "6815304449:AAHzee-0xh89yMtQb7hsQ6DUoySY92iOHDU")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://parice819:fOJsdMBDj7xMKVFW@cluster0.str54m7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", -1002302799359))

OWNER_ID = int(getenv("OWNER_ID", "8142003954"))

BOT_USERNAME = getenv("BOT_USERNAME" , "Riya_musiczx_bot")

COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Sonkarxkoushal/rzx",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "SPY")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RIYAUPDATES")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Riya_Chat_support")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", False)
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

YTPROXY_URL = getenv("YTPROXY_URL", 'https://tgapi.xbitcode.com') ## E.G https://yt.okflix.
YT_API_KEY = "xbit_000000CUTE002"
COOKIES_URL=getenv("COOKIES_URL" , "https://gist.githubusercontent.com/sparrow9616/f29fc6588086a3c72d92dd9c03773350/raw/4229f3f4aab4a6693fc0794d136d30f54d67ae85/gistfile1.txt")



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 21474836480))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 21474836480))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGvu80AKyEuV1bwNDMcFR91aUgP2NSezBWuY2QW6HZAS9Sgx-Tfo_nMu_PnxUChN5YPEbasD12obyqyK84COe3xLlDMUS9d7zUmITTsWf_ljE8ML4uVRZ8btJKx-CkXVc84nClTUNFqiDgQXt_yzu5HgJAUYmNJN55AnsGG8MpWTHRS3Ycs_hLBm8PF434ai6Zwu8oEwvhvZ_pB2kJIHxQMIK6nCRBMCVXExgJjirGZb8l_suCw_0s_iD3X4rHrDZC6A_eQACJTwsoYds-DXBLXWK0iWzOrmFTOWnD9aug4n8BdpGKtG3IRUIxutISozYRjaaSIKg3rWkNW5Omq4JpIa4zrggAAAAHG-LpkAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/n4vivz.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/8kifut.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"
STATS_IMG_URL = "https://files.catbox.moe/8kifut.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2vq8oz.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2vq8oz.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/53f1a295e172d39eaa39d.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

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
