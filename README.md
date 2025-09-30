# R.E.P.O - Sagrator Modpack Installer ![Python](https://img.shields.io/badge/Python-3776AB?logo=python\&logoColor=white) ![Windows](https://img.shields.io/badge/Platform-Windows-blue) ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green)

## Overview

**R.E.P.O - Sagrator Modpack Installer** is a **Windows GUI application** for installing and managing mod files for the game **REPO**.

The installer handles:

* Downloading the latest mod files from **Google Drive**
* Installing the mod into the game's folder
* Optionally deleting installed mod files
* Custom folder selection for flexibility

---

## Screenshots

![Screenshot 1](screenshots/screenshot1.png)
*Main installer window showing installation path and buttons.*

![Screenshot 2](screenshots/screenshot2.png)
*Progress during download and installation.*

> Add your own screenshots in a `screenshots` folder and update the paths above.

---

## Features

* **Automatic download** from Google Drive
* **Zip extraction** and file placement in game folder
* **Folder picker** to choose custom installation path
* **Progress feedback** via GUI labels and progress bar
* **Delete mod files** button to safely remove installed files

---

## Installation

1. **Clone or download this repository**.
2. Ensure **Python 3.9+** is installed on your system.
3. Install required packages:

```bash
pip install gdown
```

4. Place the installer script in any convenient folder.
5. Run the installer:

```bash
python R.E.P.O-Sagrator-Modpack.py
```

6. Choose the game folder or keep the default:
   `C:\Program Files (x86)\Steam\steamapps\common\REPO`

> You can also download **pre-built installers or zip releases** from the [Releases](https://github.com/YourUsername/R.E.P.O-Sagrator-Modpack/releases) section for convenience.

---

## Usage

1. **Change Folder** – Optional: select a custom installation folder.
2. **Start Installation** – Downloads and installs the mod automatically.
3. **Delete Mod Files** – Remove all installed mod files safely.

The installer handles `BepInEx` folder, configuration files, and other mod-related assets automatically.

---

## What I Learned / Key Challenges

* **GUI Development** with Tkinter: designed a responsive interface with buttons, labels, and progress bar.
* **File Management**: handled zip extraction, folder copying, and safe deletion of files.
* **Downloading from Google Drive** using `gdown` with progress handling.
* **Error Handling**: implemented checks for missing folders, permission issues, and file conflicts.
* **User Experience**: added clear progress feedback and confirmation dialogs for install and delete actions.
* **Cross-tool Integration**: combined Python scripting with Steam game directories and mod management.

---

## Structure

* **R.E.P.O-Sagrator-Modpack.py** – Main Python script with GUI.
* **icon.ico** – Window icon for the installer.
* **screenshots/** – Folder for project screenshots.
* **Releases/** – Pre-built installers or zip releases for easy download.
