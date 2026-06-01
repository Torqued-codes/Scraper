import pandas as pd
from scraperengine import StartupScraper

def main():
    # Example target: replace with the URL you want to scrape
    URL = "https://example-startup-listing-site.com" 
    
    scraper = StartupScraper(URL)
    soup = scraper.fetch_page(URL)
    
    if soup:
        data = scraper.parse_startups(soup)
        df = pd.DataFrame(data)
        
        # Save to data folder
        df.to_csv('data/scraped_startups.csv', index=False)
        print(f"Success! Scraped {len(df)} companies.")

if __name__ == "__main__":
    main()