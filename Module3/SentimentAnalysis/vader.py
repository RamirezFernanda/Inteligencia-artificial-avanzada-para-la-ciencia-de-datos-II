
# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print(end=" ")

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")

    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")

    else:
        print("Neutral")


# Function that returns a list of strings that contains all the
# sentences in a txt file
def reading_dataset(dataset):
    lst = []
    f = open(dataset, "r")
    for line in f:
        lst.append(line.strip())
    return lst
