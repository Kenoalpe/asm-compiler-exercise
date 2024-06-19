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
        opcode_list_out = []
        counter = 0

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

            # Remove label definition
            line = AssemblerUtil.remove_label(line=line)
            if not line:
                continue

            # Replace instruction with opcode
            instruction_pattern = r'([A-Z]*\s*[A-Z]{0,1})'
            match = re.search(pattern=instruction_pattern, string=line)
            if match:
                try:
                    opcode_list_out.append(self.model.opcode_table[match.group(1).strip()])
                except KeyError:
                    raise SyntaxError(f"Instruction on line '{line}' not available in opcode table!")

            # Check if a label need to be placed
            label_pattern = r'([_a-z]\w*)\s*'
            match = re.search(pattern=label_pattern, string=line)
            if match:
                try:
                    opcode_list_out.append(AssemblerUtil.hexlify(self.model.symbol_table[match.group(1).strip()], True))
                finally:
                    pass

            # Check if a constant needs to be added
            const_value_pattern = r'#([0-9a-fA-F]{1,2})'
            match = re.search(pattern=const_value_pattern, string=line)
            if match:
                opcode_list_out.append(AssemblerUtil.hexlify(match.group(1), False))

            counter += 1

        print(opcode_list_out)
