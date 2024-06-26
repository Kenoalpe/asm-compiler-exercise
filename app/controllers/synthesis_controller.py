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
        ilc = 0
        opcode_list = []

        # Optional debugging:
        # print('---------------------')
        # print(self.model.opcode_table)
        # print(self.model.symbol_table)
        # print('---------------------')

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
            ilc, opcode_list = self._parse_line(
                counter=ilc,
                opcode_list=opcode_list,
                line=line
            )

            ilc += 1

        self.view.print_to_file(opcode_list)
        return opcode_list

    def _parse_line(self, counter: int, opcode_list, line: str):
        # Internal copies
        internal_ilc = counter
        internal_opcode_list = opcode_list

        # Match line to regex
        match = re.match(pattern=self.model.pattern, string=line)

        # Get tokens
        instruction = match.group(self.model.instruction_group)
        called_label = match.group(self.model.label_call_group)
        byte = match.group(self.model.byte_definition_group)

        # Replace instruction and byte with opcode
        if instruction:
            instruction = instruction.strip()

            # Check for pseudo-instruction
            if instruction in self.model.pseudo_instruction:
                if byte:
                    if instruction == 'DB':
                        internal_opcode_list.append(AssemblerUtil.hexlify(byte.strip(), False))
                    elif instruction == 'RESB':
                        byte = int(byte.strip())
                        for i in range(0, byte):
                            internal_opcode_list.append('00')

                    return internal_ilc, internal_opcode_list
                else:
                    raise SyntaxError(f'Line: {line} must have a number or value.')

            try:
                # Check if instruction is available in opcode table
                instruction_opcode = self.model.opcode_table[instruction]
                # Check for a byte
                if byte or called_label:
                    # Check if this instruction has different connotations, if yes differentiate between address and
                    # value if not, just add the opcode of the instruction following the value
                    if isinstance(instruction_opcode, dict):
                        if '#' in byte:
                            byte = byte.replace('#', '')
                            internal_opcode_list.append(instruction_opcode['#'])
                        else:
                            internal_opcode_list.append(instruction_opcode[''])
                    else:
                        internal_opcode_list.append(instruction_opcode)
                    if not called_label:
                        internal_opcode_list.append(AssemblerUtil.hexlify(byte.strip(), False))
                else:
                    internal_opcode_list.append(instruction_opcode)
            except KeyError:
                raise SyntaxError(f"Instruction on line '{line}' not available in opcode table!")

        # Place called_label
        if called_label:
            symbol_num = self.model.symbol_table[called_label.strip()]
            if isinstance(symbol_num, str):
                internal_opcode_list.append(AssemblerUtil.hexlify(symbol_num, False))
            else:
                internal_opcode_list.append(AssemblerUtil.hexlify(symbol_num, True))

        return internal_ilc, internal_opcode_list
