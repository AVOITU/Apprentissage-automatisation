import first_configuration
import simplecommands
from tkinter import simpledialog
import tkinter as tk

def user_demand():
    fenetre_principale = tk.Tk()
    fenetre_principale.title("Fonctions")
    fenetre_principale.geometry("800x600")

    button_repository_initialisation = tk.Button(fenetre_principale, text="Repository initialisation", command=lambda: repository_initialisation(git_bash_path, file_path, message_commit))
    button_branch_creation = tk.Button(fenetre_principale, text="Branch creation", command=lambda: branch_creation(git_bash_path, branch_checkout))
    button_update_file = tk.Button(fenetre_principale, text="Update file", command=lambda: update_file(git_bash_path, message_commit))

    button_repository_initialisation.grid(row=0, column=0)
    button_branch_creation.grid(row=1, column=0)
    button_update_file.grid(row=2, column=0)

    fenetre_principale.mainloop()

def repository_initialisation(git_bash_path, file_path, message_commit):
    file_name=file_path.split('\\')
    simplecommands.init(git_bash_path)
    simplecommands.link_repo(git_bash_path)
    message_commit=f'first commit to create {file_name}.py, link repositories and initiate GitHub repository'
    simplecommands.first_touch_add_commit_push(git_bash_path, file_name, message_commit)
    
def branch_creation(git_bash_path, branch_checkout):
    branch_checkout=simpledialog.askstring("branch_creation", "Enter the name of your parent branch:")
    simplecommands.checkout(git_bash_path, branch_checkout)
    branch_checkout=simplecommands.new_branch(git_bash_path)
    simplecommands.checkout(git_bash_path, branch_checkout)
    message_commit=f"creation of an empty file to write the code for '{branch_checkout}'"
    file_name=[branch_checkout]
    simplecommands.first_touch_add_commit_push(git_bash_path, file_name, message_commit)

def update_file(git_bash_path, message_commit):
    file_name=simpledialog.askstring("Update file", "Enter file to update:")
    branch_checkout=file_name
    simplecommands.checkout(git_bash_path, branch_checkout)
    simplecommands.add(git_bash_path, file_name)
    simplecommands.commit(git_bash_path, message_commit)
    simplecommands.push(git_bash_path, file_name)


# def initially used to back end functionnment, no longer necessary
def complexcommands(git_bash_path, branch_checkout, message_commit, user_choice):
    try:
        match user_choice:
            case "repository_initialisation":
                repository_initialisation(git_bash_path, file_path, message_commit)
            case "branch_creation":
                branch_creation(git_bash_path, branch_checkout)
            case "update_file":
                update_file(git_bash_path, message_commit)
            case _:
                file_path=simpledialog.askstring("Erreur", "Invalid input")    
    except Exception as e:
        simpledialog.askstring("Local path", f"{e}")

if __name__ == "__main__":
    message_commit=0
    branch_checkout=0
    root, git_bash_path, file_path=first_configuration.first_configuration()
    user_demand()