import spacy
from collections import Counter

nlp = spacy.load("en_core_web_md")

def get_most_common_entities(text, entity_label="PERSON", top_n=10, merge_entity_names=[]):
  doc = nlp(text)
  entities = []
  for ent in doc.ents:
      if ent.label_ == entity_label:
          entities.append(ent.text)

  for entity_name_list in merge_entity_names:
      for i in range(len(entities)):
          if entities[i] in entity_name_list:
              entities[i] = entity_name_list[0]

  counts = Counter(entities)
  return counts.most_common(top_n)
