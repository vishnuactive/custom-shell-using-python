import shlex

class Tokenizer:
    def tokenize(self,user_input):
        try:
            return shlex.split(user_input)
        except Exception as ex:
            print(f"Error during parsing : {str(ex)}")