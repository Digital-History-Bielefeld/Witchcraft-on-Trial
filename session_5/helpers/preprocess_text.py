import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()


def preprocess_text(raw_text):
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

  custom_stopwords = ['upon', 'thou', 'thy', 'thee']
  stop_words = stopwords.words('english')
  stop_words.extend(custom_stopwords)

  clean_tokens = []
  for lemma in lemmas:
      if lemma not in stop_words:
          clean_tokens.append(lemma)
  
  return clean_tokens
