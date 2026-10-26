import requests
from bs4 import BeautifulSoup
import pandas as pd

# Test E-commerce website එකේ URL එක
url = "http://books.toscrape.com/"

print("Scraping started. Please wait...")
response = requests.get(url)

# HTML Parse කිරීම
soup = BeautifulSoup(response.text, "html.parser")

# වෙබ් අඩවියේ ඇති සෑම පොතක්ම අඩංගු 'article' tags සොයා ගැනීම
books = soup.find_all("article", class_="product_pod")

data = []

for book in books:
    # පොතේ නම ලබා ගැනීම
    title = book.find("h3").find("a")["title"]
    
    # පොතේ මිල ලබා ගැනීම
    price = book.find("p", class_="price_color").text
    
    # Stock තත්ත්වය ලබා ගැනීම
    availability = book.find("p", class_="instock availability").text.strip()
    
    # List එකට ඩේටා ටික එකතු කරගැනීම
    data.append({
        "Book Title": title,
        "Price": price,
        "Availability": availability
    })

# Pandas පාවිච්චි කරලා Dataframe එකක් හදාගැනීම
df = pd.DataFrame(data)

# CSV File එකක් ලෙස Save කිරීම
output_file = "books_data.csv"
df.to_csv(output_file, index=False, encoding="utf-8")

print(f"Scraping Completed Successfully! Data saved to {output_file}")