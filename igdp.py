#usr/bin/env python3
from os import get_terminal_size
from colorama import Fore
from colorama import Style
from colorama import init
import instaloader
import argparse
import time
import sys
import os
import io

s=get_terminal_size().columns
init(autoreset=True)

r=Fore.RED+Style.BRIGHT
y=Fore.YELLOW+Style.BRIGHT
b=Fore.BLUE+Style.BRIGHT
g=Fore.GREEN+Style.BRIGHT
c=Fore.CYAN+Style.BRIGHT
m=Fore.MAGENTA+Style.BRIGHT                                                

def profile():
		try:
			parser=argparse.ArgumentParser()
			dp=instaloader.Instaloader()
			parser.add_argument('link',help='Enter the profile username')
			args=parser.parse_args()
			os.system("clear")
			print("\n")
			print(r+" /$$$$$$  /$$$$$$          /$$$$$$$  /$$$$$$$ ".center(s))
			print(y+"|_  $$_/ /$$__  $$        | $$__  $$| $$__  $$".center(s))
			print(b+"  | $$  | $$  \__/        | $$  \ $$| $$  \ $$".center(s))
			print(g+"  | $$  | $$ /$$$$ /$$$$$$| $$  | $$| $$$$$$$/".center(s))
			print(r+"  | $$  | $$|_  $$|______/| $$  | $$| $$____/ ".center(s))
			print(m+"  | $$  | $$  \ $$        | $$  | $$| $$     ".center(s))    
			print(r+" /$$$$$$|  $$$$$$/        | $$$$$$$/| $$     ".center(s))    
			print(y+"|______/ \______/         |_______/ |__/      ".center(s))
			print(c,"\n")
			print(y+"#### Instagram Profile Picture Downloader By C09YC47 #### \n".center(s))
			print(c+"[!] Downloading please wait.....")
			sys.stdout = dump_data = io.StringIO()
			dp.download_profile(args.link,profile_pic_only=True)
			os.system("mkdir /sdcard/IGDP> /dev/null 2>&1")
			os.system("mv "+args.link+" /sdcard/IGDP> /dev/null 2>&1")
			time.sleep(1)
			sys.stdout = sys.__stdout__
			result=(f"[*] Downloaded Successfully And Saved To Folder IGDP as '{args.link}'")
			print(g+result)
			
		except:
			print(r+"[!] This Pic Has Been Already Downloaded Or Something Went Wrong!")
			exit()
		
profile()
