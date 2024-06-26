import re


class AssemblerUtil:

    @staticmethod
    def remove_comments_line(line: str):
        # Prepare line and remove comments
        return line.split(';', 1)[0].strip()

    @staticmethod
    def remove_label(line: str):
        label_pattern = r'([_a-z]\w*)\s*:'
        match = re.match(pattern=label_pattern, string=line)
        if match:
            line = line.replace(match.group(1) + ':', '', 1).strip()  # Remove label from line
        return line

    @staticmethod
    def hexlify(num: int | str, isint: bool = False) -> str:
        if isint:
            num = hex(num)[2:]
        if len(num) == 1:
            num = f'0{num}'
        return num

    def __init__(self):
        raise NotImplementedError('This class is not meant to be instantiated')
