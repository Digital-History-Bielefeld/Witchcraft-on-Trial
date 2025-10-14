import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()

def preprocess_text(text, custom_stopwords=[]):
    text_lower = text.lower()
    tokens = [token for token in nltk.word_tokenize(text_lower) if token.isalpha()]
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    stop_words = stopwords.words('english').extend(custom_stopwords)
    clean_tokens = [token for token in lemmas if token not in stop_words]
    return clean_tokens
