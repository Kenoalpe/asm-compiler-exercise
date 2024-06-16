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
        opcode_add_counter = 0

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

            # Remove label
            line = AssemblerUtil.remove_label(line=line)
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
                    break

            # Check if any instruction was found
            if not found_instruction:
                raise SyntaxError(f"Instruction on line '{line}' not available in opcode table!")

            # Check if a label need to be placed
            for key in self.model.symbol_table:
                match = re.search(pattern=key, string=line)
                if match:
                    #opcode_list_out.append(opcode_list_out[self.model.symbol_table[key] + opcode_add_counter])
                    # ToDo Hex change to hex and correct presentation
                    opcode_list_out.append(self.model.symbol_table[key] + opcode_add_counter)
                    break

            # Check if a constant needs to be added
            const_value_pattern = r'#([0-9a-fA-F]{1,2})'
            match = re.search(pattern=const_value_pattern, string=line)
            if match:
                const_value = match.group(1)
                # Add a 0 when too short
                if len(const_value) == 1:
                    const_value = f'0{const_value}'
                opcode_list_out.append(const_value)
                opcode_add_counter += 1

            print()

        print(opcode_list_out)
