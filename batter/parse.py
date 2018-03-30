from enum import Enum
from lexer import Token

class Expression(Enum):
    Assign = 0
    Op = 1
    FnCall = 2
    FnDef = 3

class Parser():
    def __init__(self, lexer):
        print(lexer.data)
        self.var_types = ['int', 'str']
        self.lex = lexer.data
        self.sym = self.lex[0]
        self.idx = 0
        self.block()
    
    def next_sym(self):
        if self.idx + 1 >= len(self.lex):
            print('nah')
        self.idx += 1
        self.sym = self.lex[self.idx]

    def accept(self, s, c=None):
        if self.sym[0] == s and (True if not c else self.sym[1] == c):
            self.next_sym()
            return True
        return False
    
    def expect(self, s):
        if(self.accept(s)): return True
        raise Exception("Unexpected symbol: " + s)
    
    def block(self):
        if(self.accept(Token.Symbol)):
            if self.sym[1] in self.var_types:
                self.expect(Token.Symbol)
                self.expect(Token.Punc, ';')