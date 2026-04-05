# RaidBOT - ItzPopelka

> ⚠️ **Disclaimer**: This project is for **educational and demonstration purposes only**. Using it to disrupt Discord servers may violate **Discord Terms of Service** and local laws. The author assumes **no responsibility** for misuse.

A modular **Discord bot** written in Python using `discord.py`. It uses a **bot token** (not a user/self token) and loads commands dynamically via cogs.

---

## ✅ Key Points

* Uses **Discord Bot Token** (OAuth2 bot application)
* **Prefix commands**: `r?[command]`
* Modular cog-based architecture
* You dont need the perms - the bot does

---

## 📦 Requirements

* Python **3.8+**
* `discord.py`
* `requirements.txt` installed (`pip install -r requirements.txt`)
* A **Discord Bot Application** with required *(All for no bugs)* intents enabled

---

## 🚀 Setup

1. **Clone the repository**
*Open terminal and paste this in*
```bash
git clone https://github.com/ItzPopelka/raidbot.git
cd raidbot
```

2. **Install dependencies**
*Open terminal and paste this in*
```bash
pip install -r requirements.txt
```

3. **Create a Discord Bot**
*Make it look like legit bot*
* Go to Discord *[Developer Portal](https://discord.com/developers/applications/)*
* Create an application → Bot
* Copy the **BOT TOKEN**
* Enable **Server Members Intent** and **Message Content Intent**

4. **Configure token**
*You need bot token (not user!)*
- Create token.json file
- Paste this in: ```{"TOKEN": "YOUR_BOT_TOKEN"}```
- Replace "YOUR_BOT_TOKEN" with your actual token

> ❗ Never send anyone or publish your token.

5. **Run the bot**
*Open terminal and paste this in*
```bash
cd raidbot
python main.py
```

---

## 🧩 Command Prefix

All commands use the prefix:

```
r?[command]
```

Example:

```
r?info
```

---

## 📚 Commands

### Server

| Command             | Description                                | Permissions      |
| ------------------- | ------------------------------------------ | ---------------- |
| `ban_all`           | Bans all members except the command author | Ban Members      |
| `rename_all <name>` | Renames all members                        | Manage Nicknames |
| `purge_all`         | Purges messages in all text channels       | Manage Messages  |

### Channels & Roles

| Command    | Description                                      | Permissions     |
| ---------- | ------------------------------------------------ | --------------- |
| `channels` | Deletes all channels and recreates text channels | Manage Channels |
| `roles`    | Deletes all roles and recreates roles            | Manage Roles    |

### Server Info

| Command       | Aliases                   | Description                    |
| ------------- | ------------------------- | ------------------------------ |
| `change_info` | —                         | Changes server name and icon   |
| `info`        | `i`, `serverinfo`, `list` | Prints server stats to console |

### Spam / Media

| Command       | Description                         | Permissions    |
| ------------- | ----------------------------------- | -------------- |
| `spam`        | Sends repeated messages             | —              |
| `spam_crash`  | Spams gifs that crashes your dc     | —              |
| `spam_ping`   | Repeatedly mentions everyone        | —              |
| `emoji_spam`  | Deletes emojis and creates new ones | Manage Emojis  |
| `invite_spam` | Creates multiple invite links       | Create Invites |
| `spam_muzik1` | Repeated music link                 | —              |
| `spam_muzik2` | Repeated music link                 | —              |
| `spam_video`  | Repeated video link                 | —              |

### Automation / Combined

| Command     | Description                                     | Permissions   |
| ----------- | ----------------------------------------------- | ------------- |
| `full_nuke` | Runs multiple destructive commands sequentially | Administrator |
| `bypass`    | Attempts to remove anti-raid bots/channels      | Administrator |

### System

| Command   | Description              |
| --------- | ------------------------ |
| `restart` | Restarts the bot process |
| `stop`    | Stops the bot            |

### Misc

| Command | Description                                                                      |
| ------- | ---------------------------------------------------------------------------------|
| `uwu`   | Sends a GIF                                                                      |
| `ip`    | Sends a redirect link (logging functionality present in web page)                |
| `wb`    | Sends a list where are all webhooks in the server where the command was executed |
| `crash` | Spams crash gif that you create (Ress is 15000x15000, you need good internet)    |

---

## 🗂 Project Structure

```
├── 📁 assets
│   └── 🖼️ pfp.webp
├── 📁 funcs
│   ├── 🐍 ban.py
│   ├── 🐍 bypass.py
│   ├── 🐍 channels.py
│   ├── 🐍 crash.py
│   ├── 🐍 full_nuke.py
│   ├── 🐍 info.py
│   ├── 🐍 purge.py
│   ├── 🐍 rename.py
│   ├── 🐍 roles.py
│   ├── 🐍 spam.py
│   ├── 🐍 system.py
│   ├── 🐍 update.py
│   ├── 🐍 uwu.py
│   ├── 🐍 video.py
│   └── 🐍 webhook.py
├── 📁 scripts
│   └── 🐍 crash-gif_maker.py
├── ⚙️ .gitignore
├── 📝 README.md
├── 🐍 main.py
└── 📄 requirements.txt
```

---

## ⚠️ Legal & Safety Notes

* Use **only** in servers you own or have **explicit permission** to manage
* Some commands are **destructive** by design
* Logging or tracking users without consent may be **illegal** in some regions

This repository is intended to showcase **Discord API automation techniques**, not to encourage abuse.

---

## 🧠 Development Notes

* Commands are loaded dynamically from `funcs/`
* Prefix is hardcoded as `r?`
* Intents are set to `Intents.all()` — adjust for production
---

## 🧪 Update
- Just press `y/n` on the start-up

---

## 📄 License

Educational / demonstration use only. If you want to edit this, mention me in the README.

---
## 🐍 Support and communication
Feel free to dm me on these platforms:
- [Discord](https://discord.com/users/1478453769401405544)
- [Instagram](https://instagram.com/tomase.k_)

