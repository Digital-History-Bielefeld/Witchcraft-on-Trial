# Exercises
## Session 3 — Techniques for Text Analysis (for Historians)


### Exercise 1 — Text Preprocessing with NLTK

We will start with a simple text preprocessing procedure using the NLTK library. The goal is to prepare the text by tokenizing, stemming, lemmatizing, and removing stopwords. 

1. First of all, we want to install the NLTK library. Type the following command in your terminal:
   ```
   pip install nltk
   ```
   After the installation process, NLTK is ready to use in your codespace.
2. Now you can open the file exercise.py. There you need to import the necessary NLTK modules and download the required resources (like punkt and stopwords). You can do this by adding the following lines at the beginning of your script:
   ```python
   import nltk
   from nltk.corpus import stopwords
   from nltk.stem import WordNetLemmatizer

   nltk.download('punkt_tab')
   nltk.download('wordnet')
   nltk.download('stopwords')
   ```
   This is necessary to use the tokenization and stopword functionalities of NLTK inside your code.
3. Next, we want to access our example text file EAP_1.txt. You can **read** the content of the file using the open()-function. The correct path to the file is "../data/EAP_1.txt". Make sure to read the file with the correct encoding (utf-8). You can look at Session 2 if you need a reminder of how to work with files in Python or check the hints below. Save the content of the file in a variable called `first_text`. Print the content of the variable to see if you have successfully loaded the text.
   ```python
   with open("../data/EAP_1.txt", "r", encoding="utf-8") as f:
       first_text = f.read()
   ```
4. Now we can work with the text. To analyse the text, we need to preprocess it first. The preprocessing steps include:
   - Lowercasing the text
   - Tokenizing the text into words
   - Lemmatizing the tokens
   - Removing stopwords
Let's start with lowercasing the text. You can do this by using the `.lower()` method on the text variable. You  can find more information about this method in session 1. Save the result in a variable called `text`. Print the content of the variable to see if it worked.
   ```python
   text = first_text.lower()
   ```
5. Next, we will tokenize the text into words. You can use the `nltk.word_tokenize()` function for this. Pass the lowercased text to this function (which means, you should write the variable name `text` in the parentheses) and save the result in a variable called `tokens`. Print the content of the variable to see if it worked.
6. Now we have a list of tokens, but it also contains punctuation and special characters. We want to keep only the alphabetic tokens. You can use a list comprehension to filter out non-alphabetic tokens. The method `.isalpha()` can be used to check if a token is alphabetic. Update the `tokens` variable to contain only alphabetic tokens. It should look like this:
    ```python
    for t in tokens:
        if not t.isalpha():
            tokens.remove(t)
    
    # or the shorter version with list comprehension:
    tokens = [t for t in tokens if t.isalpha()]
    ```
    Print the content of the variable to see if it worked.
7. Next, we will lemmatize the tokens using the WordNet Lemmatizer. First, create an instance of the `WordNetLemmatizer` class. This means you need to write `lemmatizer = WordNetLemmatizer()` to create a lemmatizer object with which you can lemmatize words. This part of code should also be placed after the `nltk.download('stopwords')` line. It is a good practice to put all the imports and initializations at the beginning of your script.
Next, create a new empty list called `lemmas`. Then, use a for loop to iterate over the `tokens` list and apply the `lemmatizer.lemmatize()` method to each token. Append the lemmatized tokens to the `lemmas` list. Print the content of the `lemmas` variable to see if it worked.
8. Finally, we will remove stopwords from the lemmatized tokens. You can use the `stopwords.words('english')` function to get a list of English stopwords. Save `stopwords.words('english')` in a variable called `stop_words`.
Create a new empty list called `clean_tokens`. Then, use a for loop to iterate over the `lemmas` list and check if each token is not in the stopwords list. If it is not a stopword, append it to the `clean_tokens` list. Print the content of the `clean_tokens` variable to see if it worked.
9. Sometimes you want to add custom stopwords that are specific to your text. You can create a list of custom stopwords and extend the existing stopwords list with it. For example:
    ```python
    custom_stopwords = ['said', 'one', 'like']
    stop_words = stopwords.words('english')
    stop_words.extend(custom_stopwords)
    ```
    Try it out by adding some words that you think are not useful for the analysis of the text.
10. As a last step, we want to make our code more reusable. Therefore, we will wrap the preprocessing steps into a function called `preprocess_text()`. This function should take a text string as input and return the list of clean tokens. You can copy your code from the previous steps and paste it into the function. Make sure to indent the code correctly so that it is part of the function. The function should look like this:
    ```python
    def preprocess_text(text):
        # Your preprocessing code here
        return clean_tokens
    ```
Finally, call the function with `first_text` as an argument and print the result.
11. With the function in place, you can easily preprocess any text by calling `preprocess_text(your_text_here)`. You can also use this function with multiple texts if you want to preprocess more than one document, as you will need to do later with the trial sources. Let's practice this.
Save your second text file in the variable second_text. You can read the file the same way as you did before. The paths to the file is "../data/EAP_2.txt". Then, create a list called texts that contains both text variables `first_text` and `second_text`. Finally, use a for-loop to iterate over the texts list, preprocess each text using the preprocess_text() function, and print the result.

Perfect! You have successfully preprocessed the text using NLTK. You can now use the `clean_tokens` list for further analysis, such as frequency distribution, word clouds, or any other text analysis techniques.
