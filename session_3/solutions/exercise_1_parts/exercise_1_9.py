import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os

nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()


folder_path = './session_3/data/'
all_texts = []
for filename in os.listdir(folder_path):
  with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
      all_texts.append(file.read())

our_text = all_texts[0]

text = our_text.lower()
#print(text)

tokens_full = nltk.word_tokenize(text)
#print(tokens_full)

tokens= []
for token in tokens_full:
    if token.isalpha():
        tokens.append(token)
# print(tokens)

lemmas = []
for token in tokens:
    lemma = lemmatizer.lemmatize(token)
    lemmas.append(lemma)
# print(lemmas)

custom_stopwords = ["wa", "e", "said"]
stop_words = stopwords.words('english')
stop_words.extend(custom_stopwords)

clean_tokens = []
for lemma in lemmas:
    if lemma not in stop_words:
        clean_tokens.append(lemma)
print((clean_tokens))
