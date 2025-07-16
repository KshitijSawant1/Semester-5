import pandas as pd

df = pd.read_csv("spam-sms-classifier/spam.csv", encoding='latin-1')

print(df.head())
print(df["v1"].unique())
