from pysentimiento import SentimentAnalyzer, EmotionAnalyzer


"""
Sentiment Analysis
"""
analyzer = SentimentAnalyzer(lang="en")
res = analyzer.predict("i love you")
print(res.output)


"""
Emotion Analysis
"""
# emotion_analyzer = EmotionAnalyzer(lang="en")
# res = emotion_analyzer.predict("fuck off")
# print(res.output)
