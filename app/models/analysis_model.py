# External imports
import re

# Internal imports
from app.util import FileUtils


class AnalysisModel:
    def __init__(self,
                 assembly_file_path: str,
                 pattern: str,
                 pseudo_instruction: str,
                 instruction_group: int,
                 label_definition_group: int,
                 label_call_group: int,
                 byte_definition_group: int):
        self._data = FileUtils.parse_txt(assembly_file_path)
        self.path = assembly_file_path
        self.pattern = re.compile(pattern)
        self.pseudo_instruction = pseudo_instruction
        self.instruction_group = instruction_group
        self.label_definition_group = label_definition_group
        self.label_call_group = label_call_group
        self.byte_definition_group = byte_definition_group

    @property
    def data(self) -> str:
        return self._data

    @property
    def line_data(self):
        return self._data.splitlines()
