# External imports
import re

# Internal imports
from app.models import SynthesisModel
from app.exception import SemanticError, SyntaxError
from app.util import AssemblerUtil


class AnalysisController:
    @staticmethod
    def semantic_error_check(symbol_table: dict[str, int | None]):
        for symbol, value in symbol_table.items():
            if value is None:
                raise SemanticError(f"Symbol: {symbol} has no value")

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        # Initialize variables
        ilc = 0
        symbol_table: dict[str, int | None] = {}

        # Parse line for line into the symbol_table
        for line in self.model.line_data:
            # Remove comment and comment lines
            line = AssemblerUtil.remove_comments_line(line=line)
            if not line:
                continue

            # Parse line into symbol-table
            ilc, symbol_table = self._parse_line(
                instruction_line_counter=ilc,
                symbol_table=symbol_table,
                line=line
            )

            # Inc ilc for next line
            ilc += 1

        # Check for a sematic error
        self.semantic_error_check(symbol_table)

        return SynthesisModel(
            analysis_model=self.model,
            symbol_table=symbol_table,
        )

    def _parse_line(self, instruction_line_counter: int, symbol_table: dict[str, int | None], line: str):
        # Internal copies
        internal_ilc = instruction_line_counter
        internal_symbol_table = symbol_table

        # Match line to regex
        match = re.match(pattern=self.model.pattern, string=line)

        # Get tokens
        instruction = match.group(3)
        defined_label = match.group(self.model.label_definition_group)
        called_label = match.group(self.model.label_call_group)
        byte = match.group(self.model.byte_definition_group)

        # Check if anything matches, if not raise an SyntaxError
        if match:
            # Check if a label definition needs to be added to the symbol_table
            if defined_label:
                internal_symbol_table[defined_label] = instruction_line_counter

            # Check if a label gets called
            if called_label:
                # Increment counter because of the extra byte
                internal_ilc += 1
                if called_label not in internal_symbol_table:
                    internal_symbol_table[called_label] = None
            else:
                # Check for a byte value
                if byte:
                    # Increment counter
                    internal_ilc += 1

            # Check for pseudo-instructions
            if instruction:
                instruction = instruction.strip()
                if instruction in self.model.pseudo_instruction:
                    if instruction == 'DB':
                        internal_ilc -= 1
                    elif instruction == 'EQU':
                        internal_ilc -= 2
                        internal_symbol_table[defined_label] = byte
                    elif instruction == 'RESB':
                        internal_ilc = internal_ilc + int(byte) - 2

        else:
            # Wrong characters
            raise SyntaxError(f'No valid assembly on line: {instruction_line_counter}')

        # Return updated counter and symbol_table
        return internal_ilc, internal_symbol_table
