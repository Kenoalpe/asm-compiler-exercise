class AnalysisView:
    @staticmethod
    def display_raw(assembler: str):
        print('Assembly code to assemble:')
        print('__________________________')
        if assembler is not None:
            print(assembler)
        print('__________________________')

    @staticmethod
    def display_cleaned(assembler: str):
        print('Raw assembly without comments')
        print('__________________________')
        if assembler is not None:
            print(assembler)
        print('__________________________', end='')
