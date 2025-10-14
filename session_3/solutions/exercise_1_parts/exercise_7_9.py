import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()

with open('../data/EAP_1.txt', 'r', encoding='utf-8') as file:
    first_text = file.read()

# You can ignore the following line. It is just a more compact way of doing exercise 1.4, 1.5, and 1.6 in one line.
tokens = [token for token in nltk.word_tokenize(first_text.lower()) if token.isalpha()]

# Exercise 1.7
lemmas = []
for token in tokens:
    lemma = lemmatizer.lemmatize(token)
    lemmas.append(lemma)
print("Lemmatized Tokens:")
print(lemmas)

# Exercise 1.8
stop_words = stopwords.words('english')
clean_tokens = []
for token in lemmas:
    if token not in stop_words:
        clean_tokens.append(token)
print("Clean Tokens (No Stopwords):")
print(clean_tokens)

# Exercise 1.9
custom_stopwords = ['upon', 'thou', 'thy', 'thee'] # Add more as needed or leave the list blank, if you don't want any custom stopwords
stop_words.extend(custom_stopwords)
clean_tokens = []
for token in lemmas:
    if token not in stop_words:
        clean_tokens.append(token)
print("Clean Tokens (No Stopwords + Custom Stopwords):")
print(clean_tokens)
