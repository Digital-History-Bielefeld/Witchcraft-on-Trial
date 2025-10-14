import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim import corpora
from gensim.models import LdaModel
import os

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
