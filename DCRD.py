"""
This script is basically just stolen code put into one script
the way it functions is based on the text based adventure game
little dungeon https://github.com/wallacezone/little-dungeon/
the decoding methods are most likely all taken from stack overflow
the cracking of all ciphers except shift uses code written by
al sweigart https://inventwithpython.com/hacking/
"""
from sys import exit

# Main Menu
def main_menu():
    print ("Please enter your choice")
    print ("(1) Binary")
    print ("01110100 01100101 01110011 01110100")
    print ("(2) Hexdecimal") 
    print ("74 65 73 74 20 74 65 78 74 DA")
    print ("(3) Ceaser Shift")
    print ("grfg zrffntr")
    print ("(4) Base64")
    print ("dGVzdA==")

    choice = input("> ");

    if "1" in choice:
        binary()
    if "2" in choice:
        hexdecimal()
    if "3" in choice:
        shift()
    if "4" in choice:
        base64()
    else:
        main_menu()

# Binary
# https://stackoverflow.com/questions/7396849/

def binary():
    print ("Please enter your string")

    choice = input("> ");

    a = int(choice, 2)
    b = a.to_bytes((a.bit_length() + 7) // 8, 'big').decode()
    print (b)
    reboot("You will be redirected to the reboot menu")

# Hexdecimal
# https://stackoverflow.com/questions/3283984/

def hexdecimal():
    print ("You can uses spaces or no spaces")
    print ("DO NOT USE DASHES")
    print ("Please enter your string")

    choice = input("> ");

    a = bytes.fromhex(choice).decode('ascii')
    print (a)
    reboot("You will be redirected to the reboot menu")
 
# Ceaser Shift
# https://github.com/Hakarin/CrackROTk

def shift():
    print ("This will print 25 possible messages you have to manually determin which is correct")
    print ("Please enter your string")
    bruteforceshift()
import string

def rotate(text, offset):
    offset %= len(text)
    return text[offset:] + text[:offset]

def make_rot(offset):
    table = str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
    rotate(string.ascii_lowercase, offset) + rotate(string.ascii_uppercase, offset))

    return lambda text: text.translate(table)

def bruteforceshift():
    choice = input("> ")
    rot1 = make_rot(-1)
    print("ROT-1")
    print(rot1(choice))
    print("")
    rot2 = make_rot(-2)
    print("ROT-2")
    print(rot2(choice))
    print("")
    rot3 = make_rot(-3)
    print("ROT-3")
    print(rot3(choice))
    print("")
    rot4 = make_rot(-4)
    print("ROT-4")
    print(rot4(choice))
    print("")
    rot5 = make_rot(-5)
    print("ROT-5")
    print(rot5(choice))
    print("")
    rot6 = make_rot(-6)
    print("ROT-6")
    print(rot6(choice))
    print("")
    rot7 = make_rot(-7)
    print("ROT-7")
    print(rot7(choice))
    print("")
    rot8 = make_rot(-8)
    print("ROT-8")
    print(rot8(choice))
    print ("")
    rot9 = make_rot(-9)
    print("ROT-9")
    print(rot9(choice))
    print("")
    rot10 = make_rot(-10)
    print("ROT-10")
    print(rot10(choice))
    print("")
    rot11 = make_rot(-11)
    print("ROT-11")
    print(rot11(choice))
    print("")
    rot12 = make_rot(-12)
    print("ROT-12")
    print(rot12(choice))
    print("")
    rot13 = make_rot(-13)
    print("ROT-13")
    print(rot13(choice))
    print("")
    rot14 = make_rot(-14)
    print("ROT-14")
    print(rot14(choice))
    print("")
    rot15 = make_rot(-15)
    print("ROT-15")
    print(rot15(choice))
    print("")
    rot16 = make_rot(-16)
    print("ROT-16")
    print(rot16(choice))
    print("")
    rot17 = make_rot(-17)
    print("ROT-17")
    print(rot17(choice))
    print("")
    rot18 = make_rot(-18)
    print("ROT-18")
    print(rot18(choice))
    print("")
    rot19 = make_rot(-19)
    print("ROT-19")
    print(rot19(choice))
    print("")
    rot20 = make_rot(-20)
    print("ROT-20")
    print(rot20(choice))
    print("")
    rot21 = make_rot(-21)
    print("ROT-21")
    print(rot21(choice))
    print("")
    rot22 = make_rot(-22)
    print("ROT-22")
    print(rot22(choice))
    print("")
    rot23 = make_rot(-23)
    print("ROT-23")
    print(rot23(choice))
    print("")
    rot24 = make_rot(-24)
    print("ROT-24")
    print(rot24(choice))
    print("")
    rot25 = make_rot(-25)
    print("ROT-25")
    print(rot25(choice))
    print("")
    rot26 = make_rot(-26)
    print("ROT-26")
    print(rot26(choice))
    print("")

    reboot("You will be redirected to the reboot menu")

# BASE64
#
def base64():
    import base64
    print("Please input your string")
    choice = input("> ")
    a = base64.b64decode(choice)
    print (a)

    reboot("You will be redirected to the reboot menu")
# START
def start():
    main_menu()

# REBOOT
def reboot(s):
    print (s) 
    print ("Do you want to use the script again? (y/n)")

    choice = ""
    while choice != "y" and choice != "n":
        choice = input("> ")
        if choice == "y":

            start()

        elif choice == "n":
            exit(0)

# MAIN

start() 
