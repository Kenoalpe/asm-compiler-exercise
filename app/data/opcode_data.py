class OpcodeData:
    @staticmethod
    def get_opcode_data() -> dict[str, str]:
        return {
            'INPUT': '01',
            'OUTPUT': '02',
            'JMP': '03',
            'LOAD A,': {
                '#': '04',
                '': '1D'
            },
            'INC A': '05',
            'MOV B,A': '06',
            'ADD A,B': '07',
            'HALT': '08',
            'INC B': '10',
            'SUB A,B': '11',
            'AND A,B': '12',
            'OR A,B': '13',
            'EQUAL': '15',
            'BEQ': '16',
            'STORE A,': '18',
        }

    @staticmethod
    def get_pseudo_instruction_data():
        return ['DB', 'EQU', 'RESB']

    def __init__(self):
        raise NotImplementedError('This class is not meant to be instantiated')
