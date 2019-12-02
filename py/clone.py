import RPi.GPIO as GPIO
import sys
import os
from time import sleep
from mfrc522 import SimpleMFRC522

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


def clone():
    os.system("clear")
    try:
        cpf("--------------")
        cpf("CLONE RFID TAG")
        cpf("--------------")
        print()
        sys.stdout.write(BLUE)
        print("[-] INFO: \033[1;36mPlace Source RFID tag.")
        sys.stdout.write(RESET)
        id, txt = reader.read()
        while id == "" or txt == "":
            id, txt = reader.read()
        sys.stdout.write(GREEN)
        print("[+] SUCCUSS: Read done.")
        sys.stdout.write(RESET)
        sleep(1)
        sys.stdout.write(BLUE)
        print("[-] INFO: \033[1;36mPlace Destination RFID tag.")
        sys.stdout.write(RESET)
        if id and txt not in reader.read():
            sys.stdout.write(GREEN)
            print("[+] SUCCESS: Read done.")
            sys.stdout.write(RESET)
            while not reader.write(txt):
                reader.write(txt)
            sys.stdout.write(BLUE)
            print("[-] INFO: \033[1;36mTags cloned successfully.")
            sys.stdout.write(RESET)
            sleep(1)
        else:
            sys.stdout.write(GREEN)
            print("[+] SUCCESS: Read done.")
            sys.stdout.write(RED)
            print("[x] ERROR: Tags conflict.")
            sys.stdout.write(RESET)
        print()
    except KeyboardInterrupt:
        clone()
    finally:
        GPIO.cleanup()
        os.system('setterm -cursor on')


clone()
