import spacy
from collections import Counter
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")

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
