import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import plotly.graph_objects as go


class Analyzer:

    def __init__(self, filename: str) -> None:

        analyzer = SentimentIntensityAnalyzer()
        df = pd.read_json(filename)
        title_scores: list[int] = []

        subtitle_scores: list[int] = []
        content_scores: list[int] = []
        for _, row in df.iterrows():
            title_scores.append(analyzer.polarity_scores(row['title'])['compound'])
            subtitle_scores.append(analyzer.polarity_scores(row['subtitle'])['compound'])
            content_scores.append(analyzer.polarity_scores(row['content'])['compound'])
        df['title_compound'] = title_scores
        df['subtitle_compound'] = subtitle_scores
        df['content_compound'] = content_scores

        self.df = df

    def show(self):
        fig = go.Figure(data=[
            go.Bar(name='Title', x=self.df['title'], y=self.df['title_compound']),
            go.Bar(name='Subtitle', x=self.df['title'], y=self.df['subtitle_compound']),
            go.Bar(name='Content', x=self.df['title'], y=self.df['content_compound']),
        ])
        fig.update_layout(
            title_text='News Sentiment',
            yaxis=dict(title='Polarity'),
            barmode='group',
            bargap=0.3,
            bargroupgap=0.0,
            legend=dict(
                x=0,
                y=1.0,
            ),
        )
        fig.show()

        # pd.options.plotting.backend = "plotly"
        # fig = self.df.plot(x="title",
        #                    y=["title_compound", "subtitle_compound", "content_compound"],
        #                    facet_row="variable",
        #                    kind="bar")
        # fig.show()
