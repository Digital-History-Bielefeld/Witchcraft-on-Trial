import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os
from collections import Counter
from nltk.util import ngrams
from gensim import corpora
from gensim.models import TfidfModel
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()

def preprocess_text(raw_text, custom_stopwords=[]):
    text = raw_text.lower()
    tokens_full = nltk.word_tokenize(text)
    tokens= []
    for token in tokens_full:
        if token.isalpha():
            tokens.append(token)
    lemmas = []
    for token in tokens:
        lemma = lemmatizer.lemmatize(token)
        lemmas.append(lemma)
    stop_words = stopwords.words('english')
    stop_words.extend(custom_stopwords)
    clean_tokens = []
    for lemma in lemmas:
        if lemma not in stop_words:
            clean_tokens.append(lemma) 
    return clean_tokens

def word_frequency(tokens, top_n=10):
    word_counts = Counter(tokens)
    return word_counts.most_common(top_n)

def find_ngrams(tokens, n=2, top_k=10):
    n_grams = ngrams(tokens, n)
    ngram_counts = Counter(n_grams)
    return ngram_counts.most_common(top_k)

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

folder_path = './session_4/data/'
all_texts = [] 
for filename in os.listdir(folder_path):
  with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file: 
      all_texts.append(file.read())

our_text = all_texts[0]
custom_stopwords = ['thee', 'thy', 'thou', "wa", "made"]
clean_tokens = preprocess_text(our_text, custom_stopwords=custom_stopwords)

all_tokens = []
for text in all_texts:
    tokens = preprocess_text(text, custom_stopwords=custom_stopwords)
    all_tokens.append(tokens)

most_common_words = word_frequency(clean_tokens, top_n=10)
most_common_bigrams = find_ngrams(clean_tokens, n=2, top_k=10)
most_common_trigrams = find_ngrams(clean_tokens, n=3, top_k=10)
top_tfidf_words = find_top_tfidf_words(all_tokens, top_n=8)

# ----------------------------
# Write your code below
# ----------------------------

words, counts = zip(*most_common_words)

def plot_bar_chart(words, counts, title):
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{title.replace(' ', '_').lower()}.png")

def generate_word_cloud(tokens, filename="word_cloud.png"):
   text = ' '.join(tokens)  # Join the tokens into a single string
   wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

   # Display the word cloud using Matplotlib
   plt.figure(figsize=(10, 5))
   plt.imshow(wordcloud, interpolation='bilinear')
   plt.axis('off')  # Hide the axes
   plt.title('Word Cloud of Most Common Words')
   plt.tight_layout()
   plt.savefig(filename)

# Plot the most common words of the first text
words, counts = zip(*most_common_words)
# plot_bar_chart(words, counts, 'Most Common Words in the Text')

# Plot the most common bigrams of the first text
bigram_words, bigram_counts = zip(*most_common_bigrams)
bigram_words = [' '.join(bigram) for bigram in bigram_words]
# plot_bar_chart(bigram_words, bigram_counts, 'Most Common Bigrams in the Text')

# Plot the most common trigrams of the first text
trigram_words, trigram_counts = zip(*most_common_trigrams)
trigram_words = [' '.join(trigram) for trigram in trigram_words]
# plot_bar_chart(trigram_words, trigram_counts, 'Most Common Trigrams in the Text')

tfidf_words, tfidf_scores = zip(*top_tfidf_words[0])
plot_bar_chart(tfidf_words, tfidf_scores, 'Top TF-IDF Words in the Text')

# Plot the top TF-IDF words of the second text
tfidf_words, tfidf_scores = zip(*top_tfidf_words[1])
plot_bar_chart(tfidf_words, tfidf_scores, 'Top TF-IDF Words in the Second Text')


generate_word_cloud(all_tokens[0], filename="first_text_wordcloud.png")
