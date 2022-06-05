from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup


@dataclass
class Article:
    title: str
    subtitle: str
    time: str
    content: str


class WebScrape:

    def __init__(self) -> None:
        self.__site = "https://www.aljazeera.com"
        self.articles: dict[str, any] = {}

    def run(self, path='/where/mozambique/') -> None:
        main_page = requests.get(f"{self.__site}{path}")
        content = BeautifulSoup(main_page.content, 'html.parser')

        for article in content.find_all('article', class_='gc--type-post')[:10]:
            print(article.find('h3', class_='gc__title').get_text())
            print(self.scrape_article(article.find('h3', class_='gc__title').a['href']))

    def scrape_article(self, path: str):
        page = requests.get(f"{self.__site}{path}")
        content = BeautifulSoup(page.content, 'html.parser')
        header = content.find('header', class_='article-header')
        date = content.find('div', class_='article-dates').find_all('span')[1]

        paragraphs: list[str] = []
        for p in content.find('div', class_='wysiwyg').find_all('p'):
            paragraphs.append(p.get_text())

        return Article(header.h1.get_text(), header.p.get_text(), date.get_text(),
                       '\n'.join(paragraphs))


if __name__ == '__main__':
    w = WebScrape()
    w.run()