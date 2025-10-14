import spacy
from spacy.matcher import Matcher
from collections import Counter
import os

# ----------------------------
# Load model and data
# ----------------------------
nlp = spacy.load("en_core_web_md")

folder_path = "../data/"
all_texts = []
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
            all_texts.append(f.read())

our_text = all_texts[4]

# ----------------------------
# Named Entity Recognition
# ----------------------------
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

# Example: Top persons
merge_names = [["Augustus Bedloe", "Bedloe", "Augustus Bedlo"], ["Warren Hastings", "Hastings"]]
most_common_entities = get_most_common_entities(our_text, merge_entity_names=merge_names)
print(most_common_entities)

# ----------------------------
# Basic co-occurrence context
# ----------------------------
def get_entity_context(text, entity_names, top_n=10):
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)
    for name in entity_names:
      pattern = [{"LOWER": token.lower()} for token in name.split()]
      matcher.add("NAME", [pattern])


    matches = matcher(doc)
    context_words = []
    for match_id, start, end in matches:
      span = doc[start:end].sent
      for token in span:
        if token.pos_ in ["NOUN", "VERB", "ADJ"]:
            context_words.append(token.lemma_.lower())

    return Counter(context_words).most_common(top_n)

# Example: Context words around "Templeton"
context_templeton = get_entity_context(our_text, ["Templeton"], top_n=10)
print("\nTop context words around 'Templeton':")
for word, freq in context_templeton:
    print(f"  {word}: {freq}")

# context_multiple = get_entity_context(our_text, ["Augustus Bedloe", "Bedloe"], top_n=10)
# print("\nTop context words around 'Augustus Bedloe' and 'Bedloe':")
# for word, freq in context_multiple:
#     print(f"  {word}: {freq}")

# ----------------------------
# You can add your code for visualization below
# ----------------------------
