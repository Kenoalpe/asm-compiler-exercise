# External imports
from sly import Lexer, Parser

# Internal imports
from app.models import AnalysisModel, SynthesisModel
from app.views import AnalysisView, SynthesisView
from app.controllers import AnalysisController, SynthesisController
from app.util import FileUtils


class AsmLexer(Lexer):
    # Available Token
    tokens = {INSTRUCTION, NOP}

    # Ignore whitespace and tab
    ignore = " \t"

    # Ignore assembler
    ignore_comment = r'\;.*'

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


class AsmParser(Parser):
    tokens = AsmLexer.tokens

    def __init__(self):
        self.env = {}

    @_('INSTRUCTION')
    def statement(self, p):
        print('Test')

    # Grammar rules and actions
    @_('NOP')
    def statement(self, p):
        print('NOP -> PRINT')


def run():
    # Run analysis on the assembly file and return the synthesis_model
    synthesis_model = AnalysisController(model=AnalysisModel('assembler/asm-1.txt'), view=AnalysisView).run()

    # Set the opcode table in the synthesis model

    # Run the synthesis to generate machine code
    SynthesisController(model=synthesis_model, view=SynthesisView).run()

    #print('Welcome, let\'s assemble some assembly!\n')

    # Assembly program code parse
    #data = FileUtils.parse_txt('assembler/asm-1.txt')

    # Output raw input data
    #print('Assembly code to assemble:')
    #print('__________________________')
    #if data is not None:
    #    print(data)
    #print()

    # Get instances of lexer and parser
    #lexer = AsmLexer()

    # Split file into tokens
    #tokenized = lexer.tokenize(data)

    # Print
    #for token in tokenized:
    #    print('line=%r, type=%r, value=%r' % (token.lineno, token.type, token.value))
