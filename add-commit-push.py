import os

def printAdd(userInput): 
    if userInput == "Y" or "y":
        print("git add")
        os.system("git add -A")
    elif userInput == "N" or "n":
        exit
    else:
        print("That's not a proper command")
        printAdd(input("Would you like to stage files for commit?"))

def printComm(userInput):
    if userInput == "Y" or "y":
        msgOption = input("Would like to enter add a message? Y or N?")
        if msgOption == "Y" or "y":
            userMsg = input("Enter your message")
            print("git commit")
            os.system(f"git commit -m '{userMsg}'")
        elif msgOption == "N" or "n":
            print("git commit")
            os.system("git commit")
        else:
            print("That's not a proper command.")
            printComm(input("Would you like to execute Git commit? Y or N?"))
    elif userInput == "N" or "n":
        exit
    else:
        print("That's not a proper command.")
        printComm()

def printPush(userInput):
    if userInput == "Y" or "y":
        print("git push")
        os.system("git push")
    elif userInput == "N" or "n":
        exit
    else:
        print("That's not a proper command.")
        printPush(input("Would you like to execute Git push? Y or N?"))


print("Executing git status. . . ")
os.system("git status")

printAdd(input("Would you like to stage files for commit?"))
printComm(input("Would you like to execute Git commit? Y or N?"))
printPush(input("Would you like to execute Git push? Y or N?"))
 