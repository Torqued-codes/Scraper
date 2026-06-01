import requests
from bs4 import BeautifulSoup

class StartupScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    def fetch_page(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page: {e}")
            return None

    def parse_books(self, soup):
        books = []
        
        items = soup.find_all('article', class_='product_pod')
        
        for item in items:
            # Extracting specific data points
            title = item.h3.a['title']
            price = item.find('p', class_='price_color').text
            books.append({'Title': title, 'Price': price})
            
        return books