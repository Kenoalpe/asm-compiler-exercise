from app.models import AnalysisModel


class SynthesisModel(AnalysisModel):
    def __init__(self, assembly_file_path: str, pattern: str, symbol_table: dict[str, int], opcode_table=None):
        super().__init__(assembly_file_path,
                         pattern=pattern,
                         # ToDo get from model
                         label_definition_group=2,
                         label_call_group=7,
                         byte_definition_group=5
                         )
        self.symbol_table = symbol_table
        self._opcode_table = opcode_table

    @property
    def opcode_table(self):
        return self._opcode_table

    @opcode_table.setter
    def opcode_table(self, opcode_table):
        self._opcode_table = opcode_table
