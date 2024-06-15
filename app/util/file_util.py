class FileUtils:

    def __init__(self):
        raise NotImplementedError('This class is not meant to be instantiated')

    @staticmethod
    def parse_txt(file_path: str = None):
        file_data = None
        try:
            with open(file_path) as file:
                file_data = file.read()
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
        return file_data
