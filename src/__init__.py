from scrape import WebScrape
from analyzer import Analyzer
import nltk

nltk.download('vader_lexicon')

try:
    w = WebScrape()
    w.run()
    filename = w.save()

    analyzer = Analyzer(filename)
except Exception as err:
    print(err)

# fig = px.bar(x=["positive", "neutral", "negative"], y=[pos, neu, neg])
# fig.write_html('first_figure.html', auto_open=True)
# print(analyzer.polarity_scores(w.articles[0].subtitle))
# print(analyzer.polarity_scores(w.articles[0].content))