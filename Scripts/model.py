from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(df):
    X = df[["RATING", "TITLE_LENGTH"]]
    y = df["PRICE"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LinearRegression()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)

    return model, score