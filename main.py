import gdown
import zipfile
import shutil
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

GDRIVE_FILE_ID = "1TvyxrKE4jaO7sTnGVHAA_-Qge2YbfcnW"  # from the Google Drive link
ZIP_FILENAME = "latest.zip"
DEFAULT_MOD_TARGET_FOLDER = r"C:\Program Files (x86)\Steam\steamapps\common\REPO"
MOD_TARGET_FOLDER = [DEFAULT_MOD_TARGET_FOLDER]  # Change this to your game's mod folder

# === GUI SETUP ===
window = tk.Tk()
window.title("Sagrator REPO Modpack Installer")
window.geometry("450x200")

status_label = tk.Label(window, text="", font=("Arial", 10))
progress = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")

# === FUNCTION: Download with Progress ===
def download_from_gdrive():
    status_label.config(text="Downloading files...")
    window.update_idletasks()

    url = f"https://drive.google.com/uc?id={GDRIVE_FILE_ID}"

    gdown.download(url, ZIP_FILENAME, quiet=True)

# === FUNCTION: Install ===
def install_mod():
    status_label.config(text="Installing files...")
    window.update_idletasks()

    with zipfile.ZipFile(ZIP_FILENAME, 'r') as zip_ref:
        zip_ref.extractall("temp_mod_files")

    bepinex_path = os.path.join(MOD_TARGET_FOLDER[0], "BepInEx")
    if os.path.exists(bepinex_path):
        shutil.rmtree(bepinex_path)

    for item in os.listdir("temp_mod_files"):
        s = os.path.join("temp_mod_files", item)
        d = os.path.join(MOD_TARGET_FOLDER[0], item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    shutil.rmtree("temp_mod_files")
    os.remove(ZIP_FILENAME)
    messagebox.showinfo("Success", "Mod files installed!")
    window.destroy()

# === FUNCTION: Run ===
def run_installer():
    status_label.config(text="Starting...")
    window.update_idletasks()
    try:
        download_from_gdrive()
        install_mod()
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")
        status_label.config(text="")

# === FUNCTION: Folder Picker ===
def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        MOD_TARGET_FOLDER[0] = folder
        install_folder_label.config(text=MOD_TARGET_FOLDER[0])

# === GUI LAYOUT ===
tk.Label(window, text="Installing mod to:", font=("Arial", 11)).pack(pady=5)

install_folder_label = tk.Label(window, text=MOD_TARGET_FOLDER[0], font=("Arial", 9), fg="gray")
install_folder_label.pack(pady=5)

tk.Button(window, text="Change Folder", font=("Arial", 10), command=choose_folder).pack(pady=2)

tk.Button(window, text="Start Installation", font=("Arial", 12), command=run_installer).pack(pady=10)

status_label.pack()

window.mainloop()
