import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
nltk.download("punkt")
nltk.download("stopwords")

def extractive_summarization(text, num_sentences=5):
    """Performs extractive text summarization."""
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Get English stopwords
    stop_words = set(stopwords.words("english"))

    # Tokenize words and remove stopwords
    words = [
        word.lower()
        for sentence in sentences
        for word in word_tokenize(sentence)
        if word.isalnum() and word.lower() not in stop_words
    ]

    # Compute word frequencies
    word_freq = nltk.FreqDist(words)

    # Compute sentence scores
    sentence_scores = {
        i: sum(word_freq[word] for word in word_tokenize(sentence.lower()) if word in word_freq)
        for i, sentence in enumerate(sentences)
    }

    # Select top-scoring sentences
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

    # Generate summary
    summary = " ".join([sentences[i] for i in sorted(summary_sentences)])

    return summary
