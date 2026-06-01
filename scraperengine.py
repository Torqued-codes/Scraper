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

    def parse_startups(self, soup):
        # REPLACE these tags with the actual HTML tags from your target site
        startups = []
        cards = soup.find_all('div', class_='listing-item') 
        for card in cards:
            name = card.find('h3').text.strip() if card.find('h3') else "N/A"
            industry = card.find('p', class_='industry').text.strip() if card.find('p', class_='industry') else "N/A"
            startups.append({'Company': name, 'Industry': industry})
        return startups