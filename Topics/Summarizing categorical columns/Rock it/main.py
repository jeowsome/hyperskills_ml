import pandas as pd

df = pd.read_csv("data/dataset/input.txt")
print(df.labels.loc[df.labels == "R"].count())