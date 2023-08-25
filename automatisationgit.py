import subprocess
import os
import tkinter as tk
from tkinter import simpledialog

def first_configuration():
    #configure the path to git bash and stock instead the path 1
    path1=0
    if path1==0:
        print("copy-past the git bash path:")
        git_bash_path=input()
        with open("automatisationgit.py","r") as git_bash_file:
            #open automatisation.py to memorize the lines, git_bash_file: name choosen to apply the function 
            # there's no importance of the name for the execution of the function, just take the same to use the write function
            lines=git_bash_file.read()

        lines[6]=git_bash_path
        with open("automatisationgit.py","w") as git_bash_file:
            git_bash_file.write(lines)


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