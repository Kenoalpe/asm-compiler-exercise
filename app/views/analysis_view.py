class AnalysisView:
    @staticmethod
    def display_raw(assembler: str):
        print('Assembly code to assemble:')
        print('--------------------------')
        if assembler is not None:
            print(assembler)
        print('--------------------------')
