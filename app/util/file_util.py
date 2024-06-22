class FileUtils:
    @staticmethod
    def parse_txt(file_path: str):
        file_data = None
        try:
            with open(file_path) as file:
                file_data = file.read()
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
        return file_data

    @staticmethod
    def parse_array_to_file(filename: str, text: [str]):
        with open(filename, 'w') as file:
            file.write(' '.join(text))

    def __init__(self):
        raise NotImplementedError('This class is not meant to be instantiated')
