# External imports
import re

# Internal imports
from app.util import AssemblerUtil

class SynthesisController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        # Initialize variables
        opcode_list_out = []



        print(self.model.symbol_table)

