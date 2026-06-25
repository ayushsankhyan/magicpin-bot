from core.loader import DataLoader

loader = DataLoader("expanded")

categories = loader.load_categories()
merchants = loader.load_merchants()
customers = loader.load_customers()
triggers = loader.load_triggers()

print("=" * 40)
print("Categories:", len(categories))
print("Merchants :", len(merchants))
print("Customers :", len(customers))
print("Triggers  :", len(triggers))
print("=" * 40)

print("\nSample Merchant:")
print(next(iter(merchants.keys())))