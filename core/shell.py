from commandparser.command import Command
from commandparser.tokenizer import Tokenizer
from commandexecutor.executor import Executor
from builtin_commands.register import is_builtin_command,execute_builtin_command
from commandexecutor.executor_pipe import PipeExecution
import os

class Shell:
    def __init__(self):
        self.running = True
        self.tokenizer = Tokenizer()
        self.executor = Executor()
        self.pipe_executor = PipeExecution()

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
                piped_commmands = self.tokenizer.split_pipe_tokens(tokens)
                commands = []
                for command in piped_commmands:
                    commands.append(Command.from_tokens(command))
                if len(commands) == 1 and is_builtin_command(commands[0]):
                    execute_builtin_command(commands[0])
                else:
                    if len(commands) == 1:
                        self.executor.execute(commands[0])
                    else:
                        self.pipe_executor.execute_pipe_commands(commands)
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