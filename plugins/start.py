from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/torleechgopal")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/joinchat/6gpkQ61WLqFjOGZl")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nI'm Gopal's YouTube Uploader..! Send me YouTube link and I'll upload that video/audio for you😊"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
