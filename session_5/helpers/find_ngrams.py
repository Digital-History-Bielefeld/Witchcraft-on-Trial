from collections import Counter
from nltk.util import ngrams

def find_ngrams(tokens, n=2, top_k=10):
    n_grams = ngrams(tokens, n)
    ngram_counts = Counter(n_grams)
    return ngram_counts.most_common(top_k)
