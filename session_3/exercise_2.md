# Exercises
## Session 3 — Techniques for Text Analysis (for Historians)


### Exercise 2 — Named Entity Recognition (NER) with SpaCy and Basic Co-Occurrence Analysis

In this exercise, we will use the SpaCy library to identify and analyze named entities such as persons, locations, and organizations in a text by Edgar Allan Poe.
After extracting these entities, we will extend our analysis with a basic co-occurrence approach that examines which words most often appear in the context of certain persons.
SpaCy is a powerful NLP library that provides pre-trained models for various languages and tasks, including NER. We will use SpaCy's English language model to process the text and extract named entities. You can find more information about SpaCy and its NER capabilities in the [official documentation](https://spacy.io/). There you can find [installation instructions](https://spacy.io/usage), [guides](https://spacy.io/usage/linguistic-features), and a [spaCy 101](https://spacy.io/usage/spacy-101).


1. First, we need to install the SpaCy library and download the English language model. You can do this by running the following commands in your terminal:
```bash
pip install -U pip setuptools wheel
```
```bash
pip install spacy
```
```bash
python -m spacy download en_core_web_md
```
This steps will install necessary packages, spaCy itself, and the medium-sized English language model. You can also choose to download the small or large models. If you want, you can play around with the different models later to see how they perform on the text. In our case, the medium model is a good balance between speed and accuracy, while the small model is faster but much less accurate, and the large model is more accurate but slower. To install the other models, you can use the following commands:

```bash
python -m spacy download en_core_web_sm  # Small model
```
```bash
python -m spacy download en_core_web_lg  # Large model
```


2. Next, we will import the necessary module and load the English language model in our script. Open the file `exercise_scripts/exercise_2.py` and add the imports at the beginning of your script:
```python
import spacy
```
  Then load the SpaCy model by adding the following line of code after the import:
```python
nlp = spacy.load("en_core_web_md")
```
This will load the medium English language model which is sufficient for our NER task. You can also use the small model ("en_core_web_sm") if you want a quicker setup, but the medium model generally provides better accuracy. If you want, you can play around with different models and see how they perform on the text later:
```python
nlp = spacy.load("en_core_web_sm")  # Small model
nlp = spacy.load("en_core_web_md")  # Medium model
nlp = spacy.load("en_core_web_lg")  # Large model
```
Remember to download the respective models using the command in your terminal:
```
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
python -m spacy download en_core_web_lg
```
Now you can use the functionality of SpaCy in your code.

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
  our_text = all_texts[4]
  ```
You can play around with the index to access different texts in the list. For example, `our_text[0]` will give you the first text, `all_texts[1]` the second text, and so on. For this exercise, the first text (index 0) is the best choice to start with.


4. Now we can process the text using the SpaCy NLP pipeline. SpaCy marks named entities in the text and assigns them labels such as "PERSON" for persons, "GPE" for geopolitical entities (like cities or countries), and "ORG" for organizations. We can extract these entities and count how often they appear in the text. Here is an overview of the entity labels used by SpaCy:

| Label | Description |
| --- | --- |
| PERSON | People, including fictional. |
| NORP | Nationalities or religious or political groups. |
| FAC | Buildings, airports, highways, bridges, etc. |
| ORG | Organizations, companies, agencies, institutions, etc. |
| GPE | Countries, cities, states. |
| DATE | Absolute or relative dates or periods. |
| CARDINAL | Numerals that do not fall under another type. |

Let's start by creating a function called `get_most_common_entities` that takes a text, an entity label (like "PERSON" or "GPE"), and a number `top_n` as input and returns the most common entities of that type in the text.

```python
def get_most_common_entities(text, entity_label="PERSON", top_n=10):
```
The entity_label parameter uses "PERSON" as a default value, but you can call the function with other labels to get different types of entities. The top_n parameter specifies how many of the most common entities you want to return. As a default, we want to return the top 10 entities. Inside the function, we will process the text with SpaCy and extract the entities:
```python
  doc = nlp(text)
  entities = []
  for ent in doc.ents:
      if ent.label_ == entity_label:
          entities.append(ent.text)
```
This code will create a `Doc` object by passing the text to the `nlp` object. In simple terms, this means that SpaCy will analyze the text and identify various linguistic features, including named entities. You don't need to worry about the details of how this works; just know that the `doc` object now contains all the information SpaCy has extracted from the text. Then, the code will iterate over the named entities in the `Doc` object and append the text of the entities that match the specified label to the `entities` list. Finally, we will count the occurrences of each entity and return the most common ones. For this, we will use the `Counter` class from the `collections` module. You need to import it at the beginning of your script:

```python
from collections import Counter
```

Then, you can add the following code to the function to count the entities and return the most common ones:
```python
  counts = Counter(entities)
  return counts.most_common(top_n)
```
The `most_common` method returns a list of the most common entities along with their counts.
Your function is now complete and should look like this:
```python
def get_most_common_entities(text, entity_label="PERSON", top_n=10):
  doc = nlp(text)
  entities = []
  for ent in doc.ents:
      if ent.label_ == entity_label:
          entities.append(ent.text)
  counts = Counter(entities)
  return counts.most_common(top_n)
```
You can now call the function with `our_text` as an argument and print the result. You can also play around with the `entity_label` and `top_n` parameters to see how they affect the output. You can call the function like this:

```python
top_persons = get_most_common_entities(our_text)
print("Most common persons:", top_persons)
```
Or to get the most common locations, you can call the function like this with the 3 top locations:
```python
top_locations = get_most_common_entities(our_text, entity_label="GPE", top_n=3)
print("Most common locations:", top_locations)
```


5. You may notice that some names appear multiple times in different forms (like "Mr. Smith" and "Smith"). To clean this up, you can create a merge function that combines these variations into a single name. You have different options for how to do this. In this exercise, we will use a simple approach. We will create a list with lists of name variations. For example:
```python
merge_names = [
    ["Mr. Smith", "Smith", "John Smith"],
    ["Dr. Johnson", "Johnson"]
]
```
Remember that you have various options to work with lists. One is to create a list with lists in it. If you want to access the first list in the list, you can do it like this: `merge_names[0]`. If you want to access the first element of the first list, you can do it like this: `merge_names[0][0]`. You can also use a for loop to iterate over the lists and their elements. For example:
```python
for name_list in merge_names:
    for name in name_list:
      print(name)
```
You can use this approach to do the following:
- Create a list `merge_names` with lists of name variations. The first name in each list will be the name that all variations will be merged into.
- Then we want to iterate over the `persons` list to check if a name is in one of the lists in `merge_names`. If it is, we will replace it with the first name of the corresponding list.
- With this approach, all variations of a name will be replaced with a single, consistent name.

So let's implement this in our `get_most_common_entities` function. You can add `merge_entity_names` as a parameter to the function with a default value of an empty list. Then we use a new concept: the `range` function. With this function, you can create a sequence of numbers. For example, `range(5)` will create a sequence of numbers from 0 to 4. You can use this function to iterate over the indices of the `persons` list. This way, you can access and modify the elements of the list directly. This code should take place before counting the names with `Counter`.
Here is how you can do it:

```python
for entity_name_list in merge_entity_names: # Iterate over the lists of name variations
  for i in range(len(entities)): # Iterate over the indices of the persons list
      if entities[i] in entity_name_list: # Check if the name is in one of the lists
        entities[i] = entity_name_list[0] # Replace it with the first name in the corresponding list
```

This code will iterate over the indices of the `persons` list and check if each name is in one of the lists in `merge_names`. If it is, it will replace it with the first name in the corresponding list. Try to understand how this code snippet works. It may helps to print out single steps to see what is happening or maybe you can try to draw the steps on a piece of paper.
Your updated function should now look like this:

```python
def get_most_common_entities(text, entity_label="PERSON", top_n=10, merge_entity_names=[]):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        if ent.label_ == entity_label:
            entities.append(ent.text)

    # Merge name variations
    for entity_name_list in merge_entity_names:
        for i in range(len(entities)):
            if entities[i] in entity_name_list:
                entities[i] = entity_name_list[0]

    counts = Counter(entities)
    return counts.most_common(top_n)
```
 Finally, call the function with a `merge_names` list and print the result to see if it worked:
```python
merge_names = [["Augustus Bedloe", "Bedloe"], ["Warren Hastings", "Hastings"]]
most_common_entities = get_most_common_entities(our_text, merge_entity_names=merge_names)
print(most_common_entities)
```
You may notice that "Bedloe" and "Augustus Bedloe" morph into "Augustus Bedloe" in the output. This changes the ranking of the most mentioned persons in the text and there is a new person in the top 10 list: "Augustus Bedlo". You should also add this name to the `merge_names` list. Play around with different name variations to see how they affect the output.


6. So far, we know who appears often.
Next, we want to explore which words typically occur around them — for example, what adjectives or nouns appear in the same sentence as the person. This can give us insights into how these persons are described or what actions they are associated with in the text. To do this, we will create a function called `get_entity_context` that takes a text, a list of entity names, and a number `top_n` as input and returns the most common words that appear in the context of those entities. The context is defined as the words that appear in the same sentence as the entity. Here is how you can implement this function:
First, you need to import the `Matcher` class from the `spacy.matcher` module at the beginning of your script:
```base
from spacy.matcher import Matcher
```
Then, you can define the `get_entity_context` function like this:
```python
def get_entity_context(text, entity_names, top_n=10):
```
Then we want to process the text with spaCy.
```python
  doc = nlp(text)
  matcher = Matcher(nlp.vocab)
  for name in entity_names:
      name_tokens = name.split()
      pattern = [{"LOWER": token.lower()} for token in name_tokens]
      matcher.add("NAME", [pattern])
```
This code will create a `Doc` object by passing the text to the `nlp` object. Then, it will create a `Matcher` object and add patterns for each entity name in the `entity_names` list. In detail, it works as follows:
- The `Matcher` class is used to find sequences of tokens that match specific patterns in the text. We create a `Matcher` object by passing the vocabulary of the `nlp` object.
- For each entity name in the `entity_names` list, we create a pattern that matches the lowercase version of the name. If the name consists of multiple words (like "John Smith"), we split it into individual tokens using the `split()` method.The pattern is a list of dictionaries, where each dictionary represents a token in the name. The `LOWER` key is used to match the lowercase version of the token. Or in very simple terms: We want to match the name regardless of whether it is written in uppercase or lowercase letters.
- Finally, we add the pattern to the matcher with the label "NAME". Or in simple terms: We tell the matcher to look for the patterns we just created.

Next, we will use the matcher to find the occurrences of the entity names in the text and extract the context words:
```python
  matches = matcher(doc)
  context_words = []
  for match_id, start, end in matches:
      span = doc[start:end].sent
      for token in span:
          if token.pos_ in ["NOUN", "VERB", "ADJ"]:
              context_words.append(token.lemma_.lower())
```
This code does the following:
- It uses the matcher to find all occurrences of the entity names in the `Doc` object and stores the matches in the `matches` variable.
- It initializes an empty list called `context_words` to store the context words.
- It iterates over the matches found by the matcher.
- For each match, it gets the sentence that contains the match using the `sent` attribute of the `Doc` object. `sent` is a property that returns the sentence span containing the matched entity.
- It then iterates over the tokens in the sentence and checks if the token is a noun, verb, or adjective using the `pos_` attribute of the token. The `pos_` attribute provides the part-of-speech tag of the token as a string.
- If the token is a noun, verb, or adjective, it appends its lemma (base form) in lowercase to the `context_words` list using the `lemma_` attribute of the token.
You don't need to worry about the details of how this works; just know that the `context_words` list now contains all the relevant words that appear in the same sentences as the specified entity names. If you want to learn more about the Matcher class and how it works, you can check out the [official SpaCy documentation on the Matcher](https://spacy.io/usage/rule-based-matching).

Finally, we will count the occurrences of each context word and return the most common ones:
```python
    return Counter(context_words).most_common(top_n)
```
This code uses the `Counter` class from the `collections` module to count the occurrences of each context word in the `context_words` list. The `most_common` method returns a list of the most common context words along with their counts.
The function is now complete and should look like this:
```python
def get_entity_context(text, entity_names, top_n=10):
  doc = nlp(text)
  matcher = Matcher(nlp.vocab)
  for name in entity_names:
      name_tokens = name.split()
      pattern = [{"LOWER": token.lower()} for token in name_tokens]
      matcher.add("NAME", [pattern])


  matches = matcher(doc)
  context_words = []
  for match_id, start, end in matches:
      span = doc[start:end].sent
      for token in span:
          if token.pos_ in ["NOUN", "VERB", "ADJ"]:
              context_words.append(token.lemma_.lower())

  return Counter(context_words).most_common(top_n)
```
You can now call the function with `our_text` and a list of entity names as arguments and print the result. You can also play around with the `entity_names` and `top_n` parameters to see how they affect the output. For example, to get the 10 most common context words around the person "Templeton", you can call the function like this:
```python
context_templeton = get_entity_context(our_text, ["Templeton"])
print("\nTop context words around 'Templeton':")
for word, freq in context_templeton:
    print(f"  {word}: {freq}")
```
This code will print the 10 most common context words that appear in the same sentences as "Templeton" along with their counts.
Play around with different names from the `most_common_entities` output to see what context words are associated with them. You can also try using multiple names at once by passing a list of names to the `entity_names` parameter, especially the merged names from the previous step:
```python
context_multiple = get_entity_context(our_text, ["Augustus Bedloe", "Bedloe"], top_n=10)
print("\nTop context words around 'Augustus Bedloe' and 'Bedloe':")
for word, freq in context_multiple:
    print(f"  {word}: {freq}")
```

In summary, you have learned:
- How to install and set up SpaCy for NER tasks.
- How to read and process text files using SpaCy.
- How to extract, filter, and count named entities.
- How to clean up entity names by merging variations.
- How to analyze the context of entities by finding co-occurring words in sentences.

These techniques can be applied to various types of texts and can provide valuable insights into the content and themes of the documents.
