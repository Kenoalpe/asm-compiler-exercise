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
        counter = 0
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

            # Remove label definition
            line = AssemblerUtil.remove_label(line=line)
            if not line:
                continue

            # Parse line into the opcode list
            counter, opcode_list_out = self._parse_line(
                counter=counter,
                opcode_list=opcode_list_out,
                line=line
            )

            counter += 1

        print(opcode_list_out)

    def _parse_line(self, counter: int, opcode_list, line: str):
        # Internal copies
        internal_counter = counter
        internal_opcode_list = opcode_list

        # Match line to regex
        match = re.match(pattern=self.model.pattern, string=line)

        # Replace instruction and constant with opcode
        instruction = match.group(3)
        if instruction:
            instruction = instruction.strip()
            try:
                # Check if instruction is available in opcode table
                instruction_opcode = self.model.opcode_table[instruction]

                # Check for a constant
                constant = match.group(self.model.byte_definition_group)
                if constant:
                    # Check if this instruction has different connotations, if yes differentiate between address and
                    # value if not, just add the opcode of the instruction following the value
                    if isinstance(instruction_opcode, dict):
                        if '#' in constant:
                            constant = constant.replace('#', '')
                            internal_opcode_list.append(instruction_opcode['#'])
                        else:
                            internal_opcode_list.append(instruction_opcode[''])
                    else:
                        internal_opcode_list.append(instruction_opcode)
                    internal_opcode_list.append(AssemblerUtil.hexlify(constant.strip(), False))
                else:
                    internal_opcode_list.append(instruction_opcode)
            except KeyError:
                raise SyntaxError(f"Instruction on line '{line}' not available in opcode table!")

        # Place label
        label = match.group(self.model.label_call_group)
        if label:
            internal_opcode_list.append(AssemblerUtil.hexlify(self.model.symbol_table[label.strip()], True))

        return internal_counter, internal_opcode_list
