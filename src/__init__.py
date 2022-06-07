from scrape import WebScrape
from analyzer import Analyzer
import nltk

nltk.download('vader_lexicon')

try:
    w = WebScrape()
    w.run()
    filename = w.save()

    analyzer = Analyzer(filename)
    analyzer.show()
except Exception as err:
    print(err)