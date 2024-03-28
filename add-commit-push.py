import os

# creating functions for git add, commit, and push

def addFile(): 
        print("Executing git add. . . ")
        os.system("git add -A")
        os.system("git status")

def commitFile():
    print("Executing git commit. . . ")
    msgOption = input("Would you like to add a message? (y/n)\n")
    if msgOption != "y":
        os.system('git commit -m "File Updated"')
    else:
        commitMessage = userMsg()
        os.system("git commit -m" + f'"{commitMessage}"')

# creating a function to store default commit message and user generated message
def userMsg():
    inputMsg = input("Please enter a message: \n")
    return inputMsg

def pushFile():
    print("Executing git push. . . ")
    os.system("git push")
    os.system("git status")
        
# beginning of script / retrieving git status
print("Executing git status. . . ")
os.system("git status")

# ask user if they would like to add file(s)
userAdd = input("Would you like to stage files for commit? (y/n)\n")
if userAdd != "y":
     print("Goodbye. . .")
     exit()
else:
    addFile()

# ask user if they would like to commit changes
userCommit = input("Would you like to commit changes? (y/n)\n")
if userCommit != "y":
    print("Goodbye. . .")
    exit()
else:
   commitFile() 

#ask user if they would like to git push
userPush = input("Would you like to push? (y/n)\n")
if userPush != "y":
    print("Goodbye. . .")
    exit()
else:
   pushFile() 