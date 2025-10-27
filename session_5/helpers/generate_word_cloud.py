from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(tokens, filename="word_cloud.png"):
   text = ' '.join(tokens)  # Join the tokens into a single string
   wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

   # Display the word cloud using Matplotlib
   plt.figure(figsize=(10, 5))
   plt.imshow(wordcloud, interpolation='bilinear')
   plt.axis('off')  # Hide the axes
   plt.title('Word Cloud of Most Common Words')
   plt.tight_layout()
   plt.savefig(filename)
