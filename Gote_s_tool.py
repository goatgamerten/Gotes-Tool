from email.mime import image
from tkinter import Image
from tkinter.tix import IMAGE
import webbrowser
import os
import time
import socket
import requests
import random
import platform
import sys

durl = "https://discord.gg/8J6Hd4t5Rq"

bin_list = [
    "11000001100010101",
    "1100000000000011001111110100",
    "10011000101000110010",
    "00110001110000101011000110",
    "1000001011010110010101010010010100101",
    "0011010101010110101011010010",
    "1100011001101010101010101010101010",
    "00110010100101010001",
]
YNList = ["I found it!", "Nah, sorry lol"]
r1 = random.randint(100, 120)

def binary_scan(r1):
    for i in range(r1):
        time.sleep(0.1)
        print(random.choice(bin_list))

def YN():
    result = random.choice(YNList)
    print(result)
    return result

def generate_password():
    length = int(input("Enter password length: "))
    characters = (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    )
    password = "".join(random.choice(characters) for i in range(length))
    print(f"Your generated password is: {password}")

def system_info():
    operating_system = platform.system()
    os_version = platform.version()
    architecture = platform.architecture()[0]
    hostname = socket.gethostname()
    python_version = sys.version
    python_implementation = platform.python_implementation()

    print("\nSystem Information:")
    print(f"Operating System: {operating_system}")
    print(f"OS Version: {os_version}")
    print(f"System Architecture: {architecture}")
    print(f"Hostname: {hostname}")
    print(f"Python Version: {python_version}")
    print(f"Python Implementation: {python_implementation}")

def weather_info():
    if platform.system() == "Windows":
        os.system("start https://wttr.in")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("curl wttr.in")

def hack_the_planet():
    phrases = [
        "Initializing cybernetic override...",
        "Bypassing mainframe security...",
        "Uploading quantum subroutine...",
        "Establishing neural uplink...",
        "Decrypting SHA-4096 firewall...",
        "Pinging Skynet...",
        "Injecting coffee into core processor...",
        "Spinning up flux capacitor...",
        "Cracking FBI database...",
        "404: File Not Found",
    ]
    os.system("cls" if os.name == "nt" else "clear")
    print("=== HACK THE PLANET MODE ACTIVATED ===\n")
    try:
        for _ in range(15):
            print(random.choice(phrases))
            time.sleep(0.7)
    except KeyboardInterrupt:
        print("\nHack interrupted by user.")
    input("\n[Press Enter to return to main menu]")

start_prompt = print(
    """
   _////               _//            _//             _/// _//////                     _//
 _/    _//             _//             _/                  _//                         _//
_//           _//    _/_/ _/   _//        _////            _//       _//       _//     _//
_//         _//  _//   _//   _/   _//    _//               _//     _//  _//  _//  _//  _//
_//   _////_//    _//  _//  _///// _//     _///            _//    _//    _//_//    _// _//
 _//    _/  _//  _//   _//  _/               _//           _//     _//  _//  _//  _//  _//
  _/////      _//       _//   _////      _// _//           _//       _//       _//    _///
                                                                                     """
)

while True:
    i = input(
        """     
     1 - Discord Link
     2 - Public/Local ip 
     3 - Gote's Bio (If the background is blue refresh)
     4 - James
     5 - Scan for smth, tbh idfk
     6 - Password Generator
     7 - System Information
     8 - Weather Information (Opens browser)
     9 - Hacking
     
     
     
     """
    )

    if i == "1":
        webbrowser.open("https://discord.gg/8J6Hd4t5Rq")
    elif i == "2":
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        response = requests.get("https://api.ipify.org?format=json")
        public_ip = response.json()["ip"]

        input(
            f"Your local ip is {local_ip}, and your public ip is {public_ip}. Press enter to continue.    "
        )
    elif i == "3":
        webbrowser.open("https://guns.lol/gote")
    elif i == "4":
        print("No :)")
    elif i == "5":
        r1 = random.randint(100, 120)
        binary_scan(r1)
        time.sleep(2)
        result = YN()
        if result == "I found it!":
            time.sleep(0.5)
            r2 = random.randint(1, 5)
            print(f"It was {r2} :)")
    elif i == "6":
        generate_password()
    elif i == "7":
        system_info()
    elif i == "8":
        weather_info()
    elif i == "9":
        hack_the_planet()

    time.sleep(2)

input("Press enter to continue")
