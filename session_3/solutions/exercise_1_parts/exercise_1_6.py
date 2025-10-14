import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

with open('../data/EAP_1.txt', 'r', encoding='utf-8') as file:
    first_text = file.read()

# Exercise 1.4
text = first_text.lower()
print("Lowercased Text:")
print(text)

# Exercise 1.5
tokens = nltk.word_tokenize(text)
print("Tokenized Text:")
print(tokens)

# Exercise 1.6
for token in tokens:
    if not token.isalpha():
        tokens.remove(token)
print("Alphabetic Tokens:")
print(tokens)
