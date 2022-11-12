from SentimentAnalysis.vader import reading_dataset, sentiment_scores

# Driver code
if __name__ == "__main__":
    sentences = reading_dataset(
        'DataSets\Tiny_movie_reviews_dataset.txt')
    print("\nSentiment analysis results:")
    print("\n-----------------------------")
    print("\n-----------------------------")
    for sentence in sentences:
        sentiment_scores(sentence)
    print("\n-----------------------------")
    print("\n-----------------------------")
