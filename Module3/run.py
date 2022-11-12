import vader

# Driver code
if __name__ == "__main__":
    sentences = vader.reading_dataset(
        'DataSets\Tiny_movie_reviews_dataset.txt')
    print("\nSentiment analysis results:")
    print("\n-----------------------------")
    print("\n-----------------------------")
    for sentence in sentences:
        vader.sentiment_scores(sentence)
    print("\n-----------------------------")
    print("\n-----------------------------")
