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

    # New line
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    # Error handling rule
    def error(self, t):
        print("Illegal alien '%s'" % t.value[0])
        self.index += 1


def run():
    data = '''
    NOPL+
    NOP
    '''

    lexer = CalcLexer()
    for token in lexer.tokenize(data):
        print('type=%r, value=%r' % (token.type, token.value))

    print(lexer)
