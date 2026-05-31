import pandas as pd

df = pd.read_csv(
    "data/banking_data.csv"
)

df["transaction_amount"] = (
    df["transaction_amount"] * 1.05
)

df.to_csv(
    "data/banking_data.csv",
    index=False
)

print("Transformation completed")