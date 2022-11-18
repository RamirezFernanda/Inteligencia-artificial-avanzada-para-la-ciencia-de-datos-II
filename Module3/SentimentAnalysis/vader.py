
# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# function to print sentiments
# of the sentence.
def get_sentiment_scores(sentence):

    # Create a SentimentIntensityAnalyzer object.
    analyzer = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = analyzer.polarity_scores(sentence)

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")

    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")

    else:
        print("Neutral")


# Function that returns a list of strings that contains all the
# sentences in a txt file
def read_dataset(dataset):  # function names should almost always start with verbs :) 
    results = []
    # you should use the "with" construction mentioned here: https://www.programiz.com/python-programming/file-operation
    # so that the file is automatically closed. right now, you are leaving it open!
    f = open(dataset, "r")
    for line in f:
        results.append(line.strip())
    return results
