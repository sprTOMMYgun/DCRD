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


    choice = input("> ");

    if "1" in choice:
        binary()
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
