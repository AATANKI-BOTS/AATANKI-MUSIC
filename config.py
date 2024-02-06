import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 30000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @KunoXrobot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6483333350))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AATANKI-BOTS/AATANKI-MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "patch-1")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+-2grMhOKoww5Nzg1")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+aih6DZ8qerdlMWU9")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 204857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
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


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/4b11c10cf7c7bdf1b5fe5.jpg)"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/47605a2381cd25cc8b050.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/c9d675e3693c169215ca5.jpg"
STATS_IMG_URL = "https://graph.org/file/77785bfc6eceb77dd5edd.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/b79ee36deb5e8302825da.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/ecfc9e0d3360e58d36700.jpg"
STREAM_IMG_URL = "https://graph.org/file/a054899caa2700893a3d6.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/fd2cd43c1b3e188f2bbec.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/77785bfc6eceb77dd5edd.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/77785bfc6eceb77dd5edd.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/b5f7e7a637ac7e32daf71.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/65afd7d5aabebf2e1a067.jpg"



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:360"))


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
