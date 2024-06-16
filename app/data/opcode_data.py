class OpcodeData:
    def __init__(self):
        raise NotImplementedError('This class is not meant to be instantiated')

    @staticmethod
    def get_opcode_data() -> dict[str, str]:
        return {
            'INPUT': '01',
            'OUTPUT': '02',
            'JMP': '03',
            '#LOAD A': '04',  # With '#'
            'INC A': '05',
            'MOV B': '06',
            'ADD A': '07',
            'HALT': '08',
            'INC B': '10',
            'SUB A': '11',
            'AND A': '12',
            'OR A': '13',
            'EQUAL': '15',
            'BEQ': '16',
            'STORE A': '18',
            'LOAD A': '1D'  # Without
        }
