import os


print("add-commit-push")
print("Executing git status: ")
os.system("git status")
print("Executing git add: ")
os.system("git add -A")
os.system("git commit -m 'Message'")
os.system("git push")