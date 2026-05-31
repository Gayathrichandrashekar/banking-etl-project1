import pandas as pd
import random
from faker import Faker

fake = Faker()

records = []

for i in range(10000):
    records.append({
        "customer_id": i + 1,
        "customer_name": fake.name(),
        "account_type": random.choice(
            ["Savings", "Current"]
        ),
        "transaction_amount": round(
            random.uniform(100, 50000), 2
        ),
        "transaction_type": random.choice(
            ["Credit", "Debit"]
        ),
        "city": fake.city()
    })

df = pd.DataFrame(records)

df.to_csv(
    "data/banking_data.csv",
    index=False
)

print("Generated 10000 records")