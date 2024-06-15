class SynthesisModel:
    def __init__(self, symbol_table, literal_table, opcode_table=None):
        self.symbol_table = symbol_table
        self.literal_table = literal_table
        self._opcode_table = opcode_table

    @property
    def opcode_table(self):
        return self._opcode_table

    @opcode_table.setter
    def opcode_table(self, opcode_table):
        self._opcode_table = opcode_table
