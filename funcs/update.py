import discord
from discord.ext import commands
import os
import shutil
import zipfile
import requests
import io

API_URL = "https://api.github.com/repos/ItzPopelka/raidbot/commits/main"
ZIP_URL = "https://github.com/ItzPopelka/raidbot/archive/refs/heads/main.zip"

SAFE_FILES = ["token.json", ".gitignore", "old_version.zip", ".current_version", ".git"]
VERSION_FILE = ".current_version"

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.check_for_update()

    def check_for_update(self):
        try:
            response = requests.get(API_URL)
            if response.status_code != 200:
                print("Cant connect to GitHub API")
                return
        
            remote_sha = response.json()['sha']
        
            if os.path.exists(VERSION_FILE):
                with open(VERSION_FILE, "r") as f:
                    local_sha = f.read().strip()
            else:
                local_sha = None

            if local_sha != remote_sha:
                print(f"New version available! (SHA: {remote_sha[:7]})")
                choice = input("Update? Y/n: ")
                if choice.lower() == 'y':
                    self.perform_full_update(remote_sha)
                else:
                    print("Skipping update...")
            else:
                print("You have the newest version!")

        except Exception as e:
            print(f"Update failed: {e}")

    def perform_full_update(self, new_sha):
        print("Creating old_version.zip...")
        with zipfile.ZipFile("old_version.zip", "w") as backup:
            for folder, subfolders, files in os.walk("."):
                for file in files:
                    file_path = os.path.join(folder, file)
                    if "old_version.zip" not in file_path:
                        backup.write(file_path)

        print("Cleaning dir...")
        for item in os.listdir("."):
            if item not in SAFE_FILES:
                if os.path.isfile(item):
                    os.remove(item)
                elif os.path.isdir(item):
                    shutil.rmtree(item)

        print("Downloading new code...")
        r = requests.get(ZIP_URL)
        if r.status_code == 200:
            z = zipfile.ZipFile(io.BytesIO(r.content))
            root_folder = z.namelist()[0]
            
            for member in z.namelist():
                if member == root_folder:
                    continue
                relative_path = member.replace(root_folder, "", 1)
                if not relative_path:
                    continue
                
                source = z.open(member)
                target_path = os.path.join(".", relative_path)
            
                if member.endswith('/'):
                    os.makedirs(target_path, exist_ok=True)
                else:
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    with open(target_path, "wb") as target:
                        shutil.copyfileobj(source, target)
        
            with open(VERSION_FILE, "w") as f:
                f.write(new_sha)
            
            print("Updated 100%.")
        else:
            print(f"Error downloading new code")

async def setup(bot):
    await bot.add_cog(Update(bot))