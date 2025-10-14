import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim import corpora
from gensim.models import LdaModel
import os
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------
# 1. Preprocessing setup
# ----------------------------
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()

def preprocess_text(text, custom_stopwords=[]):
    text_lower = text.lower()
    tokens = [token for token in nltk.word_tokenize(text_lower) if token.isalpha()]
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    stop_words = stopwords.words('english')
    stop_words.extend(custom_stopwords)
    clean_tokens = [token for token in lemmas if token not in stop_words]
    return clean_tokens

# ----------------------------
# 2. Load and preprocess data
# ----------------------------
folder_path = '../data/'
all_texts = []
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            all_texts.append(file.read())

custom_stops = ['wa', 'thou', 'thy', 'thee', 'upon']
all_tokens = [preprocess_text(text, custom_stopwords=custom_stops) for text in all_texts]

# ----------------------------
# 3. Build dictionary and corpus
# ----------------------------
dictionary = corpora.Dictionary(all_tokens)
corpus = [dictionary.doc2bow(tokens) for tokens in all_tokens]

# ----------------------------
# 4. Create LDA model
# ----------------------------
num_topics = 5
lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10)

# ----------------------------
# 5. Visualization functions
# ----------------------------
def plot_top_words_per_topic(lda_model, num_words=10):
    for topic_id, topic in lda_model.show_topics(num_topics=-1, num_words=num_words, formatted=False):
        words = [w for w, _ in topic]
        weights = [v for _, v in topic]
        plt.figure(figsize=(10, 5))
        plt.bar(words, weights, color='skyblue')
        plt.title(f"Top {num_words} Words for Topic {topic_id}")
        plt.xticks(rotation=45)
        plt.ylabel('Weight')
        plt.tight_layout()
        plt.savefig(f"topic_{topic_id}_top_words.png")
        plt.close()

def plot_topic_distribution_per_doc(lda_model, corpus, num_topics):
    """
    Visualize the topic proportions for each document as grouped bar charts (not stacked).
    Each document gets its own group of bars, one per topic.
    """
    import numpy as np
    import matplotlib.pyplot as plt

    # Get topic weights per document (ensure all topics included)
    doc_topics = [lda_model.get_document_topics(doc, minimum_probability=0) for doc in corpus]
    topic_distributions = np.array([[weight for _, weight in doc] for doc in doc_topics])

    # Setup
    num_docs = topic_distributions.shape[0]
    x = np.arange(num_docs)  # one position per document
    width = 0.8 / num_topics  # total width per group divided by number of topics

    plt.figure(figsize=(12, 6))

    # Plot one bar per topic (side-by-side)
    for topic_id in range(num_topics):
        plt.bar(
            x + topic_id * width,
            topic_distributions[:, topic_id],
            width=width,
            label=f"Topic {topic_id}"
        )

    plt.xlabel("Document")
    plt.ylabel("Topic Proportion")
    plt.title("Topic Distribution per Document")
    plt.xticks(x + width * (num_topics / 2 - 0.5), [f"Doc {i+1}" for i in range(num_docs)])
    plt.legend(title="Topics", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig("topic_distribution_per_doc_grouped.png")
    plt.show()


# ----------------------------
# 6. Run visualizations
# ----------------------------
plot_top_words_per_topic(lda_model, num_words=10)
plot_topic_distribution_per_doc(lda_model, corpus, num_topics)
