from app.util import FileUtils


class AnalysisModel:
    def __init__(self, assembly_file_path: str):
        self._data = FileUtils.parse_txt(assembly_file_path)

    @property
    def data(self) -> str:
        return self._data
