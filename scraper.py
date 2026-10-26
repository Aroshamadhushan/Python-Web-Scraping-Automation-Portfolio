import requests
from bs4 import BeautifulSoup

# අපි Scrape කරන්න ගන්න පුංචි test website එකක්
url = "https://quotes.toscrape.com/"

# 1. Website එකට HTTP Request එකක් යැවීම
response = requests.get(url)
print(f"Status Code: {response.status_code}") # 200 ආවොත් වැඩේ සාර්ථකයි

# 2. HTML Content එක Parse කිරීම
soup = BeautifulSoup(response.text, "html.parser")

# 3. වෙබ් අඩවියේ තියෙන Quotes (කියමන්) ටික සොයා ගැනීම
quotes = soup.find_all("div", class_="quote")

print("\n--- Scraped Quotes ---")
for i, q in enumerate(quotes[:5], 1):  # මුල් Quotes 5 විතරක් පෙන්වමු
    text = q.find("span", class_="text").text
    author = q.find("small", class_="author").text
    print(f"{i}. {text} - **{author}**")