import pandas as pd
from article import Article
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class Analyzer:

    def __init__(self, filename: str) -> None:
        analyzer = SentimentIntensityAnalyzer()
        df = pd.read_json(filename)
        title_scores: list[int] = []

        subtitle_scores: list[int] = []
        content_scores: list[int] = []
        for i, row in df.iterrows():
            title_scores.append(analyzer.polarity_scores(row['title'])['compound'])
            subtitle_scores.append(analyzer.polarity_scores(row['subtitle'])['compound'])
            content_scores.append(analyzer.polarity_scores(row['content'])['compound'])
        self.df = df