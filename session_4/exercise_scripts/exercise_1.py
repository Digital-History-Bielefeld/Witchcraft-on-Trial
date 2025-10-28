import spacy
import os
from collections import Counter
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")

folder_path = './session_4/data/'
all_texts = []
for filename in os.listdir(folder_path):
  with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
      all_texts.append(file.read())

our_text = all_texts[0]

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

merge_names = [["Augustus Bedloe", "Bedloe"], ["Warren Hastings", "Hastings"]]
most_common_persons = get_most_common_entities(our_text, merge_entity_names=merge_names)

context_templeton = get_entity_context(our_text, ["Templeton"])
context_multiple = get_entity_context(our_text, ["Augustus Bedloe", "Bedloe"], top_n=10)

# ----------------------------
# You can add your code for visualization below
# ----------------------------
