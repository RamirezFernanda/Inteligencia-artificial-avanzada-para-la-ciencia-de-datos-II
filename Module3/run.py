from SentimentAnalysis.vader import read_dataset, get_sentiment_scores
from TransModels.bleu import bleu_score

# Driver code
if __name__ == "__main__":
    sentences = read_dataset(
        'DataSets\Tiny_movie_reviews_dataset.txt')
    print("\nSentiment analysis results:")
    print("\n-----------------------------")
    for sentence in sentences:
        get_sentiment_scores(sentence)
    print("\n-----------------------------")
    print("\n-----------------------------")
    print("\nNER:")
    print("\n-----------------------------")
    print("hola")
    print("\n-----------------------------")
    print("\n-----------------------------")
    print("\nBleu Score:")
    print("\n-----------------------------")
    bleu_score()
    print("\n-----------------------------")
    print("\n-----------------------------")
