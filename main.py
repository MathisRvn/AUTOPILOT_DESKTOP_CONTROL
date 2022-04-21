import time
import _thread


import gui
from board import Arduino

ard = None

'''
def memory_menu():

    while 1:

        print("\n\nMemory Menu")

        print("1/ clone memory")
        print("2/ reset memory")
        print("3/ exit")

        answer = input("?")
        print("\n\n")

        if answer == "1":
            print("cloning memory")
            ard.writeCommand('mem')
            print("memory cloned")

        elif answer == "2":
            print("resetting memory")
            ard.writeCommand('cln')
            print("memory reset")

        elif answer == "3":
        
            break


def specific_cmd_menu():

    while (1):

        print("\n\nSpecific commands ?")

        print("1/ print receiver input")
        print("2/ print servo outputs")
        print("3/ print axis output")
        print("4/ ping")
        print("5/ exit")

        answer = input('?')

        if answer == "1":
            ard.writeCommand("cmd")

        elif answer == "2":
            ard.writeCommand("out")

        elif answer == "3":
            ard.writeCommand("axi")

        elif answer == "4":
            ard.writeCommand("awk")

        elif answer == "5":
            break


def gyro_menu():

    while (1):

        print("\n\Gyro ?")

        print("1/ print current attitude")
        print("2/ calibrate gyro")
        print("3/ exit")

        answer = input('?')

        if answer == "1":
            ard.writeCommand("att")

        elif answer == "2":
            ard.writeCommand("cal")

        elif answer == "3":
            break


def main_menu():
    while (1):

        print("\n\nWhat do you want to do ?")

        print("1/ memory")
        print("2/ Gyro")
        print("3/ specific command")
        print("4/ exit")

        answer = input('?')

        if answer == "1":
            memory_menu()

        elif answer == "2":
            gyro_menu()

        elif answer == "3":
            specific_cmd_menu()

        elif answer == "4":
            break

'''


def main_loop(thread_name):
    while 1:

        time.sleep(0.5)

        ard.writeCommand('cmd')
        time.sleep(0.2)
        ard.writeCommand('out')
        time.sleep(0.2)
        ard.writeCommand('axi')
        time.sleep(0.2)
        ard.writeCommand('att')
        time.sleep(0.2)

        gui.update(ard)


if __name__ == "__main__":

    print("Welcome to the desktop console!\n\n")

    ard = Arduino()

    _thread.start_new_thread(main_loop, ("Thread-2-MAIN",))

    gui.start(ard)

    print("\n\nSee you later!")
