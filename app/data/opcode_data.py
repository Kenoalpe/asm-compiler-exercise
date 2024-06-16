class OpcodeData:
    def __init__(self):
        raise NotImplementedError('This class is not meant to be instantiated')

    @staticmethod
    def get_opcode_data() -> dict[str, int]:
        return {
            'OUTPUT': 0x02,
            'LOAD A':  0x04,
            'INC A': 0x05,
            'NOP': 0x0C,
            'JMP': 0x03
        }
