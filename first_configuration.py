import os

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


first_configuration()