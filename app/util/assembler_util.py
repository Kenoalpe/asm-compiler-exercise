class AssemblerUtil:
    def __init__(self):
        raise NotImplementedError('This class is not meant to be instantiated')

    @staticmethod
    def remove_comments_line(line: str):
        # Prepare line and remove comments
        return line.split(';', 1)[0].strip()
