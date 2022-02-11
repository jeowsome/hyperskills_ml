import pandas as pd


def print_dim(df):
    row, col = df.shape
    print(f"This DataFrame contains {row} rows and {col} columns")
