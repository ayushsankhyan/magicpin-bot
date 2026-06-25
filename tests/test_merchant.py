# tests/test_merchant.py

from core.loader import DataLoader
import json

loader = DataLoader("expanded")

merchant = next(
    iter(loader.load_merchants().values())
)

print(json.dumps(merchant, indent=2))