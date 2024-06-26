# Internal Imports
from app.util import FileUtils


class SynthesisView:
    @staticmethod
    def print_to_file(text):
        FileUtils.parse_array_to_file('assembler/machine-code.txt', text)

    def __init__(self):
        raise NotImplementedError('This class is not meant to be instantiated')
