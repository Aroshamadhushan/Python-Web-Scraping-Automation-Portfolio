from playwright.sync_api import sync_playwright

def run_dynamic_scraper():
    with sync_playwright() as p:
        # Browser එක Open කිරීම (headless=False දුන්නොත් බ්‍රව්සර් එක වැඩ කරනවා අපිට බලාගන්න පුළුවන්)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("Navigating to the website...")
        # Dynamic JavaScript website එකකට යාම
        page.goto("https://quotes.toscrape.com/js/")
        
        # Quotes ටික Page එකට Load වෙනකම් පුංචි වෙලාවක් බලා සිටීම
        page.wait_for_selector(".quote")
        
        # සියලුම quote elements සොයා ගැනීම
        quotes = page.locator(".quote").all()
        
        print("\n--- Dynamically Scraped Quotes ---")
        for i, quote in enumerate(quotes[:5], 1):  # මුල් 5 පෙන්වමු
            text = quote.locator(".text").inner_text()
            author = quote.locator(".author").inner_text()
            print(f"{i}. {text} - {author}")
            
        browser.close()
        print("\nDynamic Scraping Completed Successfully!")

if __name__ == "__main__":
    run_dynamic_scraper()