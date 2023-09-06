import subprocess
import os
import tkinter as tk
from tkinter import simpledialog

def working_directory():
    #define the working directory because the file created in configuration is not writing with the python file
    for root, dirs, files in os.walk('/'):
        if "automatisationgit.py" in files:
            os.chdir(root)
            break

def configuration_file():
    #search the path to git bash, write it in "git_bash_path.txt" in order to stock it.
    try:
        for root, dirs, files in os.walk('/'):
            if "git-bash.exe" in files:
                git_bash_path=os.path.join(root, "git-bash.exe")
                with open("git_bash_path.txt","w") as git_bash_file:
                    git_bash_file.write(git_bash_path)
                return git_bash_path
    except FileNotFoundError:                   
        print("Git bash not found, verify the installation of the software")

def first_configuration():
    #search for a previous file with git bash path, write it if absent, return the path for the continuation of the programm if present
    working_directory()
    if os.path.exists("git_bash_path.txt"):
        with open("git_bash_path.txt","r") as git_bash_file:
            git_bash_path=git_bash_file.read()
    else:
        git_bash_path=configuration_file()

    return git_bash_path

def local_path():
    #ask the path from the user to separate it and prepare the command cd to bring git at the right place
    print("copy-past the path of your local repository")
    file_path=input()
    os.chdir(file_path)
    file_path=file_path.split("\\")

    return file_path

def touch(git_bash_path,local_path):
    file_name=local_path[-1]
    subprocess.run([git_bash_path,"-c",f"touch '{file_name}'"])

def init(git_bash_path):
    subprocess.run([git_bash_path,"-c","git init"])

def rename_master(git_bash_path):
    subprocess.run([git_bash_path,"-c","git branch -M main"])

def link_repo(git_bash_path):
    print("Enter an URL for your GitHub repository:")
    URL_repo_github=input()
    subprocess.run([git_bash_path,"-c",f"git remote add origin '{URL_repo_github}'"])
    return URL_repo_github

def first_touch_add_push(git_bash_path,local_path):
    file_name=local_path[-1]
    subprocess.run([git_bash_path,"-c",f"touch '{file_name}.py'"])
    subprocess.run([git_bash_path,"-c",f"git add '{file_name}.py'"])
    subprocess.run([git_bash_path,"-c",f"git push origin '{file_name}.py'"])

def add(git_bash_path):

    file_name=input()
    subprocess.run([git_bash_path,"-c",f"git add '{file_name}.py'"])

def branch_name(git_bash_path):
    print("Enter your branch name:")
    branch=input()
    subprocess.run([git_bash_path,"-c",f"git branch '{branch}'"])

def stash(git_bash_path):
    subprocess.run([git_bash_path,"-c",f"git '"])

def reset(git_bash_path):
    subprocess.run([git_bash_path,"-c",f"git '"])

def main():
    git_bash_path=first_configuration()
    file_path=local_path()
    touch(git_bash_path,file_path)
    first_touch_add_push(git_bash_path,file_path)
    init(git_bash_path)


main()