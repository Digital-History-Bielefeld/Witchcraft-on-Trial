import matplotlib.pyplot as plt

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
