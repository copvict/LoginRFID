import RPi.GPIO as GPIO
import sys
import os
from datetime import datetime
from time import sleep
import socket

try:
    from mfrc522 import SimpleMFRC522
    from getmac import get_mac_address
    import hashlib
except:
    os.system("pip3 install mfrc522")
    os.system("pip3 install getmac")
    os.system("pip3 install hashlib")

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"

GPIO.setwarnings(False)
reader = SimpleMFRC522()
os.system('setterm -cursor off')


def cpf(text):
    sizex, sizey = os.get_terminal_size()
    center = "{:^"+str(sizex)+"}"
    print(center.format(text))


def getsalt():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    mac = get_mac_address(ip=ip)
    date = datetime.now()
    signd = date.strftime('%d-%B-%Y')
    signt = date.strftime("%I:%M:%S%p")
    salt = str(mac)+str(signt)+str(signd)
    return salt

# Salt for the hash is "<MAC Address of the device><Date><Time>"


try:
    os.system("clear")
    cpf("-------------")
    cpf("HASH RFID TAG")
    cpf("-------------")
    print()
# Checks if hash.dat file and creates if there isn't
    if not os.path.isfile('hash.dat'):
        file = open('hash.dat', 'w')
        file.close()
    if os.path.isfile('hash.dat'):
        sys.stdout.write(BLUE)
# Reads RFID tag
        print("[-] INFO: \033[1;36mPlace RFID Card.")
        sys.stdout.write(RESET)
        print()
        id, txt = reader.read()
        print("Card ID: ", id)
        sys.stdout.write(GREEN)
# Calls getsalt() to generate salt for hash function
        salt = getsalt()
# Increments the salt to the RFID tag's unique ID number
        string = str(id)+str(salt)
# Generates hash
        hsh = hashlib.md5(string.encode('utf-8')).hexdigest()
        date = datetime.now()
        signd = date.strftime('%d-%B-%Y')
        signt = date.strftime("%H:%M:%S")
# writes hash on to RFID tag
        while not reader.write(hsh):
            reader.write(hsh)
        sys.stdout.write(GREEN)
        print("[+] SUCCESS: Card written successfully.")
        sys.stdout.write(BLUE)
        print("[-] INFO: \033[1;36mSigned at "+signt+" on "+signd+".")
        sys.stdout.write(RESET)
# Stores the hash with the timestamp onto a file locally to later read from
        print()
        with open("hash.dat", "w") as data:
            data.write(str(hsh)+" "+str(signd)+" "+str(signt)+"\n")
        sleep(3)

finally:
    GPIO.cleanup()
    os.system('setterm -cursor on')
