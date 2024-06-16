# External imports
import re

# Internal imports
from app.util import AssemblerUtil
from app.exception import SyntaxError


class SynthesisController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        # Initialize variables
        found_instruction = False
        opcode_list_out = []

        # ToDo remove debug
        print('---------------------')
        print(self.model.opcode_table)
        print(self.model.symbol_table)
        print('---------------------')

        for line in self.model.line_data:
            # Remove comment and comment lines
            line = AssemblerUtil.remove_comments_line(line=line)
            if not line:
                continue

            print(line)
            # Replace instruction with opcode
            for key in self.model.opcode_table:
                found_instruction = False
                match = re.search(pattern=key, string=line)
                if match:
                    opcode_list_out.append(self.model.opcode_table[key])
                    found_instruction = True
                    print('true')
                    break

            # Check if any instruction was found
            if not found_instruction:
                raise SyntaxError(f"Instruction on line '{line}' not available in opcode table!")
            print()

            # for key in self.model.opcode_table:
            #     match = re.match(r'^\w+$', key)
            #     if match:
            #         opcode_list_out.append(self.model.opcode_table[key])

        print(opcode_list_out)
