import sys

from pysentimiento import SentimentAnalyzer, EmotionAnalyzer

def get_sentiment(text: str):
    """ Sentiment Analysis -> Returns Union['POS', 'NEG']
    """
    analyzer = SentimentAnalyzer(lang="en")
    return analyzer.predict(text).output


def get_emotion(text: str):
    """ Emotion Analysis -> Return Union['Angry', 'Happy', 'Sad']
    """
    emotion_analyzer = EmotionAnalyzer(lang="en")
    return emotion_analyzer.predict(text).output


if len(sys.argv) > 1:
    if sys.argv[1] == "--help":
        print("Usage: python bertweet.py [option]")
        print("Options:")
        print("  --help: Show this help message")
        print("  --sentiment: Classify sentiment in text")
        print("  --emotion: Classify emotion in text")
    
    filename = sys.argv[-1]
    if len(sys.argv) > 1:
        filename = sys.argv[-1]
        for i in range(len(sys.argv) - 1):
            if sys.argv[i] == "--sentiment":
                f = open("sentiment.txt", "w")
                f.write(get_sentiment(sys.argv[len(sys.argv) - 1]))
                f.close()
            elif sys.argv[i] == "--emotion":
                f = open("emotion.txt", "w")
                f.write(get_emotion(sys.argv[len(sys.argv) - 1]))
                f.close()