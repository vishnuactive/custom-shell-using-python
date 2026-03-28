import shlex

class Tokenizer:
    def tokenize(self,user_input):
        try:
            return shlex.split(user_input)
        except Exception as ex:
            print(f"Error during parsing : {str(ex)}")

    def split_pipe_tokens(self,tokens):
        current = []
        commands = []
        for token in tokens:
            if token == '|':
                commands.append(current)
                current = []
            else:
                current.append(token)
        if current:
            commands.append(current)
        return commands
