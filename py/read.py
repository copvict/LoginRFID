import RPi.GPIO as GPIO
import os
import sys
import re
from time import sleep
from datetime import datetime

try:
    from mfrc522 import SimpleMFRC522
except:
    os.system("pip3 install mfrc55")

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"

GPIO.setwarnings(False)
reader = SimpleMFRC522()
os.system('setterm -cursor off')
attempts = 0


def init():
    os.system("clear")
# Checks for hash.dat and if not present, exits the method
    if not os.path.isfile('hash.dat'):
        sys.stdout.write(RED)
        print("[x] ERROR: No encrypted hash.")
        sys.stdout.write(RESET)
        sys.stdout.write(BLUE)
        print("[-] INFO: Generate encrypted hash and write tag(s).")
        sys.stdout.write(RESET)
# If hash.dat is present, opens the file
    else:
        data = open('hash.dat', 'r')
        for hush in data:
            hsh, signd, signt = hush.split()
        data.close()
# Checks if the hash is a valid hash and if valid, call read()
        if re.findall(r'(?i)(?<![a-z0-9])[a-f0-9]{32}(?![a-z0-9])', hsh):
            read(hsh, signd, signt)
# If not, exit
        else:
            sys.stdout.write(RED)
            print("[x] ERROR: Corrupted hash.")
            sys.stdout.write(RESET)
    os.system('setterm -cursor on')


def read(hsh, signd, signt):
    global attempts
    flag = False
    try:
        while True:
            # Checks for attempts, if exceeds, executes kill
            if attempts <= 3:
                sys.stdout.write(BLUE)
                print(
                    "[-] INFO: \033[1;36mAuthentication required.\033[0;0m \033[1$")
                sys.stdout.write(RESET)
                if flag:
                    # For incorrect attempts, number remaining available attempts are printed.
                    if (4-attempts) == 1:
                        sys.stdout.write(BLUE)
                        print(
                            "[-] INFO:\033[1;91m%2d remaining attempt." % (4-attempts))
                        sys.stdout.write(RESET)
                    else:
                        sys.stdout.write(BLUE)
                        print(
                            "[-] INFO:\033[1;36m%2d remaining attempts." % (4-attempts))
                        sys.stdout.write(RESET)
# Reads RFID tag
                id, text = reader.read()
                print()
                print("Card ID: ", id)
# Hash is compared from RFID tag and local file hash.dat
                if hsh in text:
                    date = datetime.now()
                    sd = date.strftime('%d-%B-%Y')
                    st = date.strftime("%H:%M:%S")
                    sys.stdout.write(GREEN)
                    print("[+] SUCCESS: Login successfully at " +
                          st+" on "+sd+".")
                    print()
                    sys.stdout.write(BLUE)
                    print("[-] INFO: \033[1;36mSigned at " +
                          signt+" on "+signd+".")
                    sys.stdout.write(RESET)
                    print()
                    sleep(1)
                    break
# If hash is not same, increment attempts
                else:
                    attempts = attempts+1
                    flag = True
                    sys.stdout.write(RED)
                    print("[x] ERROR: Login failed. Try again!")
                    sys.stdout.write(RESET)
                    print()
                    sleep(1)
            else:
                # Run commmand (In my case, I am killing ssh clients connected to user pi)
                os.system("sudo pkill -HUP -u pi")
    except KeyboardInterrupt:
        init()
    finally:
        GPIO.cleanup()
        os.system('setterm -cursor on')


init()
