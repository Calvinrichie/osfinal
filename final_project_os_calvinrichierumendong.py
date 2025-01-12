import subprocess
import shlex
import os
import shutil


def ls():
    return "\n".join(os.listdir(os.getcwd()))

def pwd():
    return os.getcwd()

def cd(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        return f"cd: {path}: No such file or directory"

def mkdir(directory):
    try:
        os.mkdir(directory)
    except FileExistsError:
        return f"mkdir: {directory}: File exists"

def rmdir(directory):
    try:
        os.rmdir(directory)
    except OSError:
        return f"rmdir: {directory}: Directory not empty or does not exist"

def touch(filename):
    with open(filename, 'w'):
        pass

def rm(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        return f"rm: {filename}: No such file"

def cp(source, destination):
    try:
        shutil.copy(source, destination)
    except FileNotFoundError:
        return f"cp: {source}: No such file"

def mv(source, destination):
    try:
        shutil.move(source, destination)
    except FileNotFoundError:
        return f"mv: {source}: No such file or directory"
    
def life ():
    return "42"

def e ():
    return "e"

def bme ():
    return "me  bee"


def help():
    return """
    Available commands:
    - ls: List files in the current directory
    - pwd: Show the current working directory
    - cd <dir>: Change the current directory
    - mkdir <dir>: Create a new directory
    - rmdir <dir>: Remove an empty directory
    - touch <file>: Create a new empty file
    - rm <file>: Remove a file
    - cp <source> <destination>: Copy a file
    - mv <source> <destination>: Move or rename a file
    - life: Get the answer to life
    - e: e
    - bme: :)
    - help: Show this help message
    - clear: Clear the terminal screen
    - exit: Exit the CLI
    """

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_cli():
    return "Exiting CLI..."

def main():
    print("Welcome to Python CLI. Type 'help' for a list of commands.")
    while True:
        user_input = input(f"{os.getcwd()} $ ").strip()
        if not user_input:
            continue
        command_parts = user_input.split()
        command = command_parts[0]
        args = command_parts[1:]

        if command == "ls":
            print(ls())
        elif command == "pwd":
            print(pwd())
        elif command == "cd" and args:
            print(cd(args[0]))
        elif command == "mkdir" and args:
            print(mkdir(args[0]))
        elif command == "rmdir" and args:
            print(rmdir(args[0]))
        elif command == "touch" and args:
            touch(args[0])
        elif command == "rm" and args:
            print(rm(args[0]))
        elif command == "cp" and len(args) == 2:
            print(cp(args[0], args[1]))
        elif command == "mv" and len(args) == 2:
            print(mv(args[0], args[1]))
        elif command == "life":
            print(life())    
        elif command == "e":
            print(e())
        elif command == "bme":
            print(bme())    
        elif command == "help":
            print(help())
        elif command == "clear":
            clear()
        elif command == "exit":
            print(exit_cli())
            break
        else:
            print(f"{command}: command not found")

