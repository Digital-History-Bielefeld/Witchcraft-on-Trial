# Exercises

## Session 3 — Techniques for Text Analysis (for Historians)

---

### **Exercise 3 — Context Analysis with Word Frequency, N-Grams, and TF–IDF**

In this exercise, we will perform a context analysis of a text by finding the most common words, identifying common word combinations (n-grams), and calculating TF–IDF scores using the Gensim library. These techniques help us understand the themes and topics present in the text.

---

1. First, we need to install the Gensim library. You can do this by running the following command in your terminal:

   ```bash
   pip install --upgrade gensim
   ```

2. Now you can open the file `exercise_3.py`. In Exercise 1, we have preprocessed the text by lowercasing, tokenizing, lemmatizing, and removing stopwords. We will work with this preprocessed text for our context analysis. The file `exercise_3.py` already contains the preprocessing steps from Exercise 1, so you can start right there.
   You need to import the following modules after the existing import statements:

   ```python
   from collections import Counter
   from nltk.util import ngrams
   from gensim import corpora
   from gensim.models import TfidfModel
   import os
   ```

3. Next, we want to access our example text files. This time, we will load **all `.txt` files** from a folder (e.g. `../data/`) to later compare their vocabulary.

   ```python
   folder_path = '../data/'
   all_texts = []
   for filename in os.listdir(folder_path):
       if filename.endswith('.txt'):
           with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
               all_texts.append(file.read())
   ```

   Each element in the list `all_texts` now contains the text of one file.

4. In this exercise we want to look at the most common words and their contexts. We will start by defining a function called `word_frequency` that takes a list of tokens as input and returns the most common words in the text. You can use the `Counter` class from the `collections` module to count the occurrences of each word. The function should look like this:

   ```python
   def word_frequency(tokens, n=10):
       word_counts = Counter(tokens)
       return word_counts.most_common(n)
   ```

   The parameter `n` specifies how many of the most common words you want to return. You can call this function with the `clean_tokens` variable from Exercise 1 and print the result to see the most common words in the text.

5. Next, we will define a function called `find_ngrams` that takes a list of tokens and an integer `n` as input and returns the most common n-grams in the text. N-grams are contiguous sequences of `n` items from a given sample of text.

   ```python
   def find_ngrams(tokens, n=2, top_k=10):
       n_grams = ngrams(tokens, n)
       ngram_counts = Counter(n_grams)
       return ngram_counts.most_common(top_k)
   ```

   The parameter `n` specifies the size of the n-grams (e.g., 2 for bigrams, 3 for trigrams), and `top_k` specifies how many of the most common n-grams you want to return. You can call this function with the `clean_tokens` variable and print the result to see the most common bigrams in the text.

6. Finally, we will calculate the TF–IDF scores for the words in the texts. TF–IDF (Term Frequency–Inverse Document Frequency) is a statistical measure used to evaluate how important a word is in a document relative to a collection of documents (the corpus). It highlights words that occur frequently in one text but less often in others — thus identifying terms that are *characteristic* for a given document.

   Define a function called `find_top_tfidf_words` that takes a list of tokenized texts (`all_tokens`) and returns the top TF–IDF words for each document:

   ```python
   def find_top_tfidf_words(all_tokens, top_n=10):
       dictionary = corpora.Dictionary(all_tokens)
       corpus = [dictionary.doc2bow(tokens) for tokens in all_tokens]
       tfidf = TfidfModel(corpus)
       corpus_tfidf = tfidf[corpus]

       top_tfidf_per_doc = []
       for doc in corpus_tfidf:
           sorted_doc = sorted(doc, key=lambda x: x[1], reverse=True)
           top_terms = [(dictionary[term_id], round(score, 4)) for term_id, score in sorted_doc[:top_n]]
           top_tfidf_per_doc.append(top_terms)
       return top_tfidf_per_doc
   ```

   You can call this function after you have preprocessed all texts:

   ```python
   top_tfidf_words = find_top_tfidf_words(all_tokens, top_n=10)
   ```

   Optionally, you can define a helper function for formatted printing:

   ```python
   def print_tfidf_results(top_tfidf_words):
       for i, doc in enumerate(top_tfidf_words):
           print(f"\nTop TF–IDF words for document {i+1}:")
           for word, score in doc:
               print(f"  {word}: {score:.4f}")
   ```

   Then call:

   ```python
   print_tfidf_results(top_tfidf_words)
   ```

   The TF–IDF value shows how *distinctive* a word is for one text.

   * A **high TF–IDF score** means that the word appears often in this text but rarely in others. So it is likely to be more meaningful and characteristic for this document.
   * A **low TF–IDF score** means that the word appears frequently across all texts and is therefore less specific.

   Example: In a corpus of early modern letters, a word like *merchant* might have a high TF–IDF score in one text written by a trader but not in others — indicating a distinct topic or authorship.


So, what did we learned about the sources? 
- The most common words in the text give us an idea of the main themes and topics discussed. For example, if we see words like "witch," "trial," and "accused" frequently, it indicates that the text is likely about witch trials. However, this method simply counts the words without taking any other parameters into account.
- The n-grams help us identify common phrases or word combinations that might be significant in the context of the text. For example, if we find bigrams like "witch trial" or "accused witch," it suggests that these phrases are important in the narrative.
- The TF–IDF scores help us identify words that are particularly relevant to this specific text compared to others in the corpus. Words with high TF–IDF scores are likely to be more meaningful and specific to the content of the text, while common words with low scores may not provide much insight into the unique aspects of the document. This helps us to find special parts of the text that are not just common words but are more specific to the context of the document.
