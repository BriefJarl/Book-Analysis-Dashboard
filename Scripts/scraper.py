import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    all_items = []

    for i in range(1, 51):
        print(f"Scraping page {i}")

        try:
            res = requests.get(base_url.format(i), timeout=5)
        except:
            continue

        soup = BeautifulSoup(res.text, "html.parser")
        articles = soup.select("article.product_pod")

        for article in articles:
            title = article.find("h3").find("a")["title"]
            price = article.select_one(".price_color").text.split("£")[1]
            rating = article.select_one(".star-rating")["class"][1]

            all_items.append([title, price, rating])

    df = pd.DataFrame(all_items, columns=["TITLE", "PRICE", "RATING"])

    df.to_csv("data/raw_data.csv", index=False)

    return df