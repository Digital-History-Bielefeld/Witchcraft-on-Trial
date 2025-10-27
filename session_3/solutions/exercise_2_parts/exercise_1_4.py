import spacy
import os
from collections import Counter

nlp = spacy.load("en_core_web_md")

folder_path = './session_3/data/'
all_texts = []
for filename in os.listdir(folder_path):
  with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
      all_texts.append(file.read())

our_text = all_texts[0]

def get_most_common_entities(text, entity_label="PERSON", top_n=10):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        if ent.label_ == entity_label:
            entities.append(ent.text)
    counts = Counter(entities)
    return counts.most_common(top_n)


top_persons = get_most_common_entities(our_text)
print("Most common persons:", top_persons)

top_locations = get_most_common_entities(our_text, entity_label="GPE", top_n=4)
print("Most common locations:", top_locations)
