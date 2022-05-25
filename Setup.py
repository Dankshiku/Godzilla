#!/bin/bash

##   Blackbird   : 	Denial of service attack tool
##   Author 	   : 	Dank Shiku 
##   Version 	   : 	1.0
##   Github 	   : 	https://github.com/Dankshiku

import os 
import sys
import time
sys
#Color
YELLOW = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[36m'
GREEN = '\033[32;1m'
RED = '\033[31;1m'
WHITE = '\033[m'
#
#Banner
banner= ''' \033[32;1m
 █████╗   ██████╗ ██████╗ ███████╗██╗██╗     ██╗      █████╗
██╔════╝ ██╔═══██╗██╔══██╗╚══███╔╝██║██║     ██║     ██╔══██╗
██║  ███╗██║   ██║██║  ██║  ███╔╝ ██║██║     ██║     ███████║
██║   ██║██║   ██║██║  ██║ ███╔╝  ██║██║     ██║     ██╔══██║
╚██████╔╝╚██████╔╝██████╔╝███████╗██║███████╗███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ \033[32;1m
    \033[m  Tool Created by @Dankshiku \033[m\033[31;1m'''

def installation():
      print("")
      os.system("clear")
      print(banner)
      print("\033[31;1m[+]\033[31;1m \033[m DOWNLOAD REQUIREMENTS    ")
      print("")
      os.system("pkg install python -y")
      os.system("pkg install ruby -y")
      os.system("pkg install nmap -y")
      os.system("pkg install perl")
      os.system("git clone https://github.com/sullo/nikto")
      os.system("clear")
      print("\033[31;1m[+]\033[31;1m \033[m Installation Successfull    ")
      time.sleep(4)
      os.system("clear")
      os.system("python Godzilla.py")
def main():
       installation()
main()