from commandparser.command import Command
from commandparser.tokenizer import Tokenizer
from commandexecutor.executor import Executor
from builtin_commands.register import is_builtin_command,execute_builtin_command
import os

class Shell:
    def __init__(self):
        self.running = True
        self.tokenizer = Tokenizer()
        self.executor = Executor()

    def display_prompt(self):
        return f"{os.getcwd()}>"
    
    def receive_user_input(self):
        return input(self.display_prompt())    
    def handle_user_input(self,user_input):
        try:
            if not user_input:
                return
            else:
                tokens = self.tokenizer.tokenize(user_input)
                command = Command.from_tokens(tokens)
                if is_builtin_command(command):
                    execute_builtin_command(command)
                else:
                    self.executor.execute(command)
        except Exception as ex:
            print(f"Error : {str(ex)}")
    
    def run(self):
        try:
            while self.running:
                self.handle_user_input(self.receive_user_input())
        except EOFError:
            print()
        except KeyboardInterrupt:
            print("Interrupted by user")