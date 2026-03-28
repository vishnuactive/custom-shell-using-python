import os

def run(args):
    if not args:
        print("The syntax of the command is incorrect")
    else:
        for argument in args:
            os.mkdir(argument)