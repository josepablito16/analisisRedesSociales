from sentiment_analysis_spanish import sentiment_analysis
def analyze(text):
    sentiment = sentiment_analysis.SentimentAnalysisSpanish()
    result = sentiment.sentiment(text)
    return result