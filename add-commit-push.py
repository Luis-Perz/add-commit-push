import os
def addFile(userInput): 
    if userInput != "y":
        exit      
    else:
        print("Executing git add. . . ")
        os.system("git add -A")
        os.system("git status")

def commitFile(userInput):
    if userInput != "y":
        exit      
    else:
        print("Executing git commit. . . ")
        msgOption = input("Would you like to add a message?")
        if msgOption != 'y':
            os.system("git commit -m 'File Updated'")
        else:
            commitMessage = userMsg()
            os.system("git commit -m'" + commitMessage + "'")

def userMsg():
    inputMsg = input("Please enter a message: \n")
    return inputMsg

def pushFile(userInput):
    if userInput != "y":
        exit
    else:
        print("Executing git push. . . ")
        os.system("git push")
        os.system("git status")
        

print("Executing git status. . . ")
os.system("git status")

addFile(input("Would you like to stage files for commit?"))
commitFile(input("Would you like to commit changes?"))
pushFile("Would you like to push?")