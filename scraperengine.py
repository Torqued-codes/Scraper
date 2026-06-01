import requests
from bs4 import BeautifulSoup


class StartupScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def fetch_page(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"Error: {e}")
            return None

    def parse_site(self, soup, container_tag, container_class, title_tag, title_class):
        results = []
        items = soup.find_all(container_tag, class_=container_class)
        
        for item in items:
            
            title = item.find(title_tag, class_=title_class).text.strip()
            results.append({'Title': title})
            
            
        return results