import json
from pathlib import Path

class JsonRepository:

    def __init__(self, filename : str | Path):
        self.file = Path(filename)

    def get_all(self) -> list:
        if not self.file.exists():
            return []
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save(self,data) -> None:
        try:
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except OSError as error:
            print(f"Error al guardar el archivo: {error}")

    def next_id(self,data : list):
        if not data:
            return 1
        return max(item["id"] for item in data) + 1