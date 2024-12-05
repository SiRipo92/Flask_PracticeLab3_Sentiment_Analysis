from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

#Create the unit test class
class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Test case for positive sentiment
        result_1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(result_1['label'], 'positive')

        # Test case for negative sentiment
        result_2 = sentiment_analyzer("I hate working with Python")
        self.assertEqual(result_2['label'], 'negative')

        # Test case for neutral sentiment
        result_3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(result_3['label'], 'neutral')

unittest.main()