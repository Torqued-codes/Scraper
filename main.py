import pandas as pd
import os
from scraperengine import StartupScraper

def main():
    URL = "http://books.toscrape.com/"
    
    if not os.path.exists('data'):
        os.makedirs('data')
        
    scraper = StartupScraper(URL)
    soup = scraper.fetch_page(URL)
    
    if soup:
        data = scraper.parse_books(soup)
        df = pd.DataFrame(data)
        
        # Save to data folder
        df.to_csv('data/test_results.csv', index=False)
        print(f"Success! Scraped {len(df)} items to data/test_results.csv")

if __name__ == "__main__":
    main()