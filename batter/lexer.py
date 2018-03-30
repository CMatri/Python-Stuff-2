import re
from enum import Enum

class Token(Enum):
    Number = 0
    String = 1
    Symbol = 2
    Operator = 3
    Punc = 4

class Lexer():
    def __init__(self, fname):
        self.data = []
        self.tokens = {
            Token.Number : '[.0-9]',
            Token.String : ('\'', '"'),
            Token.Symbol : '[_a-zA-Z]',
            Token.Operator : '+-*/%><',
            Token.Punc : '(){};:.,=',
        }

        with open(fname) as f:
            content = [s.strip() for s in f.readlines()]            
            for line in content:
                i = 0
                while i < len(line):
                    i += self.tokenize(i, line) + 1

    def tokenize(self, i, line):
        c = line[i]
        if c in ' \n': return 0
        elif c in self.tokens[Token.Operator]: 
            if c == '-' and i + 1 < len(line) and line[i + 1] == '>': 
                self.data.append((Token.Operator, '->'))
                return 1
            else: self.data.append((Token.Operator, c))
        elif c in self.tokens[Token.Punc]: self.data.append((Token.Punc, c))
        elif c in self.tokens[Token.String]: 
            j, string = self.tokenize_string(i, line)
            self.data.append((Token.String, string))
            return j
        elif re.match(self.tokens[Token.Number], c):
            j, number = self.tokenize_number(i, line)
            self.data.append((Token.Number, number))
            return j
        elif re.match(self.tokens[Token.Symbol], c):
            j, symbol = self.tokenize_symbol(i, line)
            self.data.append((Token.Symbol, symbol))
            return j
        else: raise Exception('Unknown symbol: ', line, c)
        return 0

    def tokenize_string(self, i, line):
        for j, c in enumerate(line[i+1::]):
            if c == line[i]:
                return j + 1, line[i+1:j+i+1]
        raise Exception('Unclosed string: ', line)
    
    def tokenize_number(self, i, line):
        for j, c in enumerate(line[i::]):
            if not re.match(self.tokens[Token.Number], c) or i + j == len(line) - 1:
                return j-1, line[i:j+i]
        raise Exception('Number error: ', line)
    
    def tokenize_symbol(self, i, line):
        for j, c in enumerate(line[i::]):
            if not re.match(self.tokens[Token.Symbol], c) or i + j == len(line) - 1:
                return j-1, line[i:j+i]
        raise Exception('Symbol error: ', line)
        

