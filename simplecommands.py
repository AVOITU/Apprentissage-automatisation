import subprocess
from first_configuration import first_configuration
from tkinter import simpledialog

#define empty variable for some functions in order to ask name for the user
message_commit=0
branch_checkout=0

def init(git_bash_path):
    #local repository initialisation and rename the master branch in main branch
    subprocess.run([git_bash_path,"-c","git init>outputinit.txt"])
    subprocess.run([git_bash_path,"-c","git branch -M main>outputrename.txt"])
        

def touch(git_bash_path,file_name):
    #create file based on name given by the user, name=["ok"] for test but is usually defined by the branch or the folder
    file_name=file_name[-1]
    subprocess.run([git_bash_path,"-c",f"touch '{file_name}.py'>outputtouch.txt"])
    with open(f"{file_name}.py","w") as touch_file:
        touch_file.write(f"\ndef():\ndef {file_name}():\n{file_name}()")
    return file_name 

def link_repo(git_bash_path):
    #ask user for the path to the GitHub repository
    URL_repo_github=simpledialog.askstring("Link repo", "Enter an URL for your GitHub repository:")
    subprocess.run([git_bash_path,"-c",f"git remote add origin '{URL_repo_github}'>outputlinkrepo.txt"])
    return URL_repo_github

def add(git_bash_path, file_name):
    #in order to stage
    subprocess.run([git_bash_path,"-c",f"git add '{file_name}.py'>outputadd.txt"])

def commit(git_bash_path, message_commit):
    #if there is no message commit define by another function before ask it to the user and commit
    if not message_commit==0:
        subprocess.run([git_bash_path, "-c", f'git commit -m "{message_commit}">outputcommit.txt'])
    else :
        message_commit=simpledialog.askstring("Commit", "Enter your commit message:")
        subprocess.run([git_bash_path, "-c", f'git commit -m "{message_commit}">outputcommit.txt'])

def push(git_bash_path, file_name):
    #to push the files
    subprocess.run([git_bash_path,"-c",f"git push -u origin '{file_name}'>outputpush.txt"])

def new_branch(git_bash_path):
    #create new branch
    branch_name=simpledialog.askstring("New branch", "Enter your new branch name:")
    subprocess.run([git_bash_path,"-c",f"git branch '{branch_name}'>outputnewbranch.txt"])
    return branch_name

def checkout(git_bash_path, branch_checkout):
    #if checkout is precised is another function checkout to this branch otherwise ask the user for the name
    if branch_checkout==0:
        branch_checkout=simpledialog.askstring("Checkout", "Enter your destination branch:")
        subprocess.run([git_bash_path,"-c",f"git checkout '{branch_checkout}'>outputcheckout.txt"])
    else:
        subprocess.run([git_bash_path,"-c",f"git checkout '{branch_checkout}'>outputcheckout.txt"])

    return branch_checkout

def first_touch_add_commit_push(git_bash_path,file_name, message_commit):
    #will be moved in complex commands, do all the actions necessary furing the first creation of a new file
    file_name=touch(git_bash_path,file_name)
    add(git_bash_path, file_name)
    commit(git_bash_path, message_commit)
    push(git_bash_path, file_name)

def test():
    #test all commands in the programm one by one
    root, git_bash_path, file_path=first_configuration()
    init(git_bash_path)
    #following lines (l.76 to l.77) are here to simplificate the test in order to pass first configuration programm that can be long
    #remove the # in l.76 to 78 and put # on l.72 to do make the simplication
    #file_path="C:\\Users\\avoit\\OneDrive\\Documents\\Programmation\\Projets\\AutomatisationGit\\Test"
    #os.chdir(file_path)
    #git_bash_path="C:\\Program Files\\Git\\git-bash.exe"
    file_name=["ok"]
    touch(git_bash_path, file_name)
    link_repo(git_bash_path)
    add(git_bash_path, file_name)
    commit(git_bash_path,message_commit)
    file_name=["main"]
    push(git_bash_path, file_name)
    new_branch(git_bash_path)
    checkout(git_bash_path, branch_checkout)
    first_touch_add_commit_push(git_bash_path,file_name, message_commit)

if __name__ == "__main__":
    test()