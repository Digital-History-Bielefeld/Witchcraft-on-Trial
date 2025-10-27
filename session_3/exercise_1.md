# Exercises
## Session 3 — Techniques for Text Analysis (for Historians)


### Exercise 1 — Text Preprocessing with NLTK

We will start with a simple text preprocessing procedure using the NLTK library. The goal is to prepare the text by tokenizing, stemming, lemmatizing, and removing stopwords.
NLTK (Natural Language Toolkit) is a powerful library for natural language processing in Python. It provides easy-to-use interfaces to over 50 corpora and lexical resources, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning. You can have a look at the [official NLTK documentation](https://www.nltk.org/) for more information. There you find installation instructions, tutorials, and guides on how to use the library. 

1. First of all, we want to install the NLTK library. Type the following command in your terminal:

```
pip install --user -U nltk
```
After the installation process, NLTK is ready to use in your codespace.


2. Now you can open the file `exercise_scripts/exercise_1.py`. There you need to import the necessary NLTK modules and download the required resources (like punkt and stopwords). You can do this by adding the following lines at the beginning of your script:
```python
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')
```
First you need to import the NLTK library itself to access all its functions. Then, you import the `stopwords` module from the `nltk.corpus` package to access the list of stopwords. Finally, you import the `WordNetLemmatizer` class from the `nltk.stem` package to perform lemmatization. The `nltk.download()` function is used to download the necessary resources for tokenization, lemmatization, and stopword removal.


3. Next, we want to access our example text files in the `data` folder. With digital methods, you typically work with a large number of documents, not just one. In the last exercises, we always called up the texts individually. If you are writing programs, you don't want to repeat yourself. We want to read in all texts in a folder and store them in a list. For this, we want to use the `os` module, which provides a way of using operating system-dependent functionality like reading files from directories. This step is necessary, because you need the right path to access the files in the `data` folder. The `os` module helps you to create these paths.
You can use the following code snippet to read all text files from the `data` folder and store their contents in a list:
```python
import os # Import the os module at the beginning of your script
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


4. Now we can work with the text. To analyse the text, we need to preprocess it first. The preprocessing steps include:
   - Lowercasing the text
   - Tokenizing the text into words
   - Lemmatizing the tokens
   - Removing stopwords

Let's start with lowercasing the text. You can do this by using the `.lower()` method on the text variable. You  can find more information about this method in session 2. Save the result in a variable called `text`. Print the content of the variable to see if it worked.
```python
text = our_text.lower()
```
You should now see the entire text in lowercase letters in your terminal. Before proceeding to the next step, make sure to comment out or remove the print statement to avoid cluttering your output in the following steps.


5. Next, we will tokenize the text into words. You can use the `nltk.word_tokenize()` function for this. Pass the lowercased text to this function (which means, you should write the variable name `text` in the parentheses) and save the result in a variable called `tokens`. Print the content of the variable to see if it worked.
```python
tokens_full = nltk.word_tokenize(text)
```

6. Now we have a list of tokens, but it also contains punctuation and special characters. We want to keep only the alphabetic tokens. You can filter out non-alphabetic tokens. The method `.isalpha()` can be used to check if a token is alphabetic. Update the `tokens` variable to contain only alphabetic tokens. It should look like this:
```python
tokens = []
for token in tokens_full:
    if token.isalpha():
        tokens.append(token)

# or the shorter version with list comprehension:
tokens = [token for token in tokens_full if token.isalpha()]
```
Print the content of the variable to see if it worked. Before proceeding to the next step, make sure to comment out or remove the print statement to avoid cluttering your output in the following steps.


7. Next, we will lemmatize the tokens using the WordNet Lemmatizer. First, create an instance of the `WordNetLemmatizer` class. This means you need to write `lemmatizer = WordNetLemmatizer()` to create a lemmatizer object with which you can lemmatize words, like dogs to dog, running to run, etc. This part of code should also be placed after the `nltk.download('stopwords')` line. It is a good practice to put all the imports and initializations at the beginning of your script.
Next, create a new empty list called `lemmas` at the end of your script. Then, use a for loop to iterate over the `tokens` list and apply the `lemmatizer.lemmatize()` method to each token. Append the lemmatized tokens to the `lemmas` list. Print the content of the `lemmas` variable to see if it worked.
This should look like this:
```python
lemmatizer = WordNetLemmatizer()

...

lemmas = []
for token in tokens:
    lemma = lemmatizer.lemmatize(token)
    lemmas.append(lemma)
```

Now you should see the lemmatized tokens in your terminal. Before proceeding to the next step, make sure to comment out or remove the print statement to avoid cluttering your output in the following steps.

8. Finally, we will remove stopwords from the lemmatized tokens. You can use the `stopwords.words('english')` function to get a list of English stopwords. Save `stopwords.words('english')` in a variable called `stop_words`.
Create a new empty list called `clean_tokens`. Then, use a for loop to iterate over the `lemmas` list and check if each token is not in the stopwords list. If it is not a stopword, append it to the `clean_tokens` list. Print the content of the `clean_tokens` variable to see if it worked.
This should look like this:
```python
stop_words = stopwords.words('english')
clean_tokens = []
for lemma in lemmas:
    if lemma not in stop_words:
        clean_tokens.append(lemma)
```

You should now see the list of clean tokens without stopwords in your terminal. If you are interested, you can print out the stopword list with:
```python
print(stop_words)
```
You may notice that the list contains common words like "the", "is", "in", etc. These words are often removed in text analysis because they do not carry significant meaning. But the list is for modern English texts. Since we are working with historical texts, some words might not be relevant for our analysis. 

9. Sometimes you want to add custom stopwords that are specific to your text. You can create a list of custom stopwords and extend the existing stopwords list with it. For example:
```python
custom_stopwords = ['said', 'one', 'like'] # Add your custom stopwords here
stop_words = stopwords.words('english') # Get the default stopwords
stop_words.extend(custom_stopwords) # Extend the stopwords list with custom stopwords
```
Try it out by adding some words that you think are not useful for the analysis of our example text. Create the `custom_stopwords` list and extends your existing `stop_words` list with it before the for loop where you create the `clean_tokens` list. Then, run the code again and see how the `clean_tokens` list changes.


10. As a last step, we want to make our code more reusable. Therefore, we will wrap the preprocessing steps into a function called `preprocess_text()`. This function should take a text string `raw_text`as input and return the list of clean tokens. You can copy your code from the previous steps and paste it into the function. Make sure to indent the code correctly so that it is part of the function. The function should look like this:
```python
def preprocess_text(text):
    # Your preprocessing code here
    return clean_tokens
```
The steps of the functiions should be the following:
- Lowercase the input text
- Tokenize the text into words
- Filter out non-alphabetic tokens
- Lemmatize the tokens
- Remove stopwords (including custom stopwords)

Finally, call the function with `our_text` as an argument and save the result in a variable called `processed_text`. Print the content of the `processed_text` variable to see if it worked. 


11. With the function in place, you can easily preprocess any text by calling `preprocess_text(your_text_here)`. You can also use this function with multiple texts if you want to preprocess more than one document, as you will need to do later with the trial sources. Let's practice this.
Save your second text file in the variable second_text: `second_text = all_texts[1]`. Then, call the `preprocess_text()` function with `second_text` as an argument and save the result in a variable called `processed_second_text`. Print the content of the `processed_second_text` variable to see if it worked. Finally, use a for-loop to iterate over the texts list, preprocess each text using the preprocess_text() function, and print the result.
```python
for text in all_texts:
    processed = preprocess_text(text)
    print(processed)
```
You can play around with the terminal outcome to make it more readable:
```python
for text in all_texts:
    processed = preprocess_text(text)
    print("----- New Document -----")
    print(processed)
    print("\n")
    print("----- End Document -----")
```

Perfect! You have successfully completed the text preprocessing exercise using NLTK. You can now use the `preprocess_text()` function to preprocess any text data you want to analyze further. 
You have learned:
- How to install and import the NLTK library
- How to read multiple text files from a folder
- How to preprocess text data by lowercasing, tokenizing, lemmatizing, and removing stopwords
- How to create a reusable function for text preprocessing
