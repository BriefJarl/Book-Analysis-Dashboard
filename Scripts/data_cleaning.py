import pandas as pd

def clean_data(path):
    df = pd.read_csv(path)

    df["PRICE"] = df["PRICE"].astype(float)

    rating_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
    df["RATING"] = df["RATING"].map(rating_map)

    df["TITLE_LENGTH"] = df["TITLE"].apply(len)

    return df