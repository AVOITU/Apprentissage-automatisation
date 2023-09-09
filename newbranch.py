import subprocess
import os
import first_configuration
import simplecommands

message_commit=0
branch_checkout=0

def branch_creation(branch_checkout, message_commit):
    print("Enter your parent branch's name:")
    branch_checkout=input()
    simplecommands.checkout(git_bash_path, branch_checkout)
    branch_checkout=simplecommands.new_branch(git_bash_path)
    simplecommands.checkout(git_bash_path, branch_checkout)
    message_commit=f"creation of an empty file to write the code for '{branch_checkout}'"
    simplecommands.first_touch_add_push()


root, git_bash_path=first_configuration.first_configuration()
branch_creation(branch_checkout, message_commit)
