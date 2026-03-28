from commandparser.command import Command
from commandparser.tokenizer import Tokenizer
import os
class Shell:
    def __init__(self):
        self.running = True
        self.tokenizer = Tokenizer()

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
                print(command)
                if command.name.lower() == 'exit':
                    self.running = False
                    print("Bye")
        except Exception as ex:
            print(f"Error : {str(ex)}")
    
    def run(self):
        while self.running:
            self.handle_user_input(self.receive_user_input())