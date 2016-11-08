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

    choice = input("> ");

    if "1" in choice:
        binary()
    if "2" in choice:
        hexdecimal()
    else:
        main_menu()

#Binary
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
