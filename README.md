# 🤖 Telegram Auto-Reply Bot

A simple Telegram bot with automatic responses for `/payment`, `/fud`, and `/server` commands.

---

## 📁 Files
```
telegram_bot/
├── bot.py           ← Main bot (run this)
├── config.py        ← ✏️ Edit YOUR settings here
├── requirements.txt ← Dependencies
└── README.md
```

---

## 🚀 Setup (Step by Step)

### Step 1 — Get your Bot Token
1. Open Telegram and search for **@BotFather**
2. Send `/newbot` and follow the steps
3. Copy the **token** it gives you (looks like `123456789:ABCdef...`)

### Step 2 — Edit config.py
Open `config.py` and fill in:
```python
BOT_TOKEN      = "123456789:ABCdefGHIjklMNO..."  # Your token
FUD_MENTION    = "@adminusername"                  # Who to mention for /fud
SERVER_MENTION = "@adminusername"                  # Who to mention for /server
```
You can also **customize all the messages** in `config.py`.

### Step 3 — Install Python & dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run the bot
```bash
python bot.py
```
You'll see: `✅ Bot is running!`

---

## 💬 Commands

| Command    | What it does                                      |
|------------|---------------------------------------------------|
| `/start`   | Shows welcome message & command list              |
| `/payment` | Sends your full payment info automatically        |
| `/fud`     | Sends FUD message + mentions your specified admin |
| `/server`  | Sends server info + mentions your specified admin |

---

## 🖥️ Keep it Running 24/7 (Optional)

**On a VPS / Linux server:**
```bash
# Install screen
sudo apt install screen

# Start a screen session
screen -S mybot

# Run the bot
python bot.py

# Detach (bot keeps running): Ctrl+A then D
# Re-attach later: screen -r mybot
```

Or use **PM2**:
```bash
npm install -g pm2
pm2 start bot.py --interpreter python3
pm2 save
```

---

## ❓ Troubleshooting
- **"Invalid token"** → Double-check your token in `config.py`
- **Bot not responding** → Make sure `bot.py` is still running
- **Mention not working** → Make sure username has `@` and is correct
