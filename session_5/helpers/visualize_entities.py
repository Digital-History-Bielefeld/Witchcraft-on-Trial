import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_md")

def visualize_entities(text):
    doc = nlp(text)
    displacy.serve(doc, auto_select_port=True, style="ent", options={"ents": ["GPE", "PERSON"], "colors": {"ORG": "#ec8a75", "PERSON": "#75c3ec"}})
