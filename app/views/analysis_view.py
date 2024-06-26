class AnalysisView:
    @staticmethod
    def display_raw(assembler: str):
        print('Assembly code to assemble:')
        print('--------------------------')
        if assembler is not None:
            print(assembler)
        print('--------------------------')

    def __init__(self):
        raise NotImplementedError('This class is not meant to be instantiated')
