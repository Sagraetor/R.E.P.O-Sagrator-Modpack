import os
import requests
import zipfile
import io
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# === CONFIG ===
GITHUB_REPO = "Sagraetor/R.E.P.O-Sagrator-Modpack"
ZIP_FILE_URL = f"https://github.com/{GITHUB_REPO}/latest.rar"  # or replace with direct zip link
MOD_TARGET_FOLDER = r"C:\Program Files (x86)\Steam\steamapps\common\REPO"  # change this to your friend's mod folder path

def download_and_install_mod():
    print("Downloading mod from GitHub...")
    response = requests.get(ZIP_FILE_URL)
    if response.status_code != 200:
        print("Download failed.")
        return

    print("Extracting mod files...")
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
        zip_ref.extractall("temp_mod_files")

    bepinex_path = os.path.join(MOD_TARGET_FOLDER, "BepInEx")
    if os.path.exists(bepinex_path):
        print("Found existing BepInEx folder. Deleting it...")
        shutil.rmtree(bepinex_path)
        print("BepInEx folder deleted.")

    print(f"Installing to {MOD_TARGET_FOLDER}...")
    for item in os.listdir("temp_mod_files"):
        s = os.path.join("temp_mod_files", item)
        d = os.path.join(MOD_TARGET_FOLDER, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    shutil.rmtree("temp_mod_files")
    print("Mod installation complete!")

if __name__ == "__main__":
    download_and_install_mod()
