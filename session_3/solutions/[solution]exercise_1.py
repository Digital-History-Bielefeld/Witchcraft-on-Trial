import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os

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


folder_path = './session_3/data/'
all_texts = []
for filename in os.listdir(folder_path):
  with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
      all_texts.append(file.read())

our_text = all_texts[0]
preprocessed_text = preprocess_text(our_text)
#print(preprocessed_text)

second_text = all_texts[1]
preprocessed_second_text = preprocess_text(second_text)
#print(preprocessed_second_text)

for text in all_texts:
    processed = preprocess_text(text)
    print("----- New Document -----")
    print(processed)
    print("\n")
    print("----- End Document -----")
