import json
from pathlib import Path

class JsonRepository:

    def __init__(self, filename : str | Path):
        self.file = Path(filename)

    def get_all(self) -> list:
        if not self.file.exists():
            return []
        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def save(self,data) -> None:
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4,ensure_ascii=False)
                      