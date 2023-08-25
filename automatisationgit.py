import subprocess
import os
import tkinter as tk
from tkinter import simpledialog

def first_configuration():
      #configure the path to git bash and stock it
    if not os.path.exists("git_bash_path"):
        try:
            for root, dirs, files in os.walk("C:"):
                if "git-bash.exe" in files:
                    git_bash_path=f"{root}\git-bash.exe"
                    print(git_bash_path)
                    with open("git_bash_path","w") as git_bash_file:
                        git_bash_file.write(git_bash_path)
                    break
        except ValueError:                   
            print("copy-past the git bash path:")
            git_bash_path=input()
            with open("git_bash_path","w") as git_bash_file:
                git_bash_file.write(git_bash_path)


def local_path():
    #ask the path from the user to separate it and prepare the command cd to bring git at the right place
    print("copy-past the path of your local repository")
    local_path=input()
    local_path=local_path.split('\\')
    for path in local_path:
        subprocess.run(["C:\Program Files\Git\git-bash.exe","-c","cd",path])

def init():
    subprocess.run()


def main():
    first_configuration()
    local_path()


main()