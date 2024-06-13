from sly import Lexer, Parser

machinecode = {
    "NOP" : "20"
}

class CalcLexer(Lexer):
    tokens = {INSTRUCTION, ADDRESS, HEX_NUMBERS, SPECIAL_CHARS, REGISTERS, COMMENTS, NOP}
    ignore = ' \t'
    ignore_comment = r'\;.*'

    # Tokens
    INSTRUCTION = r'[A-Z]*'
    ADDRESS = r'[a-zA-Z_][a-zA-Z0-9]*\:'
    HEX_NUMBERS = r'\#[0-9]*'
    #SPECIAL_CHARS = r':'
    REGISTERS = r'a|b'

    INSTRUCTION['NOP'] = NOP

     # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
    
    # Error handling rule
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
    
class CalcParser(Parser):
    tokens = CalcLexer.tokens


def run():
    lexer = CalcLexer().tok
    parser = CalcParser()