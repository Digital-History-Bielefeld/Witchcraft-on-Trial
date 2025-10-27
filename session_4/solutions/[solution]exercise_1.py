import spacy
import os
from collections import Counter
from spacy.matcher import Matcher
from spacy import displacy
import matplotlib.pyplot as plt

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
      matcher.add("NAME", [[{"LOWER": name.lower()}]])


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

def visualize_entities(text):
    doc = nlp(text)
    displacy.serve(doc, auto_select_port=True, style="ent", options={"ents": ["GPE", "PERSON"], "colors": {"ORG": "#ec8a75", "PERSON": "#75c3ec"}})

# visualize_entities(our_text)

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

# plot_entity_frequencies(most_common_persons)

def get_entity_label_counts(text):
    doc = nlp(text)
    label_counts = Counter([ent.label_ for ent in doc.ents])
    return label_counts

def plot_entity_labels(label_counts):
  labels = list(label_counts.keys())
  values = list(label_counts.values())
  plt.figure(figsize=(8,6))
  plt.barh(labels, values, color='skyblue')
  plt.title("Distribution of Entity Types")
  plt.xlabel("Frequency")
  plt.tight_layout()
  plt.savefig("entity_label_distribution.png")

label_counts = get_entity_label_counts(our_text)
# plot_entity_labels(label_counts)

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

plot_context_words(context_templeton, "Templeton")
