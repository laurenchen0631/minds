import hashlib
import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from article import Article


class WebScrape:

    def __init__(self) -> None:
        self.__site = "https://www.aljazeera.com"
        self.articles: list[Article] = []

    def run(self, path='/where/mozambique/', n: int = 10) -> None:
        main_page = requests.get(f"{self.__site}{path}")
        content = BeautifulSoup(main_page.content, 'html.parser')

        # gc--type-post filters non-text articles
        for article in tqdm(content.find_all('article', class_='gc--type-post')[:n]):
            post = self.scrape_article(article.find('h3', class_='gc__title').a['href'])
            self.articles.append(post)

    def scrape_article(self, path: str):
        page = requests.get(f"{self.__site}{path}")
        content = BeautifulSoup(page.content, 'html.parser')
        header = content.find('header', class_='article-header')

        paragraphs: list[str] = []
        for p in content.find('div', class_='wysiwyg').find_all('p'):
            paragraphs.append(p.get_text())

        return Article(header.h1.get_text(), header.p.get_text(), '\n'.join(paragraphs))

    def save(self) -> str:
        json_str = json.dumps([e.to_json() for e in self.articles],
                              indent=4,
                              sort_keys=True,
                              ensure_ascii=False)
        filename = hashlib.md5(json_str.encode()).hexdigest() + '.json'
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(json_str)
        return filename
