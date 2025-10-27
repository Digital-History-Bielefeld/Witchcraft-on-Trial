from collections import Counter

def word_frequency(tokens, top_n=10):
    word_counts = Counter(tokens)
    return word_counts.most_common(top_n)
