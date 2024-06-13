import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Configs
API_HASH = os.environ['API_HASH']
APP_ID = int(os.environ['APP_ID'])
BOT_TOKEN = os.environ['BOT_TOKEN']
OWNER_ID = os.environ['OWNER_ID']
FORCE_JOIN_CHANNEL = os.environ['FORCE_JOIN_CHANNEL']

# Buttons
START_BUTTONS=[
    [
        InlineKeyboardButton('Join Our Channel', url=f'https://t.me/{FORCE_JOIN_CHANNEL}'),
        InlineKeyboardButton('Join Our Channel', url=f'https://t.me/{FORCE_JOIN_CHANNEL}'),
    ],
    [InlineKeyboardButton('Admin', url="https://t.me/vanshfr")],
]

# Running bot
xbot = Client('File-Sharing', api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Notify about bot start
with xbot:
    xbot_username = xbot.get_me().username  # Better call it global once due to telegram flood id
    print("Bot started!")
    if OWNER_ID.lower() == 'all':
        print(f"OWNER_ID is set to 'all', allowing all users to use the bot.")
    elif OWNER_ID.isdigit():
        xbot.send_message(int(OWNER_ID), "Bot started!")
    else:
        print(f"OWNER_ID is not a valid integer or 'all': {OWNER_ID}")


# Start & Get file
@xbot.on_message(filters.command('start') & filters.private)
async def _startfile(bot, update):
    # Check if the user is a member of the force join channel
    try:
        await xbot.get_chat_member(FORCE_JOIN_CHANNEL, update.from_user.id)
    except Exception:
        # If the user is not a member, send a message with the force join button
        await update.reply_text(
            f"You must join our channel to use this bot.",
            True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('Join Channel', url=f'https://t.me/{FORCE_JOIN_CHANNEL}')]
            ])
        )
        return

    if update.text == '/start':
        await update.reply_text(
            f"I'm File-Sharing!\nYou can share any telegram files and get the sharing link using this bot!\n\n/help for more details...",
            True, reply_markup=InlineKeyboardMarkup(START_BUTTONS))
        return

    # No need to handle any specific file ID or message ID
    await update.reply_text("Please send a file to get the sharing link.")


# Help msg
@xbot.on_message(filters.command('help') & filters.private)
async def _help(bot, update):
    await update.reply_text("Supported file types:\n\n- Video\n- Audio\n- Photo\n- Document\n- Sticker\n- GIF\n- Voice note\n- Video note\n\n If bot didn't respond, contact @xgorn", True)


@xbot.on_message(filters.media & filters.private)
async def _main(bot, update):
    if OWNER_ID.lower() == 'all':
        # Allow all users to use the bot
        pass
    elif OWNER_ID.isdigit() and int(OWNER_ID) == update.from_user.id:
        # Allow the owner to use the bot
        pass
    else:
        # Deny access for other users
        return

    try:
        copied = await update.copy(chat_id=update.from_user.id)
    except Exception as e:
        print(f"Error copying file: {e}")
        return

    msg_id = copied.id
    if copied.video:
        unique_idx = copied.video.file_unique_id
    elif copied.photo:
        unique_idx = copied.photo.file_unique_id
    elif copied.audio:
        unique_idx = copied.audio.file_unique_id
    elif copied.document:
        unique_idx = copied.document.file_unique_id
    elif copied.sticker:
        unique_idx = copied.sticker.file_unique_id
    elif copied.animation:Okay, got it. Here's the updated code without the force join feature:

        unique_idx = copied.animation.file_unique_id
    elif copied.voice:
        unique_idx = copied.voice.file_
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButtonunique_id
    elif copied.video_note:
        unique_idx = copied.video_note.file_unique_id
    else:
        await copied.delete()
        return

    await update.reply_text(
        'Here is Your Sharing Link:',
        True,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('Sharing Link',
                                  url=f'https://t.me/{xbot_username}?start={unique_idx.lower()}')]
        ]), InlineKeyboardMarkup

# Configs
API_HASH = os.environ['API_HASH']
APP_ID = int(os.environ['APP_ID'])
BOT_TOKEN = os.environ['BOT_TOKEN']
OWNER_ID = os
    )
    await asyncio.sleep(0.5)  # Wait do to avoid 5 sec flood ban


xbot.run()
