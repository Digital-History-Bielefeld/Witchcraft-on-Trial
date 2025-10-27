from gensim import corpora
from gensim.models import TfidfModel


def find_top_tfidf_words(all_tokens, top_n=10):
    dictionary = corpora.Dictionary(all_tokens)
    corpus = []
    for tokens in all_tokens:
        bag_of_words = dictionary.doc2bow(tokens)
        corpus.append(bag_of_words)
    tfidf = TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    
    top_tfidf_per_doc = []
    for doc in corpus_tfidf:
        sorted_doc = sorted(doc, key=lambda x: x[1], reverse=True)
        top_terms = [(dictionary[term_id], round(score, 4)) for term_id, score in sorted_doc[:top_n]]
        top_tfidf_per_doc.append(top_terms)
    return top_tfidf_per_doc
