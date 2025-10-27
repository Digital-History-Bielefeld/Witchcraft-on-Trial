import matplotlib.pyplot as plt

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
