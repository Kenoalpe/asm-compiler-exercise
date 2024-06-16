class OpcodeData:
    def __init__(self):
        raise NotImplementedError('This class is not meant to be instantiated')

    @staticmethod
    def get_opcode_data() -> dict[str, str]:
        return {
            'OUTPUT': '02',
            'JMP': '03',
            'LOAD A':  '04',
            'INC A': '05'
        }
