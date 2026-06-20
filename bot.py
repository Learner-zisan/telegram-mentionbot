"""
Telegram 机器人 — 自动回复机器人，支持 /payment、/fud、/server 命令
安装依赖：  pip install python-telegram-bot
运行：      python bot.py
"""

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import (
    BOT_TOKEN,
    FUD_MENTION,
    SERVER_MENTION,
    PAYMENT_MESSAGE,
    FUD_MESSAGE,
    SERVER_MESSAGE,
    START_MESSAGE,
)

# ── 日志设置 ──────────────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


# ── /start ───────────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        START_MESSAGE,
        parse_mode="Markdown",
    )
    logger.info(f"/start 被 @{update.effective_user.username} 使用")


# ── /payment ─────────────────────────────────────────────────
async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        PAYMENT_MESSAGE,
        parse_mode="Markdown",
    )
    logger.info(f"/payment 被 @{update.effective_user.username} 使用")


# ── /fud ─────────────────────────────────────────────────────
async def fud(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    full_msg = FUD_MESSAGE + f"\n👉 {FUD_MENTION}"
    await update.message.reply_text(
        full_msg,
        parse_mode="Markdown",
    )
    logger.info(f"/fud 被 @{update.effective_user.username} 使用")


# ── /server ──────────────────────────────────────────────────
async def server(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    full_msg = SERVER_MESSAGE + f"\n👉 {SERVER_MENTION}"
    await update.message.reply_text(
        full_msg,
        parse_mode="Markdown",
    )
    logger.info(f"/server 被 @{update.effective_user.username} 使用")


# ── 主程序 ────────────────────────────────────────────────────
def main() -> None:
    if BOT_TOKEN == "8719510336:AAFrg4GxD5X2_7WhPuSUg-izWQtH9zu2R_w":
        print("❌ 错误：请先在 config.py 中设置您的 BOT_TOKEN！")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start",   start))
    app.add_handler(CommandHandler("payment", payment))
    app.add_handler(CommandHandler("fud",     fud))
    app.add_handler(CommandHandler("server",  server))

    print("✅ 机器人正在运行！按 Ctrl+C 停止。")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
