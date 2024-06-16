from app.models import AnalysisModel


class SynthesisModel(AnalysisModel):
    def __init__(self, assembly_file_path: str, symbol_table: dict[str, int], opcode_table=None):
        super().__init__(assembly_file_path)
        self.symbol_table = symbol_table
        self._opcode_table = opcode_table

    @property
    def opcode_table(self):
        return self._opcode_table

    @opcode_table.setter
    def opcode_table(self, opcode_table):
        self._opcode_table = opcode_table
