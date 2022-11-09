import vader

# Driver code
if __name__ == "__main__":
    sentence = vader.reading_dataset('DataSets\Tiny_movie_reviews_dataset.txt')
    print("\nSentiment analysis results:")
    print("\n-----------------------------")
    print("\n-----------------------------")
    for i in sentence:
        vader.sentiment_scores(i)
    print("\n-----------------------------")
    print("\n-----------------------------")
