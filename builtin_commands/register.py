from builtin_commands import cat,clrscr,mkdir,exit

BUILTINS = {
    "cls": clrscr.run,
    "clear": clrscr.run,
    "mkdir": mkdir.run,
    "cat": cat.run,
    "exit": exit.run
}

def is_builtin_command(command):
    return command.name in BUILTINS

def execute_builtin_command(command):
    function = BUILTINS.get(command.name)
    if function:
        function(command.args)