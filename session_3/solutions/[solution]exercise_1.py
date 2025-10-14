import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    # Lowercase the text
    text_lower = text.lower()

    # Tokenize the text
    tokens = nltk.word_tokenize(text_lower)

    # Remove punctuation and non-alphabetic tokens
    tokens = [token for token in tokens if token.isalpha()]

    # Lemmatize the tokens
    lemmas = []
    for token in tokens:
        lemma = lemmatizer.lemmatize(token)
        lemmas.append(lemma)

    # Custom stopwords
    custom_stopwords = ['upon', 'thou', 'thy', 'thee'] # Add more as needed or leave the list blank, if you don't want any custom stopwords
    stop_words = stopwords.words('english')
    stop_words.extend(custom_stopwords)
    clean_tokens = []
    for token in lemmas:
        if token not in stop_words:
            clean_tokens.append(token)

    return clean_tokens

# Open and read the first text file
with open('../data/EAP_1.txt', 'r', encoding='utf-8') as file:
    first_text = file.read()

# Open and read the second text file
with open('../data/EAP_2.txt', 'r', encoding='utf-8') as file:
    second_text = file.read()

texts = [first_text, second_text]

# Preprocess the texts
for text in texts:
    preprocessed_text = preprocess_text(text)
    print("============")
    print("Preprocessed Text:")
    print(preprocessed_text)

