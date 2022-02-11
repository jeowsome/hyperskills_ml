import pandas as pd

df = pd.read_csv("data/dataset/input.txt")

result = df.isnull().sum() / df.shape[0]

print(result.round(2))