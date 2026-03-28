class Command:

    def __init__(self,name,args):
        self.name = name
        self.args = args

    def __repr__(self):
        return f"Command(name={self.name}, args={self.args})"
    
    @classmethod
    def from_tokens(cls,tokens):
        if not tokens:
            return None
        else:
            name = tokens[0]
            args = tokens[1:]
            return cls(name,args)
    
    