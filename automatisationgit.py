import subprocess
import os
import tkinter as tk
from tkinter import simpledialog
import first_configuration
import simplecommands

def local_path():
    #ask the path from the user to separate it and prepare the command cd to bring git at the right place
    print("copy-past the path of your local repository")
    file_path=input()
    os.chdir(file_path)

    return file_path

def main():
    root, git_bash_path=first_configuration()
    file_path=local_path()

main()