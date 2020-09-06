from sentiment_analysis_spanish import sentiment_analysis
def analyze(text):
    sentiment = sentiment_analysis.SentimentAnalysisSpanish()
    result = sentiment.sentiment(text)
    return result
    if (result > 0.7):
        return 1
    if (result < 0.4):
        return -1
    else:
        return 0