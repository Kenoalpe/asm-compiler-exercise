from sly import Lexer, Parser

global INSTRUCTION, NOP


class CalcLexer(Lexer):
    # Available Token
    tokens = {INSTRUCTION, NOP}

    # Ignore whitespace and tab
    ignore = " \t"

    # Tokens
    INSTRUCTION = r'[A-Z][A-Z]*'
    INSTRUCTION['NOP'] = NOP

    # Define a new line
    @_(r'\n')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    # Define error if no token matches
    def error(self, t):
        print("Illegal alien '%s'" % t.value[0])
        self.index += 1


def run():
    data = '''
NOP
NOP
'''

    lexer = CalcLexer()
    for token in lexer.tokenize(data):
        print('type=%r, value=%r' % (token.type, token.value))

    print(lexer)
