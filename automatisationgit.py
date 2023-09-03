import subprocess
import os
import tkinter as tk
from tkinter import simpledialog

def working_directory():
    #define the working directory because the file created in configuration is not writing with the python file
    for root, dirs, files in os.walk('/'):
        if "automatisationgit.py" in files:
            os.chdir(root)


def configuration_file():
        #search the path to git bash, write it in "git_bash_path.txt" in order to stock it.
        try:
            for root, dirs, files in os.walk('/'):
                if "git-bash.exe" in files:
                    git_bash_path=f"{root}\git-bash.exe"
                    with open("git_bash_path.txt","w") as git_bash_file:
                        git_bash_file.write(git_bash_path)
                    break
        except ValueError:                   
            print("Git bash not found, verify the installation of the software")


def first_configuration():
    #search for a previous file with git bash path, write it if absent, return the path for the continuation of the programm if present
    if not os.path.exists("git_bash_path.txt"):
        working_directory()
        configuration_file()
    else:
        with open("git_bash_path.txt","r") as git_bash_file:
            git_bash_path=git_bash_file.read()

    return git_bash_path


def local_path(git_bash_path):
    #ask the path from the user to separate it and prepare the command cd to bring git at the right place
    print("copy-past the path of your local repository")
    local_path=input()
    subprocess.run([git_bash_path,"-c","cd",f"{local_path}"])

def init(git_bash_path):
    subprocess.run([git_bash_path,"-c","git","init"])


def main():
    git_bash_path=first_configuration()
    local_path(git_bash_path)
    init(git_bash_path)


main()