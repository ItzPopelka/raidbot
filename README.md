# RaidBOT - ItzPopelka

> ⚠️ **Warning:** This bot is for **educational and demonstration purposes only**. Using it to disrupt Discord servers is a **violation of Discord's Terms of Service** and can result in the permanent termination of your account, bot, or server. The author assumes **no responsibility** for any misuse or damage caused by this software.

A feature-rich Discord selfbot written in Python, designed to demonstrate various automation and API functionalities. It operates via a user account, not a bot token.

## ⚙️ Features

| Category | Commands | Description |
| :--- | :--- | :--- |
| **🔧 Prefix** | `r?[command]` | Use before every command. |
| **🛠️ Server Management** | `ban`, `purge`, `rename` | Mass moderation, channel cleaning, and member renaming. |
| **💥 Disruption** | `spam`, `invite_spam`, `emoji_spam` | Channel spamming with various content types. |
| **⚡ Nuke & Raid** | `full_nuke`, `channels`, `roles` | Extreme server alteration commands (destructive). |
| **📊 Information** | `info`, `system` | Fetches user, server, or system details. |
| **🔧 Utility** | `bypass`, `change_info`, `video`, `ip_logger`* | Additional utilities for profile, guild changes, etc. |

*Use of `ip_logger` is heavily discouraged and may be illegal.

## 📁 Project Structure

```
RaidBOT/
├── 📁 assets/          # Static resources (images, etc.)
├── 📁 funcs/           # All command modules
│   ├── ban.py
│   ├── bypass.py
│   ├── channels.py
│   ├── change_info.py
│   ├── emoji_spam.py
│   ├── full_nuke.py
│   ├── info.py
│   ├── invite_spam.py
│   ├── ip_logger.py
│   ├── purge.py
│   ├── rename.py
│   ├── roles.py
│   ├── spam.py
│   ├── system.py
│   └── video.py
├── 📁 web/             # Web panel files (PHP)
│   └── index.php
├── 🐍 bot.py           # Main bot launcher and core
├── 📄 requirements.txt # Python dependencies
└── 📄 README.md        # This file
```

## 🚀 Quick Start

### Prerequisites
- Dependencies `(requirements.txt)`
- Python 3.8 or higher
- A Discord bot accaunt
- Basic understanding of python and command line

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ItzPopelka/RaidBOT.git
    cd RaidBOT
    ```

2.  **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure the bot:**
    Open `bot.py` in a text editor and locate the `bot.run()` line at the bottom. Replace `'YOUR_USER_TOKEN_HERE'` with your actual Discord user token.
    > **⚠️ Critical:** Never share this token. Anyone with it can control your account.

4.  **Run the bot:**
    ```bash
    python bot.py
    ```
    The bot will log in, load all command modules, and be ready in your Discord client.

## ⚠️ Legal & Safety Disclaimer

**This software is provided strictly for educational purposes.** Understanding how these tools work can help server administrators better defend against them.

- **Violates Discord ToS:** Using a selfbot or automating a user account is explicitly forbidden by Discord.
- **High Risk:** Your Discord account will very likely be **permanently banned** if detected.
- **Ethical Use:** Only use this in private servers you own or with **explicit, written permission** from the server owner. Never use it to harass others or damage communities.

The developer (`ItzPopelka`) is **not responsible** for any consequences resulting from the use of this code, including account termination, legal action, or damage to online communities.

## 🔧 Command Loading

The bot dynamically loads all valid `.py` modules from the `funcs/` directory. The core loading logic in `bot.py` is as follows:

```python
import os
async def load_extensions():
    funcs_dir = "funcs"
    extensions = [f[:-3] for f in os.listdir(funcs_dir) 
                  if f.endswith('.py') and f != '__init__.py']
    for ext in extensions:
        try:
            await bot.load_extension(f"{funcs_dir}.{ext}")
            print(f"✅ Loaded: {ext}")
        except Exception as e:
            print(f"❌ Failed to load {ext}: {e}")
```

