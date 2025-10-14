import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
from nltk.util import ngrams
from gensim import corpora
from gensim.models import TfidfModel
import os

# Download necessary NLTK data
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()

# ----------------------------
# 1. Preprocessing function
# ----------------------------
def preprocess_text(text, custom_stopwords=[]):
    text_lower = text.lower()
    tokens = [token for token in nltk.word_tokenize(text_lower) if token.isalpha()]
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    stop_words = stopwords.words('english')
    stop_words.extend(custom_stopwords)
    clean_tokens = [token for token in lemmas if token not in stop_words]
    return clean_tokens


# ----------------------------
# 2. Frequency-based functions
# ----------------------------
def word_frequency(tokens, n=10):
    """Return n most common words and their counts."""
    word_counts = Counter(tokens)
    return word_counts.most_common(n)


def find_ngrams(tokens, n=2, top_k=10):
    """Return top_k most common n-grams."""
    n_grams = ngrams(tokens, n)
    ngram_counts = Counter(n_grams)
    return ngram_counts.most_common(top_k)


# ----------------------------
# 3. TF–IDF analysis
# ----------------------------
def find_top_tfidf_words(all_tokens, top_n=10):
    """
    Compute TF–IDF for all documents and return the top n words per text.
    Returns a list of lists: one sublist with (word, score) tuples per document.
    """
    dictionary = corpora.Dictionary(all_tokens)
    corpus = [dictionary.doc2bow(tokens) for tokens in all_tokens]
    tfidf = TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    top_tfidf_per_doc = []
    for doc in corpus_tfidf:
        sorted_doc = sorted(doc, key=lambda x: x[1], reverse=True)
        top_terms = [(dictionary[term_id], round(score, 4)) for term_id, score in sorted_doc[:top_n]]
        top_tfidf_per_doc.append(top_terms)
    return top_tfidf_per_doc


# Optional helper for pretty printing
def print_tfidf_results(top_tfidf_words):
    for i, doc in enumerate(top_tfidf_words):
        print(f"\nTop TF–IDF words for document {i+1}:")
        for word, score in doc:
            print(f"  {word}: {score:.4f}")


# ----------------------------
# 4. Load data
# ----------------------------
folder_path = '../data/'
all_texts = []
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            all_texts.append(file.read())

# Preprocess all texts
custom_stops = ['wa', 'thou', 'thy', 'thee', 'upon']
all_tokens = [preprocess_text(text, custom_stopwords=custom_stops) for text in all_texts]
clean_tokens_first_text = all_tokens[0]


# ----------------------------
# 5. Call all analyses uniformly
# ----------------------------
most_common_words = word_frequency(clean_tokens_first_text, n=20)
most_common_bigrams = find_ngrams(clean_tokens_first_text, n=4, top_k=20)
top_tfidf_words = find_top_tfidf_words(all_tokens, top_n=10)

# Example output (uncomment for testing)
# print("Most Common Words:", most_common_words)
# print("Most Common 4-grams:", most_common_bigrams)
# print_tfidf_results(top_tfidf_words)

# ----------------------------
# Write your code below
# ----------------------------
