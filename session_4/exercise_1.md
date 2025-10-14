# Exercises
## Session 4 - Data Visualization techniques

In this session, we will explore various data visualization techniques using Python. We will cover methods such as creating static and interactive visualizations, using libraries like Matplotlib.
So far, you have learned the following text analysis techniques:
- Text Preprocessing
- Named Entity Recognition (NER)
- Context Analysis with Word Frequency, N-Grams, and TF–IDF
- Topic Modeling with LDA
With these methods, you got interesting insights into the content of the texts. However, the results were mostly presented in your terminal as text output. In this session, we will learn how to visualize the results of text analysis in a more appealing and informative way. Visualizations can help you to better understand the data, identify patterns, and communicate your findings to others.

### Exercise 1 - Visualizing NER results with Displacy and Matplotlib
In this exercise, we will visualize the results of Named Entity Recognition (NER) using the Displacy library from SpaCy. Displacy is a powerful tool for visualizing linguistic annotations, including named entities. In session 3, exercise 2 you have already worked with spaCy. We will use the code from that exercise as a starting point. Remeber to install spaCy and download the English model if you haven't done so already:
```bash
pip install spacy
python -m spacy download en_core_web_md
```
And also install Matplotlib if you haven't done so already:
```bash
pip install matplotlib
```
1. Open the file `exercise_2.py`. In exercise 2 of session 3, we performed Named Entity Recognition (NER) on a text using the SpaCy library. The file `exercise_2.py` already contains the preprocessing steps and the NER function from exercise 2, so you can start right there. You need to import the necessary modules from SpaCy. You can do this by adding the following lines after the existing import statements:
   ```python
   ...
   from spacy import displacy
   import matplotlib.pyplot as plt
   ```
2. Now we want to visualize the named entities found in the text using Displacy. 
   ```python
   # Visualize named entities in the text
   def visualize_entities(text):
       doc = nlp(text)
       displacy.serve(doc, style="ent", options={"ents": ["ORG", "PERSON"], "colors": {"ORG": "red", "PERSON": "blue"}})
    ```
  With this function, we create a SpaCy document from the input text and use Displacy to serve a web page that visualizes the named entities. We specify that we want to highlight organizations (ORG) in red and persons (PERSON) in blue. Call the function with the text you want to visualize:
   ```python
   visualize_entities(our_text)
   ```
  It will open a new tab in your web browser where you can see the visualization. If you want to quit this, just stop the script in your terminal (Ctrl+C).
  For our goals, "ORG" is maybe not the most interesting entity type, let's change it to "GPE" (Geopolitical Entity) or "LOC" (Location). Just play around with the entity types to see what you get. You can find a list of all entity types in the [SpaCy documentation](https://spacy.io/api/annotation#named-entities). You may also recognize that the colors are not very appealing. You can change them to your liking, for example, you could use "GPE": "green" and "PERSON": "orange" or use hex color codes like "#FF5733":
    ```python
    displacy.serve(doc, style="ent", options={"ents": ["GPE", "PERSON"], "colors": {"ORG": "#ec8a75", "PERSON": "#75c3ec"}})
    ``` 
3. Now you have visualized the named entities in the text using Displacy. But you can also visualize the frequency of the named entities using Matplotlib. We want to create a bar chart that shows the most common named entities in the text. For this, we want to create a function, that plot the entity frequencies:
   ```python
   def plot_entity_frequencies(entity_counts):
    labels, values = zip(*entity_counts)
    plt.figure(figsize=(10,5))
    plt.bar(labels, values, color='skyblue')
    plt.title("Most Common Entities")
    plt.xlabel("Entity")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("most_common_entities.png")
  ```
  This function takes a list of entity counts (tuples of entity and frequency) and creates a bar chart using Matplotlib. You can call this function with the most common PERSON entities found in the text:
   ```python
   plot_entity_frequencies(most_common_persons)
   ```
  The `most_common_persons` variable is already defined in the code from exercise 2 of session 3. It contains the most common PERSON entities found in the text. You can also create a similar chart for GPE or LOC entities by calling the `get_most_common_entities` function with the appropriate entity type and then passing the result to the `plot_entity_frequencies` function.
4. Now we want to compare how often different types of entities occur in the text. Create a function called `get_entity_label_counts`. This function should take a text as input and return a dictionary with the counts of each entity label (e.g., PERSON, ORG, GPE, etc.) found in the text:
  ```python
  def get_entity_label_counts(text):
      doc = nlp(text)
      label_counts = Counter([ent.label_ for ent in doc.ents])
      return label_counts
  ```
  Now we want to plot the results. Create the function `plot_entity_labels`. This function should take the dictionary returned by `get_entity_label_counts` and create a bar chart showing the frequency of each entity label:
  ```python
  def plot_entity_labels(label_counts):
    labels = list(label_counts.keys())
    values = list(label_counts.values())
    plt.figure(figsize=(8,6))
    plt.barh(labels, values, color='skyblue')
    plt.title("Distribution of Entity Types")
    plt.xlabel("Frequency")
    plt.tight_layout()
    plt.savefig("entity_label_distribution.png")
  ```
You can call these functions with the text you want to analyze:

```python
label_counts = get_entity_label_counts(our_text)
plot_entity_labels(label_counts)
```
This will give you a horizontal bar chart showing the distribution of different entity types in the text. You can customize the colors and appearance of the chart as you like. This chart gives you a quick overview of which types of entities are most prevalent in the text.

5. In the NER exercise, you extracted the most common context words around an entity. Now we will visualize them as a bar chart. You can use the `context_templeton` variable from exercise 2 of session 3, which contains the most common context words around the entity "Templeton". Create a function called `plot_context_words` that takes the list of context words and their frequencies and creates a bar chart:
   ```python
   def plot_context_words(context_words, entity_name):
       words, counts = zip(*context_words)
       plt.figure(figsize=(10, 6))
       plt.bar(words, counts, color='#9f66a1ff')
       plt.xlabel('Context Words')
       plt.ylabel('Frequency')
       plt.title(f'Most Common Context Words around "{entity_name}"')
       plt.xticks(rotation=45)
       plt.tight_layout()
       plt.savefig(f'context_words_{entity_name.lower()}.png')
   ```
  You can then call this function with the `context_templeton` variable:
  ```python
  plot_context_words(context_templeton, "Templeton")
  ```
This will create a bar chart showing the most common context words around the entity "Templeton".

Now you learned about visualizing NER results using Displacy and Matplotlib. You can explore further by experimenting with different entity types, colors, and texts. Visualizations can greatly enhance your understanding of the data and make it easier to communicate your findings.
