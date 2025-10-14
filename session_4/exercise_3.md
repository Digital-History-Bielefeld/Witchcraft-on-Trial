# Exercises

## Session 4 - Data Visualization techniques

In this session, we will explore various data visualization techniques using Python. We will cover methods such as creating static and interactive visualizations, using libraries like Matplotlib.
So far, you have learned the following text analysis techniques:

* Text Preprocessing
* Named Entity Recognition (NER)
* Context Analysis with Word Frequency, N-Grams, and TF–IDF
* Topic Modeling with LDA
  With these methods, you got interesting insights into the content of the texts. However, the results were mostly presented in your terminal as text output. In this session, we will learn how to visualize the results of text analysis in a more appealing and informative way. Visualizations can help you to better understand the data, identify patterns, and communicate your findings to others.

### Exercise 3 — Visualizing Topic Modeling Results with Matplotlib

In this exercise, we will visualize the results of the LDA topic modeling that you created in Session 3, Exercise 4. Visualization helps us interpret the discovered topics and their most important words. We will use the `matplotlib` library to create clear and simple visual representations of the topics and their distributions.

1. First, make sure you have the `matplotlib` library installed:

   ```bash
   pip install matplotlib
   ```

2. Open the file `exercise_3.py`, which contains the LDA topic modeling code from Session 3, Exercise 4. We will add visualization code to this file. You should already have the LDA model created and the corpus and dictionary prepared. 

3. Add the following imports to the top of your file:

   ```python
   import matplotlib.pyplot as plt
   import numpy as np
   ```

4. Now, let’s visualize the **top words for each topic**. Each topic can be represented as a bar chart where the x-axis shows the top words and the y-axis shows their contribution (weight).
   Add the following function to your code:

   ```python
   def plot_top_words_per_topic(lda_model, num_words=10):
       for topic_id, topic in lda_model.show_topics(num_topics=-1, num_words=num_words, formatted=False):
           words = [w for w, _ in topic]
           weights = [v for _, v in topic]
           plt.figure(figsize=(10, 5))
           plt.bar(words, weights, color='skyblue')
           plt.title(f"Top {num_words} Words for Topic {topic_id}")
           plt.xticks(rotation=45)
           plt.ylabel('Weight')
           plt.tight_layout()
           plt.savefig(f"topic_{topic_id}_top_words.png")
           plt.close()
   ```

   This function loops through all topics in the LDA model, extracts the top words and their weights, and creates one bar chart per topic.
   Call this function with:
   
   ```python
   plot_top_words_per_topic(lda_model, num_words=10)
   ```
   You will get a PNG file for each topic showing the top words and their weights.
5. Next, we want to visualize the **topic distribution for each document**. For this, we can use a stacked bar chart that shows how strongly each topic is represented in a given document. Add the following code:

   ```python
   def plot_topic_distribution_per_doc(lda_model, corpus, num_topics):
       doc_topics = [lda_model.get_document_topics(doc) for doc in corpus]
       topic_distributions = np.zeros((len(doc_topics), num_topics))

       for i, doc in enumerate(doc_topics):
           for topic_id, weight in doc:
               topic_distributions[i][topic_id] = weight

       plt.figure(figsize=(10, 6))
       for topic_id in range(num_topics):
           plt.bar(range(len(doc_topics)), topic_distributions[:, topic_id], bottom=np.sum(topic_distributions[:, :topic_id], axis=1), label=f"Topic {topic_id}")
       plt.xlabel("Document")
       plt.ylabel("Topic Proportion")
       plt.title("Topic Distribution Across Documents")
       plt.legend()
       plt.tight_layout()
       plt.savefig("topic_distribution_per_doc.png")
       plt.close()
   ```



These visualizations help you understand:

* which words define each topic
* how strongly each topic appears across your documents.

You can experiment with the number of topics and words per topic to see how the visualizations change. Try increasing `num_topics` or `num_words` and observe how the structure of your data becomes clearer.
