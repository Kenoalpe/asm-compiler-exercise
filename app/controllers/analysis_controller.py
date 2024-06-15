# External imports
import re

# Internal imports
from app.models import SynthesisModel


class AnalysisController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        symbol_table = None
        literal_table = None

        # Display raw assembly
        self.view.display_raw(self.model.data)

        # Populate tables
        assembler = None

        for line in self.model.line_data:
            # Remove comment and comment lines
            line = self.__remove_comments(line)
            if line is None:
                continue

            # Parse line into tables
            self.__parse_asm_line(line)
            print(line)

        return SynthesisModel(symbol_table=symbol_table, literal_table=literal_table)

    @staticmethod
    def __remove_comments(line: str):
        # Prepare line and remove comments
        return line.split(';', 1)[0].strip()

    @staticmethod
    def __parse_asm_line(line: str):

        # Check for label
        label_pattern = r'([_a-z]\w*)\s*:'
        match = re.match(pattern=label_pattern, string=line)
        if match:
            # ToDo something
            pass
