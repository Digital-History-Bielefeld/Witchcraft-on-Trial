# Exercises
## Session 4 - Data Visualization techniques

In this session, we will explore some data visualization techniques using Python. Data visualization is a powerful tool to help you understand and communicate insights from your data.
So far, you have learned the following text analysis techniques:
- Text Preprocessing
- Named Entity Recognition (NER)
- Context Analysis with Word Frequency, N-Grams, and TF–IDF
With these methods, you got interesting insights into the content of the texts. However, the results were mostly presented in your terminal as text output. In this session, we will learn how to visualize the results of text analysis in a more appealing and informative way. Visualizations can help you to better understand the data, identify patterns, and communicate your findings to others.

### Exercise 2 — Visualizing Word Frequencies with Matplotlib
In this exercise, we will visualize the word frequencies from the context analysis (corresponding to exercise 3 of session 3) using the Matplotlib library. The Matplotlib library is a widely used library for creating static visualizations in Python. You can read more about Matplotlib in the [official documentation](https://matplotlib.org). If you haven't installed Gensim and NLTK in session 3, please do so by running:

```bash
pip install --upgrade gensim
```
```bash
pip install --user -U nltk
```

1. First, we need to install the Matplotlib library. You can do this by running the following command in your terminal:
```
pip install matplotlib 
```

With Matplotlib installed, we can now proceed to visualize the word frequencies.


2. Now you can open the file `exercise_scripts/exercise_2.py`. In exercise 3 of session 3, we performed a context analysis of a text by finding the most common words using the `word_frequency` function. We will use the results from that exercise to create a bar chart. The file `exercise_2.py` already contains the preprocessing steps and the `word_frequency` function from exercise 3, so you can start right there. There you need to import the necessary modules from Matplotlib. You can do this by adding the following lines after the existing import statements:
```python
...
import matplotlib.pyplot as plt
```
These imports will allow you to use Matplotlib for creating bar charts.


3. Now we want to use the `most_common_words` variable from exercise 3, which contains the most common words and their frequencies. We will create a bar chart to visualize this data. You can do this by adding the following code after the line where `most_common_words` is defined:
```python
# Unzip the most common words into two lists: words and counts
words, counts = zip(*most_common_words)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(words, counts, color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Most Common Words in the Text')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('most_common_words.png')  # Save the figure as a PNG file
```
So, what happens here?
- We unzip the `most_common_words` list into two separate lists: `words` and `counts`. This allows us to easily access the words and their corresponding frequencies.
- We create a bar chart using Matplotlib. We set the figure size, bar colors, and labels for the x-axis and y-axis. We also add a title to the chart.
- We rotate the x-axis labels for better readability and use `plt.tight_layout()` to ensure that the layout is adjusted properly.
- Finally, we save the figure as a PNG file using `plt.savefig()`. You should see a file named `most_common_words.png` in your working directory after running the script.

You can play around with the parameters to customize the appearance of the chart. For example, you can change the color of the bars, adjust the figure size, or modify the labels and title. You should also play around with the custom stopwords in line 67 to get better results.


4. We want to use the same code for the most common n-grams. So, we should create a function to avoid code duplication. Define a function called `plot_bar_chart` that takes two lists (words and counts) and a title as input and creates a bar chart:

```python
def plot_bar_chart(words, counts, title):
   plt.figure(figsize=(10, 6))
   plt.bar(words, counts, color='skyblue')
   plt.xlabel('Words')
   plt.ylabel('Frequency')
   plt.title(title)
   plt.xticks(rotation=45)
   plt.tight_layout()
   plt.savefig(f"{title.replace(' ', '_').lower()}.png")  # Save the figure as a PNG file
```

This code replaces the code you wrote in step 3. The function takes the same parameters as before and creates a bar chart with the given title.
You can then call this function with the `most_common_words` to get the same result as before:

```python
# Plot the most common words of the first text
words, counts = zip(*most_common_words)
plot_bar_chart(words, counts, 'Most Common Words in the Text')
```

Plotting the most common bigrams and trigrams is a bit more tricky because the n-grams are tuples of words. You need to convert them to strings before plotting. You can do this by adding the following code after the line where `most_common_trigrams` is defined:

```python
# Plot the most common bigrams of the first text
bigram_words, bigram_counts = zip(*most_common_bigrams)
bigram_words = [' '.join(bigram) for bigram in bigram_words] # This converts the tuples to strings with a list comprehension
plot_bar_chart(bigram_words, bigram_counts, 'Most Common Bigrams in the Text')

# Plot the most common trigrams of the first text
trigram_words, trigram_counts = zip(*most_common_trigrams)
trigram_words = [' '.join(trigram) for trigram in trigram_words] # This converts the tuples to strings with a list comprehension
plot_bar_chart(trigram_words, trigram_counts, 'Most Common Trigrams in the Text')
```

Now you should see three PNG files in your working directory: `most_common_words_in_the_text.png`, `most_common_bigrams_in_the_text.png`, and `most_common_trigrams_in_the_text.png`. Each file contains a bar chart showing the frequency of the most common words, bigrams, and trigrams in the text, respectively.

If you are done exploring the visualizations of word frequencies, delete or comment out (with a #) the different calls to `plot_bar_chart` to avoid cluttering your working directory with too many files.


5. Now let's continue with the last part: visualizing the TF-IDF results. We will create a bar chart to display the top TF-IDF words in the text. You can use the `plot_bar_chart` function we defined earlier to create the bar chart. Add the following code at the end of the script:
```python
# Plot the top TF-IDF words of the first text
tfidf_words, tfidf_scores = zip(*top_tfidf_words[0])
plot_bar_chart(tfidf_words, tfidf_scores, 'Top TF-IDF Words in the Text')
```
This will create a bar chart showing the top TF-IDF words in the first text and save it as `top_tfidf_words_in_the_text.png` in your working directory. You can customize the appearance of the chart as you like. This chart gives you a quick overview of which words are most important in the text according to the TF-IDF metric. You can also use diffeerent texts by changing the index in `top_tfidf_words[index]` to visualize the TF-IDF results for other texts in your dataset:
```python
# Plot the top TF-IDF words of the second text
tfidf_words, tfidf_scores = zip(*top_tfidf_words[1])
plot_bar_chart(tfidf_words, tfidf_scores, 'Top TF-IDF Words in the Second Text')
```

   
6. There are many more ways to visualize text data. Let's try out another one. We will create a word cloud to visualize the most common words in the text. A word cloud is a graphical representation of word frequency, where the size of each word indicates its frequency in the text. It is a popular way to visualize text data because it provides an immediate visual impression of the most important words in a text, but it is not very precise. To create a word cloud, we will use the `wordcloud` library. You can install it by running the following command in your terminal:
```bash
pip install wordcloud
```
Now you can import the necessary modules from the `wordcloud` library by adding the following lines after the existing import statements:
```python
from wordcloud import WordCloud
```
Next, we will create a function called `generate_word_cloud` that takes a list of tokens as input and generates a word cloud:
```python
def generate_word_cloud(tokens, filename="word_cloud.png"):
   text = ' '.join(tokens)  # Join the tokens into a single string
   wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

   # Display the word cloud using Matplotlib
   plt.figure(figsize=(10, 5))
   plt.imshow(wordcloud, interpolation='bilinear')
   plt.axis('off')  # Hide the axes
   plt.title('Word Cloud of Most Common Words')
   plt.tight_layout()
   plt.savefig(filename) # Save the figure as a PNG file
```
You can then call this function with the `all_tokens` variable to generate the word cloud. Specify the index of the text you want to visualize. For example, to generate a word cloud for the first text, you can add the following code at the end of the script:
```python
generate_word_cloud(all_tokens[0], filename="first_text_wordcloud.png")
```
This will create a word cloud image of the words in the first text and saves it as `first_text_wordcloud.png` in your working directory. The words that appear more frequently in the text will be displayed in larger font sizes in the word cloud.
You can customize the appearance of the word cloud by changing the parameters of the `WordCloud` class, such as the width, height, and background color. You can also change the filename and the index in `all_tokens[index]` to generate word clouds for other texts in your dataset.

Now you learned about visualizing word frequencies using bar charts and word clouds. You can explore more visualization techniques and libraries to further enhance your text analysis projects. If you understand this exercise, you basically know how to work with different visualizations. 
