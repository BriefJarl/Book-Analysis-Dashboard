from scripts.scraper import scrape_books
from scripts.data_cleaning import clean_data
from scripts.model import train_model

# Step 1: Scrape data
raw_df = scrape_books()

# Step 2: Clean data
clean_df = clean_data("data/raw_data.csv")

# Save cleaned data
clean_df.to_csv("data/data.csv", index=False)

# Step 3: Train model
model, score = train_model(clean_df)

print("Model Accuracy:", score)