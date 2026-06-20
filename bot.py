import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import (
    FUD_MENTION, SERVER_MENTION, PAYMENT_PHOTO,
    PAYMENT_MESSAGE, FUD_MESSAGE, SERVER_MESSAGE, START_MESSAGE,
)

logging.basicConfig(format="%(asctime)s | %(levelname)s | %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

async def send_payment(update: Update) -> None:
    photo_src = PAYMENT_PHOTO.strip()
    is_url = photo_src.startswith("http://") or photo_src.startswith("https://")
    try:
        if is_url:
            await update.message.reply_photo(photo=photo_src, caption=PAYMENT_MESSAGE, parse_mode="Markdown")
        else:
            if os.path.exists(photo_src):
                with open(photo_src, "rb") as img:
                    await update.message.reply_photo(photo=img, caption=PAYMENT_MESSAGE, parse_mode="Markdown")
            else:
                await update.message.reply_text(PAYMENT_MESSAGE, parse_mode="Markdown")
    except Exception as e:
        logger.error(f"图片发送失败：{e}")
        await update.message.reply_text(PAYMENT_MESSAGE, parse_mode="Markdown")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_MESSAGE, parse_mode="Markdown")

async def pay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_payment(update)

async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_payment(update)

async def fud(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(FUD_MESSAGE + f"\n👉 {FUD_MENTION}", parse_mode="Markdown")

async def server(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(SERVER_MESSAGE + f"\n👉 {SERVER_MENTION}", parse_mode="Markdown")

def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("❌ BOT_TOKEN not found in environment variables!")
        return
    print("✅ 机器人正在运行！")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pay", pay))
    app.add_handler(CommandHandler("payment", payment))
    app.add_handler(CommandHandler("fud", fud))
    app.add_handler(CommandHandler("server", server))
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
