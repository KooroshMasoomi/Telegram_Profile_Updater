from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from pyrogram import Client
from random import choice
from pytz import timezone

API_ID = int
API_HASH = str

app = Client(
    name="Client",
    api_id=API_ID,
    api_hash=API_HASH,
)

emojis = [
    "\U0001f600",
    "\U0001f603",
    "\U0001f604",
    "\U0001f601",
    "\U0001f642",
    "\U0001f643",
    "\U0001f609",
    "\U0001f60a",
    "\U0001fae0",
    "\U0001f920",
    "\U0001f60f",
]


def update_profile():
    time = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")
    text = f"Your last visit to my bio was {time} {choice(emojis)}"
    app.update_profile(bio=text)


scheduler = BackgroundScheduler()
scheduler.add_job(update_profile, "interval", minutes=1)

if __name__ == "__main__":
    scheduler.start()
    app.run()
