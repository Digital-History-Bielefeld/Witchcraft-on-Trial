# Exercises
## Session 3 — Techniques for Text Analysis (for Historians)

### Exercise 3 — Context Analysis with Word Frequency, N-Grams, and TF–IDF

In this exercise we perform a context analysis of one or more texts by identifying the most common words, extracting common word combinations (n-grams) using the NLTK library, and calculating TF–IDF scores using the Gensim library. These techniques help reveal the themes and topics present in the texts and highlight terms that are particularly characteristic of individual documents.
Gensim is a popular Python library for natural language processing, particularly known for its capabilities in topic modeling and document similarity analysis. You can find more information about Gensim and its documentation here: https://radimrehurek.com/gensim/. The documentation contains useful tutorials and examples to help you get started with the library. We will use Gensim to calculate TF–IDF scores for words in our texts, but if you want to explore more advanced features, the documentation is a great resource.
Additionally, we will use the NLTK library to extract n-grams from the texts. NLTK (Natural Language Toolkit) is a widely used library for natural language processing tasks in Python. It provides tools for tokenization, stemming, lemmatization, and more. You can find more information about NLTK and its documentation here: https://www.nltk.org/. The documentation includes tutorials and examples that can help you understand how to use the library effectively. You may notice, that it is a common practice to use multiple libraries together for different NLP tasks, as each library may have its own strengths and capabilities.

1. First, we need to install the Gensim library and the NLTK library. You can do this by running the following commands in your terminal:

```bash
pip install --upgrade gensim
```
```bash
pip install --user -U nltk
```
Now you have Gensim and NLTK installed in your Codespace and can use them in your Python scripts.


2. Now you can open the file `exercise_scripts/exercise_3.py`. In Exercise 1, we have preprocessed the text by lowercasing, tokenizing, lemmatizing, and removing stopwords. We will work with this preprocessed text for our context analysis. The file `exercise_3.py` already contains the preprocessing steps from Exercise 1, so you can start right there.

First, we want to access our example text files in the `data` folder. With digital methods, you typically work with a large number of documents, not just one. In the last exercises, we always called up the texts individually. If you are writing programs, you don't want to repeat yourself. We want to read in all texts in a folder and store them in a list. For this, we want to use the `os` module, which provides a way of using operating system-dependent functionality like reading files from directories. This step is necessary, because you need the right path to access the files in the `data` folder. The `os` module helps you to create these paths.
You can use the following code snippet to read all text files from the `data` folder and store their contents in a list:
```python
import os # Import the os module at the beginning of your script below the other imports
...

folder_path = './session_3/data/' # Path to the data folder 
all_texts = [] # Empty list to store the texts
for filename in os.listdir(folder_path): # Loop through all files in the folder
  with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file: # Open each file with the open() function
      all_texts.append(file.read()) # Read the content and append it to the list
```

This code will read all `.txt` files in the specified folder and store their contents in the `all_texts` list. Add it to your code and create a new variable `our_text`. We want to start with only one text for now. You can choose any text from the `all_texts` list. 
Here is how you can do it:

```python
our_text = all_texts[0]
```

You can play around with the index to access different texts in the list. For example, `our_text[0]` will give you the first text, `all_texts[1]` the second text, and so on.

3. Now we have a text, but we need to preprocess it first. You can reuse the preprocessing steps from Exercise 1. For this, we need to take the `our_text` variable and apply the preprocessing functions to it. It takes the text as input and returns a list of cleaned tokens.
Here is how you can do it:

```python
clean_tokens = preprocess_text(our_text)
```
You can then print the `clean_tokens` variable to see the preprocessed tokens with `print(clean_tokens)`. What do you think about the result? If you see words that have no meaning, like "thee" or "thy", you can add them as custom stopwords to the function and rerun your script. For example:
```python
custom_stopwords = ['thee', 'thy', 'thou'] # Add your custom stopwords here
clean_tokens = preprocess_text(our_text, custom_stopwords=custom_stopwords)
```

4. In this exercise we want to look at the most common words and their contexts. We will start by defining a function called `word_frequency` that takes a list of tokens as input and returns the most common words in the text. You can use the `Counter` class from the `collections` module to count the occurrences of each word. You can import it at the beginning of your script:
```python
from collections import Counter
```
This module can be used right away without installation, as it is part of the Python standard library.
Now, we want to define the `word_frequency` function. It should take a list of tokens as an argument and a top_n parameter to specify how many of the most common words to return. Here is how you can implement it:
```python
def word_frequency(tokens, top_n=10):
```
The list of tokens will be our preprocessed text `clean_tokens`. Inside the function, we can use the `Counter` class to count the occurrences of each word: `word_counts = Counter(tokens)`. And return the most common ones using the `most_common()` method: `word_counts.most_common(top_n)`. Here is the complete function:

```python
def word_frequency(tokens, top_n=10):
    word_counts = Counter(tokens)
    return word_counts.most_common(top_n)
```

You can call this function with the `clean_tokens` variable and print the result to see the most common words in the text:

```python
common_words = word_frequency(clean_tokens, top_n=10)
print(common_words)
```
You may notice that some words appear very frequently. These words can give us an idea of the main themes and topics discussed in the text. If you think some of the words are not meaningful, you can add them to the custom stopwords list and rerun the preprocessing step from Exercise 3.3. Play around with the `top_n` parameter and see how many common words you want to display.
Before proceeding to the next step, make sure to comment out or remove the print statement to avoid cluttering your output in the following steps.



5. Next, we will define a function called `find_ngrams` that takes a list of tokens and an integer `n` as input and returns the most common n-grams in the text. N-grams are contiguous sequences of `n` items from a given sample of text. For example, bigrams are 2-grams (pairs of words), and trigrams are 3-grams (triplets of words). So in other words, n-grams help us identify common phrases or word combinations that might be significant in the context of the text.
You can use the `ngrams` function from the `nltk.util` module to generate n-grams from the list of tokens. You can import it at the beginning of your script:
```python
from nltk.util import ngrams
```
Now, we want to define the `find_ngrams` function. It should take a list of tokens as an argument, an integer `n` to specify the size of the n-grams, and a `top_k` parameter to specify how many of the most common n-grams to return. Here is how you can implement it:
```python
def find_ngrams(tokens, n=2, top_k=10):
```
Inside the function, we can use the `ngrams` function from NLTK to generate n-grams from the list of tokens: `n_grams = ngrams(tokens, n)`. Then, we can use the `Counter` class to count the occurrences of each n-gram: `ngram_counts = Counter(n_grams)`. Finally, we return the most common n-grams using the `most_common()` method: `ngram_counts.most_common(top_k)`. Here is the complete function:

```python
def find_ngrams(tokens, n=2, top_k=10):
    n_grams = ngrams(tokens, n)
    ngram_counts = Counter(n_grams)
    return ngram_counts.most_common(top_k)
```
You can call this function with the `clean_tokens` variable and print the result to see the most common n-grams in the text:

```python
common_bigrams = find_ngrams(clean_tokens, n=2, top_k=10)
print(common_bigrams)
```
You can change the `n` parameter to find trigrams or higher-order n-grams. For example, to find the most common trigrams, you can call the function like this:

```python
common_trigrams = find_ngrams(clean_tokens, n=3, top_k=10)
print(common_trigrams)
```

Before proceeding to the next step, make sure to comment out or remove the print statement to avoid cluttering your output in the following steps.


6. Finally, we will calculate the TF–IDF scores for the words in the texts. TF–IDF (Term Frequency–Inverse Document Frequency) is a statistical measure used to evaluate how important a word is in a document relative to a collection of documents (the corpus). It highlights words that occur frequently in one text but less often in others — thus identifying terms that are *characteristic* for a given document.
First, we need to import the necessary modules from Gensim. You can add the following imports at the beginning of your script:
```python
from gensim import corpora
from gensim.models import TfidfModel
```

Define a function called `find_top_tfidf_words` that takes a list of tokenized texts (`all_tokens`) and returns the top TF–IDF words for each document:
```python
def find_top_tfidf_words(all_tokens, top_n=10):
```
Next, we want to create a Gensim dictionary and corpus from the tokenized texts, and then compute the TF–IDF scores. You don't need to worry about the details of how TF–IDF works internally; Gensim handles that for us. But here is how you can implement the function step by step:
Inside the function, we first need to create a Gensim dictionary from the tokenized texts: `dictionary = corpora.Dictionary(all_tokens)`. This dictionary maps each unique word to a unique integer ID. Then we create  an empty list called `corpus` to store the bag-of-words representation of each document. We loop through each list of tokens in `all_tokens`, convert it to a bag-of-words format using the dictionary, and append it to the `corpus` list:
```python
corpus = []
for tokens in all_tokens:
    bag_of_words = dictionary.doc2bow(tokens)
    corpus.append(bag_of_words)
```
Next, we create a TF–IDF model using the corpus: `tfidf = TfidfModel(corpus)`. We then apply the TF–IDF model to the corpus to get the TF–IDF representation of each document: `corpus_tfidf = tfidf[corpus]`. The function part should now look like this:
```python
def find_top_tfidf_words(all_tokens, top_n=10):
    dictionary = corpora.Dictionary(all_tokens)
    corpus = []
    for tokens in all_tokens:
        bag_of_words = dictionary.doc2bow(tokens)
        corpus.append(bag_of_words)
    tfidf = TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
``` 
Now, we want to extract the top TF–IDF words for each document. We can loop through each document in `corpus_tfidf`, sort the terms by their TF–IDF scores in descending order, and select the top `top_n` terms. We can then convert the term IDs back to words using the dictionary and store the results in a list:

```python
top_tfidf_per_doc = [] # Empty list to store top TF–IDF words for each document
for doc in corpus_tfidf: # Loop through each document
    sorted_doc = sorted(doc, key=lambda x: x[1], reverse=True) # Sort terms by TF–IDF score
    top_terms = [(dictionary[term_id], round(score, 4)) for term_id, score in sorted_doc[:top_n]] # Get top n terms and convert IDs to words
    top_tfidf_per_doc.append(top_terms) # Append to the results list
return top_tfidf_per_doc # Return the list of top TF–IDF words for each document
```
Here is the complete `find_top_tfidf_words` function:
```python
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
```

You can call this function now with the list of all tokenized texts. For this you need to preprocess all texts in the `all_texts` list first. You can do this by using a for loop:
```python
all_tokens = []
for text in all_texts:
    tokens = preprocess_text(text)
    all_tokens.append(tokens)
```
Now you can call the `find_top_tfidf_words` function with the `all_tokens` variable and print the result to see the top TF–IDF words for each document:

```python
top_tfidf_words = find_top_tfidf_words(all_tokens, top_n=10)
print(top_tfidf_words[0])  # Print top TF–IDF words for the first document
```
The output will show you the words with the highest TF–IDF scores in the first document, along with their scores. You can play around with the `top_n` parameter to see more or fewer words and look at other documents by changing the index in `top_tfidf_words`. You can also add custom stopwords to the preprocessing step if you notice that some common words are appearing in the TF–IDF results:
```python
custom_stopwords = ['thee', 'thy', 'thou'] # Add your custom stopwords here
all_tokens = []
for text in all_texts:
    tokens = preprocess_text(text, custom_stopwords=custom_stopwords) # Add custom stopwords variable here
    all_tokens.append(tokens)
```

The TF–IDF value shows how *distinctive* a word is for one text. 

* A **high TF–IDF score** means that the word appears often in this text but rarely in others. So it is likely to be more meaningful and characteristic for this document. The highest score is 1.0.
* A **low TF–IDF score** means that the word appears frequently across all texts and is therefore less specific. The lowest score is 0.0.

Example: In a corpus of early modern letters, a word like *merchant* might have a high TF–IDF score in one text written by a trader but not in others — indicating a distinct topic or authorship. Our example corpus is too small to see big differences, but in larger corpora, this method is very useful to identify characteristic terms.


So, what did we learned about the sources? 
- The most common words in the text give us an idea of the main themes and topics discussed. For example, if we see words like "witch," "trial," and "accused" frequently, it indicates that the text is likely about witch trials. However, this method simply counts the words without taking any other parameters into account.
- The n-grams help us identify common phrases or word combinations that might be significant in the context of the text. For example, if we find bigrams like "witch trial" or "accused witch," it suggests that these phrases are important in the narrative.
- The TF–IDF scores help us identify words that are particularly relevant to this specific text compared to others in the corpus. Words with high TF–IDF scores are likely to be more meaningful and specific to the content of the text, while common words with low scores may not provide much insight into the unique aspects of the document. This helps us to find special parts of the text that are not just common words but are more specific to the context of the document.
