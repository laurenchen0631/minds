from scrape import WebScrape
from analyzer import Analyzer
import nltk
import time

nltk.download('vader_lexicon')

start = now = time.process_time()


def measure_time(label: str, from_beginning=False) -> None:
    global now
    t = time.process_time()
    print(f'{label}: {t - (start if from_beginning else now):.4f}s')
    now = t


try:
    w = WebScrape()
    w.run()
    measure_time('Web Scraping')
    filename = w.save()
    measure_time('Save JSON')

    analyzer = Analyzer(filename)
    measure_time('Sentiment Analysis')

    analyzer.show()
    measure_time('Data Visualization')
    print('------------------------------')
    measure_time('Operation time', from_beginning=True)

except Exception as err:
    print(err)
