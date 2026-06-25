# tests/test_health_score.py

from core.loader import DataLoader
from core.health_score import MerchantHealthScore

loader = DataLoader("expanded")

merchant = next(
    iter(loader.load_merchants().values())
)

score = MerchantHealthScore()

print(
    score.calculate(
        merchant
    )
)