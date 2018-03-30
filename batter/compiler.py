from lexer import Lexer
from parse import Parser

lex = Lexer('tests/first.btr')
parser = Parser(lex)