from scripts.scraper import scrape_books
from scripts.data_cleaning import clean_data
from scripts.model import train_model
raw_df = scrape_books()
clean_df = clean_data("data/raw_data.csv")
clean_df.to_csv("data/data.csv", index=False)
model, score = train_model(clean_df)

print("Model Accuracy:", score)
