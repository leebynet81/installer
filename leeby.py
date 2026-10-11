#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

print("=================================================================")
print("   Starting Leeby.com PRIVATE EDITION DM520 Python 3 AJPanel...   ")
print("=================================================================")

# 1. Update Package Feeds and System Core
print("[1/10] [Leeby.com] Updating Feeds & System Core...")
os.system("opkg update && opkg upgrade -y")

# 2. Install Core System Dependencies & Python 3 Tools
print("[2/10] [Leeby.com] Installing Core Dependencies & Python3 Tools...")
os.system("opkg install wget curl python3-core python3-requests python3-json python3-codecs python3-certifi python3-urllib3 ffmpeg gstplayer exteplayer3 enigma2-plugin-systemplugins-serviceapp -y")

# 3. Install Softcams
print("[3/10] [Leeby.com] Installing All Softcams & Emulators for Python3...")
os.system("wget -q --no-check-certificate https://raw.githubusercontent.com/MOHAMED19OS/Enigma2-Softcams/main/installer.sh -O - | sh")

# 4. Install Your Specific Custom Panels
print("[4/10] [Leeby.com] Installing Mohamed Panel...")
os.system("wget -O - https://raw.githubusercontent.com/goper77wq/MohamedStore/main/install.sh | sh 2>/dev/null")

print("[5/10] [Leeby.com] Installing LinuxsatPanel V 5.91...")
os.system("wget -q --no-check-certificate https://raw.githubusercontent.com/Belfagor2005/LinuxsatPanel/main/installer.sh -O - | sh 2>/dev/null")

print("[6/10] [Leeby.com] Installing MagicPanelGold...")
os.system("wget -q --no-check-certificate https://raw.githubusercontent.com/Ham-ahmed/G10/refs/heads/main/MagicPanelGold-install.sh -O - | sh 2>/dev/null")

# 5. Install AJPanel and General Tools
print("[7/10] [Leeby.com] Installing AJPanel...")
os.system("wget -q --no-check-certificate https://raw.githubusercontent.com/biko-73/AjPanel/main/installer.sh -O - | sh")

# 6. Customizations: MK Loading Spinner Directory
print("[8/10] [Leeby.com] Setting Up Custom MK Spinner Directory...")
os.system("mkdir -p /usr/share/enigma2/spinner/")

# 7. Clean-up & Restart
print("[9/10] [Leeby.com] Cleaning Temporary Files...")
os.system("rm -rf /tmp/*.ipk /tmp/*.tar.gz /tmp/*.sh")

print("=================================================================")
print("   Leeby.com PRIVATE EDITION FINISHED! RESTARTING ENIGMA2 GUI    ")
print("=================================================================")
os.system("sleep 3 && init 4 && sleep 2 && init 3")
