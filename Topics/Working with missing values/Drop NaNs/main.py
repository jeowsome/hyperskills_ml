import pandas as pd

df = pd.read_csv("data/dataset/input.txt")
old_row = df.shape[0]

df.dropna(inplace=True)
new_row = df.shape[0]

print(old_row, new_row)