# core/loader.py

import json
from pathlib import Path


class DataLoader:

    def __init__(self, dataset_path="expanded"):
        self.dataset_path = Path(dataset_path)

    def load_json(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def load_categories(self):
        data = {}

        folder = self.dataset_path / "categories"

        for file in folder.glob("*.json"):
            item = self.load_json(file)

            key = item.get("slug", file.stem)

            data[key] = item

        return data

    def load_merchants(self):
        data = {}

        folder = self.dataset_path / "merchants"

        for file in folder.glob("*.json"):
            item = self.load_json(file)

            data[file.stem] = item

        return data

    def load_customers(self):
        data = {}

        folder = self.dataset_path / "customers"

        for file in folder.glob("*.json"):
            item = self.load_json(file)

            data[file.stem] = item

        return data

    def load_triggers(self):
        data = {}

        folder = self.dataset_path / "triggers"

        for file in folder.glob("*.json"):
            item = self.load_json(file)

            data[file.stem] = item

        return data