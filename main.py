from scraperengine import StartupScraper
import pandas as pd
import os

def main():
    URL = "http://books.toscrape.com/"
    CONFIG = {
        'container_tag': 'article',
        'container_class': 'product_pod',
        'title_tag': 'h3',
        'title_class': None 
    }
    
    scraper = StartupScraper(URL)
    soup = scraper.fetch_page(URL)
    
    if soup:
        data = scraper.parse_site(soup, **CONFIG)
        df = pd.DataFrame(data)
       
        if not os.path.exists('data'):
            os.makedirs('data')
        
        output_path = os.path.join('data', 'test_results.csv')
        df.to_csv(output_path, index=False)
        print(f"Success! Data saved to {output_path}")
    
if __name__ == "__main__":
    main()