import requests
from bs4 import BeautifulSoup
import pandas as pd

# අපි Lead Generation සෙවීම සඳහා පාවිච්චි කරන Test Directory එකක්
# (මෙහි උදාහරණයක් ලෙස Quotes වෙබ් අඩවියේ ඇති authors / tags පාවිච්චි කරමු, 
# Real-world වලදී මෙය YellowPages හෝ Business Directories වෙනස් කරනු ලැබේ)
url = "http://quotes.toscrape.com/"

print("Scraping business/lead data. Please wait...")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# වෙබ් අඩවියේ ඇති Tags ටික Leads/Keywords විදිහට එකතු කරගනිමු
tags = soup.find_all("a", class_="tag")

leads_data = []

for i, tag in enumerate(tags[:10], 1):
    tag_name = tag.text
    # Mock data ලෙස Lead එකක තොරතුරු සකස් කිරීම
    leads_data.append({
        "Lead ID": i,
        "Business/Keyword Name": tag_name,
        "Contact Number": f"+1-555-019{i}", # Simulated Lead Phone
        "Status": "Active"
    })

# Pandas හරහා CSV එකකට Export කිරීම
df = pd.DataFrame(leads_data)
output_file = "generated_leads.csv"
df.to_csv(output_file, index=False, encoding="utf-8")

print(f"\nLead Generation Completed Successfully!")
print(f"Total Leads Collected: {len(leads_data)}")
print(f"Data saved to {output_file}")