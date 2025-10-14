# Exercises
## Session 3 — Techniques for Text Analysis (for Historians)


### Exercise 2 — Named Entity Recognition (NER) with SpaCy and Basic Co-Occurrence Analysis

In this exercise, we will use the SpaCy library to identify and analyze named entities such as persons, locations, and organizations in a literary text by Edgar Allan Poe.
After extracting these entities, we will extend our analysis with a basic co-occurrence approach that examines which words most often appear in the context of certain persons.

1. First, we need to install the SpaCy library and download the English language model. You can do this by running the following commands in your terminal:
  ```
  pip install -U pip setuptools wheelpip install -U pip setuptools wheel
  pip install spacy
  python -m spacy download en_core_web_md
  ```
2. Next, we will import the necessary modules from SpaCy and load the English language model. Open the file `exercise_2.py` and add the imports at the beginning of your script:
  ```python
  import spacy
  from collections import Counter
  from spacy.matcher import Matcher
  import os
  ```
  Then load the SpaCy model:
  ```python
  nlp = spacy.load("en_core_web_md")
  ```
This will load the medium English language model which is sufficient for our NER task. You can also use the small model ("en_core_web_sm") if you want a quicker setup, but the medium model generally provides better accuracy. If you want, you can play around with different models and see how they perform on the text:
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

3. Next, we want to access our example text files in the `data` folder. With digital methods, you typically work with a large number of documents, not just one. In the last exercises, we always called up the texts individually. If you are writing programs, you don't want to repeat yourself. So we want to fix the part where we read in each text individually. Instead, we want to read in all texts in a folder and store them in a list. You can use the `os` module to list all files in a directory and read their contents. Here is an example of how you can do this:
   ```python
   import os

   folder_path = '../data/'
   all_texts = []
   for filename in os.listdir(folder_path):
       if filename.endswith('.txt'):
           with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
               all_texts.append(file.read())
   ```
This code will read all `.txt` files in the specified folder and store their contents in the `all_texts` list. Add it to your code and create a new variable `our_text`. We want to start with only one text for now, to learn how to work with SpaCy. You can choose any text from the `all_texts` list. The best results will be achieved with the text `EAP_5.txt`, which you can access with `all_texts[4]`. Here is how you can do it:
   ```python
   our_text = all_texts[4]
   ```
You can play around with the index to access different texts in the list. For example, `our_text[0]` will give you the first text, `all_texts[1]` the second text, and so on.

4. Now we can process the text using the SpaCy NLP pipeline. Let's start by creating a function called `get_most_common_entities` that takes a text, an entity label (like "PERSON" or "GPE"), and a number `top_n` as input and returns the most common entities of that type in the text. 
  ```python
  def get_most_common_entities(text, entity_label="PERSON", top_n=10):
  ```
The entity_label parameter uses "PERSON" as a default value, but you can call the function with other labels to get different types of entities. The top_n parameter specifies how many of the most common entities you want to return. Inside the function, we will process the text with SpaCy and extract the entities:
  ```python
     doc = nlp(text)
     entities = []
     for ent in doc.ents:
         if ent.label_ == entity_label:
             entities.append(ent.text)
  ```
This code will create a `Doc` object by passing the text to the `nlp` object. Then, it will iterate over the named entities in the `Doc` object and append the text of the entities that match the specified label to the `entities` list. Finally, we will count the occurrences of each entity and return the most common ones:
  ```python
     counts = Counter(entities)
     return counts.most_common(top_n)
  ```
This code uses the `Counter` class from the `collections` module to count the occurrences of each entity in the `entities` list. The `most_common` method returns a list of the most common entities along with their counts.
The function is now complete and should look like this:
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
You can now call the function with `our_text` as an argument and print the result. You can also play around with the `entity_label` and `top_n` parameters to see how they affect the output. For example, to get the 10 most common persons in the text, you can call the function like this:
  ```python
  top_persons = get_most_common_entities(our_text, "PERSON", top_n=10)
  print("Most common persons:", top_persons)
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
- Create a list `merge_names` with lists of name variations. 
- Then we want to iterate over the `persons` list to check if a name is in one of the lists in `merge_names`. If it is, we will replace it with the first name in the corresponding list. 
- With this approach, all variations of a name will be replaced with a single, consistent name.

So let's implement this in the `get_most_common_entities` function. You can add the `merge_names` list as a parameter to the function with a default value of an empty list. Then we use a new concept: the `range` function. With this function, you can create a sequence of numbers. For example, `range(5)` will create a sequence of numbers from 0 to 4. You can use this function to iterate over the indices of the `persons` list. This way, you can access and modify the elements of the list directly. Here is how you can do it:
  ```python
  for entity_name_list in merge_entity_names:
    for i in range(len(entities)):
        if entities[i] in entity_name_list:
          entities[i] = entity_name_list[0]
  ```
This code will iterate over the indices of the `persons` list and check if each name is in one of the lists in `merge_names`. If it is, it will replace it with the first name in the corresponding list. You can add this part of code to the `get_most_common_entities` function before counting the names with `Counter`:
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
You may notice that "Bedloe" and "Augustus Bedloe" morph into "Augustus Bedloe" in the output. This changes the ranking of the most mentioned persons in the text and there is a new person in the top 10 list: "Augustus Bedlo". You should also add this name to the `merge_names` list.

6. So far, we know who appears often.
Next, we want to explore which words typically occur around them — for example, what adjectives or nouns appear in the same sentence as the person. This can give us insights into how these persons are described or what actions they are associated with in the text. To do this, we will create a function called `get_entity_context` that takes a text, a list of entity names, and a number `top_n` as input and returns the most common words that appear in the context of those entities. The context is defined as the words that appear in the same sentence as the entity. Here is how you can implement this function:
```python
def get_entity_context(text, entity_names, top_n=10):
```
Then we want to process the text with spaCy.
```python
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)
    for name in entity_names:
      pattern = [{"LOWER": token.lower()} for token in name.split()]
      matcher.add("NAME", [pattern])
```
This code will create a `Doc` object by passing the text to the `nlp` object. Then, it will create a `Matcher` object and add patterns for each entity name in the `entity_names` list. The patterns are defined to match the lowercase version of the entity names. Next, we will use the matcher to find the occurrences of the entity names in the text and extract the context words:
```python
    matches = matcher(doc)
    context_words = []
    for match_id, start, end in matches:
        span = doc[start:end].sent
        for token in span:
            if token.pos_ in ["NOUN", "VERB", "ADJ"]:
                context_words.append(token.lemma_.lower())
```
This code will find all matches of the entity names in the `Doc` object and iterate over them. For each match, it will get the sentence that contains the match and iterate over the tokens in that sentence. If a token is a noun, verb, or adjective, it will append its lemma (base form) in lowercase to the `context_words` list. Finally, we will count the occurrences of each context word and return the most common ones:
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
      matcher.add("NAME", [[{"LOWER": name.lower()}]])


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
context_templeton = get_entity_context(our_text, ["Templeton"], top_n=10)
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
