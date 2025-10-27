import spacy
from collections import Counter
import matplotlib.pyplot as plt

nlp = spacy.load("en_core_web_md")


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

label_counts = get_entity_label_counts(text) # you need to pass your text here
plot_entity_labels(label_counts)
