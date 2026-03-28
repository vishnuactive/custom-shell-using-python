import os


def run(args):
    if not args:
        print("Syntac of the command is incorrect")
    else:
        for argument in args:
            try:
                file = open(argument,"r")
                print('\n'.join(file.readlines()))
            except FileNotFoundError:
                print(f"File not found : {argument}")
