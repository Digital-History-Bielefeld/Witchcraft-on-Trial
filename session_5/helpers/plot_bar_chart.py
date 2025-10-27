import matplotlib.pyplot as plt

words, counts = zip(*most_common_words) # Most_common_words is a result of word_frequency function

def plot_bar_chart(words, counts, title):
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{title.replace(' ', '_').lower()}.png")
