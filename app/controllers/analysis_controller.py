# External imports
import re
from typing import Dict, Any

# Internal imports
from app.models import SynthesisModel
from app.exception import SemanticError


class AnalysisController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        # Initialize variables
        counter = 0
        symbol_table: dict[str, int | None] = {}

        # Display raw assembly
        self.view.display_raw(self.model.data)

        for line in self.model.line_data:
            # Remove comment and comment lines
            line = self.__remove_comments(line=line)
            if not line:
                continue

            # Parse line into symbol_table
            self.__parse_asm_line(line=line, counter=counter, symbol_table=symbol_table)
            counter += 1

        # Check for semantic error
        for symbol, value in symbol_table.items():
            if value is None:
                raise SemanticError(f"Symbol: {symbol} has no value")

        return SynthesisModel(symbol_table=symbol_table)

    @staticmethod
    def __remove_comments(line: str):
        # Prepare line and remove comments
        return line.split(';', 1)[0].strip()

    @staticmethod
    def __parse_asm_line(line: str, counter: int, symbol_table: dict[str, int | None]):
        # Check for label
        label_pattern = r'([_a-z]\w*)\s*:'
        match = re.match(pattern=label_pattern, string=line)
        if match:
            line = line.replace(match.group(1) + ':', '', 1).strip()  # Remove label from line
            symbol_table[match.group(1)] = counter

        # Check for variable
        variable_pattern = r'[_a-z]\w*\s*'
        match = re.search(pattern=variable_pattern, string=line)
        if match:
            variable = match.group()
            # Variable check if found does not already have a value
            if variable not in symbol_table:
                symbol_table[match.group()] = None
