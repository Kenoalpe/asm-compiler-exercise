# External imports
import re

# Internal imports
from app.models import SynthesisModel
from app.exception import SemanticError
from app.util import AssemblerUtil


class AnalysisController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        # Initialize variables
        instruction_line_counter = 0
        symbol_table: dict[str, int | None] = {}

        # Initialize patterns
        variable_pattern = r'[_a-z]\w*\s*'
        const_value_pattern = r'#([0-9a-fA-F]{1,2})'

        all_pattern = (r'(\s*([_a-z]\w*)\s*:)?\s*([A-Z]*\s*[A-Z]\s*,{0,1}\s*[A-Z]{0,1})\s*(#([0-9a-fA-F]{0,2})\s*)?('
                       r'\s*([_a-z]\w*)\s*)?')

        # Display raw assembly
        # ToDo remove debug
        self.view.display_raw(self.model.data)

        # Parse line for line into the symbol_table
        for line in self.model.line_data:
            # Remove comment and comment lines
            line = AssemblerUtil.remove_comments_line(line=line)
            if not line:
                continue

            match = re.match(pattern=all_pattern, string=line)
            if match:

                label_definition = match.group(2)
                if label_definition is not None:
                    print('Label Def:' + label_definition)

                label_call = match.group(7)
                if label_call is not None:
                    # ToDo inc ilc
                    print('Label Call: ' + label_call)

                const_definition = match.group(5)
                if const_definition is not None:
                    # ToDo inc ilc
                    print('Value definition: ' + const_definition)

            else:
                continue

            # Check for label-definition
            # ToDo change to assembler_util
            label_pattern = r'([_a-z]\w*)\s*:'
            match = re.match(pattern=label_pattern, string=line)
            if match:
                line = line.replace(match.group(1) + ':', '', 1).strip()  # Remove label from line
                symbol_table[match.group(1)] = instruction_line_counter

            # Check for label-call
            match = re.search(pattern=variable_pattern, string=line)
            if match:
                variable = match.group()
                # Variable check if found does not already have a value
                if variable not in symbol_table:
                    symbol_table[match.group()] = None
                instruction_line_counter += 1
            instruction_line_counter += 1

            # Check if the ilc need to be incremented
            match = re.search(pattern=const_value_pattern, string=line)
            if match:
                # Increment in symbol_table when 2 Byte instruction occurs
                instruction_line_counter += 1

        # Check for semantic error
        for symbol, value in symbol_table.items():
            if value is None:
                raise SemanticError(f"Symbol: {symbol} has no value")

        return SynthesisModel(assembly_file_path=self.model.path, symbol_table=symbol_table)
