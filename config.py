import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", "24081339"))

API_HASH = getenv("API_HASH", "52ef4637744116982ed28210da47a5bd")

BOT_TOKEN = getenv("BOT_TOKEN", "6815304449:AAESc6FsFkmOG2PNUd1r7_XBTklS5Ab6I50")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://parice819:fOJsdMBDj7xMKVFW@cluster0.str54m7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", -1002551836060))

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
YT_API_KEY = "xbit_0000743191821303754064"
COOKIES_URL=getenv("COOKIES_URL" , "https://gist.githubusercontent.com/sparrow9616/f29fc6588086a3c72d92dd9c03773350/raw/4229f3f4aab4a6693fc0794d136d30f54d67ae85/gistfile1.txt")



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 21474836480))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 21474836480))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFvc7sAJdx1UZtOCxVt9z13QOU6HEMPhbUMi_PJy5zb9XLMG0ghogqBJlVGyeKuBKvhncDCZiaV-HIghBz3m_BYbJF9rDiIrUX0hZaSuw5TpwDjTPt5AVOAPRYFMtxT7pzHLcFHaQsPp8chAx58s4zjB9Zjrmq3mj8MFvg2ETMahzZIEQ2gx1qn4iE2CwB4tFl6HQQ1sJHOajzD_yAmGtv56p9l177pO63FFLWcp2znjJwQcYLuRuIw8LE0hY4zftwYgLv891sGuKS3myh416hd1llDJ0fD3GN3VaCX3m0bR-v6xELasTwWdF0qkPrIMwjBCLkkTF2Eqi5qgfTzvWeZRBodZgAAAAGYbGLMAA")
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
