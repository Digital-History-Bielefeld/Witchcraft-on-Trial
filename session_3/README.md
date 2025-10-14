# Session 3: Techniques for text analysis

You have learned the following concepts in Python so far:
- **Variables**: How to store and manipulate data
- **Data types**: Different types of data in Python (e.g., strings, integers, lists, dictionaries)
- **Control structures**: How to use `if` statements and loops
- **Strings**: How to work with strings in Python
- **Working with files**: How to read from and write to files
- **Functions**: How to define and use functions
- **Python Libraries**: How to use Python libraries

In this session you will learn some basic techniques for text analysis using Python:
- **Natural Language Processing (NLP)**: An introduction to NLP and its applications
- **Named Entity Recognition (NER)**: How to identify and classify named entities in a text
- **Text Preprocessing**: Techniques for cleaning and preparing text data for analysis
- **Word Frequency Analysis**: How to analyze the frequency of words in a text
- **N-gram Analysis**: How to analyze sequences of words in a text
- **TF-IDF (Term Frequency-Inverse Document Frequency)**: A statistical measure used to evaluate the importance of a word in a document relative to a collection of documents
- **Libraries for Text Analysis Tasks**: An overview of popular Python libraries for text analysis, including SpaCy, NLTK, and Gensim

This concepts are a good toolbox for historians to analyze texts and extract meaningful information from them. They are powerful techniques that can be applied to a wide range of historical texts, from letters and diaries to newspapers and official documents. For now we will work with a text from Edgar Allan Poe to practice these techniques. After this session you should be able to apply these techniques to the Salem Witch Trials and think about a research question you want to explore with text analysis.

## Basic vocabulary

**Corpus**: A corpus is a large collection of texts that are used for linguistic analysis and research. In the context of text analysis, a corpus can be made up of various types of texts, such as books, articles, speeches, or social media posts. The purpose of a corpus is to provide a representative sample of language use in a particular domain or context, which can then be analyzed to identify patterns, trends, and other linguistic features. For example, our [Salem Witchcraft Papers](https://salem.lib.virginia.edu/category/swp.html) could be considered a corpus of historical texts related to the Salem Witch Trials.

**Document**: A document is a single piece of text that is part of a larger corpus. In the context of text analysis, a document can be any type of written or spoken material, such as a book, article, email, or speech. Documents are typically analyzed individually or in relation to other documents in the corpus to identify patterns and trends in language use. For example, a letter written by a person accused of witchcraft during the Salem Witch Trials could be considered a document within the larger corpus of texts related to the trials.

**Token**: A token is a single unit of text that is used in natural language processing (NLP) and text analysis. Tokens can be words, phrases, or even individual characters, depending on the level of analysis being performed. In most cases, tokens are created by breaking down a larger piece of text into smaller, more manageable units. For example, the sentence "The quick brown fox jumps over the lazy dog" can be tokenized into individual words: ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]. Tokenization is an important step in many NLP tasks, such as text classification, sentiment analysis, and named entity recognition.

**Stop words**: Stop words are common words that are often removed from text data during natural language processing (NLP) and text analysis. These words are typically considered to be of little value in terms of meaning or context, and their removal can help to reduce noise and improve the accuracy of analysis. Examples of stop words in English include "the", "is", "in", "and", "to", and "a". However, the specific list of stop words can vary depending on the language, domain, and context of the text being analyzed.

**Bag of Words (BoW)**: The Bag of Words (BoW) model is a simple and commonly used technique in natural language processing (NLP) and text analysis. In this model, a piece of text (such as a document or sentence) is represented as a "bag" of its individual words, without considering the order or context in which they appear.

**Machine Learning**: Machine learning is a subset of artificial intelligence (AI) that focuses on the development of algorithms and statistical models that enable computers to learn from and make predictions or decisions based on data. In the context of natural language processing (NLP) and text analysis, machine learning techniques are often used to build models that can automatically classify, cluster, or extract information from text data.

**(Un)supervised Learning**: Supervised learning is a type of machine learning where the model is trained on a labeled dataset, meaning that each input data point is associated with a corresponding output label or target value. The goal of supervised learning is to learn a mapping function that can predict the output label for new, unseen input data based on the patterns learned from the training data. Common supervised learning tasks include classification (e.g., spam detection, sentiment analysis) and regression (e.g., predicting house prices). Unsupervised learning, on the other hand, is a type of machine learning where the model is trained on an unlabeled dataset, meaning that there are no predefined output labels or target values associated with the input data. The goal of unsupervised learning is to identify patterns, structures, or relationships within the data without any prior knowledge of the desired output. Common unsupervised learning tasks include clustering (e.g., grouping similar documents) and dimensionality reduction (e.g., reducing the number of features in a dataset while preserving important information).

## Some important concepts

### Natural Language Processing (NLP)
Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and human (natural) languages. It involves the development of algorithms and models that enable computers to understand, interpret, and generate human language in a way that is meaningful and useful. NLP has a wide range of applications, including:
- Text classification (e.g., spam detection, sentiment analysis)
- Named entity recognition (NER)
- Machine translation (e.g., Google Translate)
- Chatbots and virtual assistants (e.g., Siri, Alexa)
- Text summarization
- Speech recognition
- and many more.
For your historical research, NLP can help you analyze large volumes of text data, extract relevant information, and uncover patterns and trends that may not be immediately apparent through manual analysis. For example, you can use NLP to extract names of people, places, and events from historical documents, analyze the sentiment of letters and diaries, or identify common themes and topics in newspapers and official records.

#### Named Entity Recognition (NER)
Named Entity Recognition (NER) is a subtask of NLP that involves identifying and classifying named entities in a text into predefined categories such as persons, organizations, locations, dates, and more. NER is useful for extracting structured information from unstructured text and can help historians identify key entities and their relationships in historical documents. For example, in a historical text, NER can help identify the names of historical figures, places mentioned, dates of events, and organizations involved. This information can then be used to create timelines, maps, and social networks, or to analyze the roles and relationships of different entities in historical events.
NER - same as NLP - is based on machine learning models that have been trained on large datasets of annotated text. These models learn to recognize patterns in the text and can then be applied to new, unseen texts to identify named entities.

### Text Preprocessing
Text preprocessing is a crucial step in NLP that involves cleaning and transforming raw text data into a format that is suitable for analysis. Common text preprocessing techniques include:
- Tokenization: Splitting text into individual words or tokens.
- Stemming: Reducing words to their root form (e.g., "running" to "run").
- Lemmatization: Reducing words to their base or dictionary form (e.g., "better" to "good").
- Removing stop words: Eliminating common words that do not carry significant meaning (e.g., "the", "is", "and").
- Lowercasing: Converting all text to lowercase to ensure uniformity.
- Removing punctuation and special characters.

This is important because raw text data can be noisy and inconsistent, and preprocessing helps to standardize the text and reduce its complexity. Even if it seems unusual to convert a text into a form that is more difficult for humans to read, it is necessary for computers to process and analyze the text effectively, especially because you want to focus on the meaning of the words and not on their specific forms. 

### Word Frequency Analysis
Word frequency analysis involves counting the occurrences of each word in a text or a collection of texts. This technique helps identify the most common words and can provide insights into the main themes and topics of the text. For example, in a historical text, word frequency analysis can help identify key terms and concepts that are frequently mentioned, such as "witch", "trial", "accusation", etc. This information can be used to create word clouds, frequency distributions, and other visualizations that highlight the most important words in the text. And often it reveals interesting patterns, e.g. if certain words are used more frequently in specific contexts or time periods.

### N-gram Analysis
N-gram analysis involves examining sequences of 'n' consecutive words (n-grams) in a text. For example, bigrams (2-grams) are pairs of consecutive words, while trigrams (3-grams) are triplets of consecutive words. N-gram analysis can help identify common phrases and patterns in the text. For example, in the sentence "The quick brown fox jumps over the lazy dog", the bigrams would be:
- "The quick"
- "quick brown"
- "brown fox"
- "fox jumps"
- "jumps over"
- "over the"
- "the lazy"
- "lazy dog"

This technique shows how words are used in context and can help identify collocations (words that frequently occur together) and common expressions in the text. For historians, n-gram analysis can reveal important phrases and terminology used in historical documents, which can provide insights into the language and discourse of the time. Compared to word frequency analysis, n-gram analysis provides more context about how words are used together, which can be particularly useful for understanding idiomatic expressions and specific terminology in historical texts.

### TF-IDF (Term Frequency-Inverse Document Frequency)
TF-IDF is a statistical measure used to evaluate the importance of a word in a document relative to a collection of documents (corpus). It combines two metrics:
- Term Frequency (TF): The number of times a word appears in a document.
- Inverse Document Frequency (IDF): A measure of how common or rare a word is across all documents in the corpus.
TF-IDF helps identify words that are significant in a specific document while down-weighting common words that appear frequently across all documents. Compared to simple word frequency analysis or n-gram analysis, TF-IDF provides a more nuanced view of word importance by considering both the frequency of a word in a document and its rarity across the corpus. This makes TF-IDF particularly useful for tasks such as information retrieval, document classification, and topic modeling, where the goal is to identify words that are most relevant to a specific document or topic.

### Topic Modeling
Topic modeling is a technique used to identify and extract topics from a collection of documents. It is an unsupervised machine learning method that analyzes the words in the documents and groups them into topics based on their co-occurrence patterns. Topic modeling can help to identify underlying themes and topics in large collections of historical texts, such as letters, diaries, newspapers, and official records. By analyzing the topics present in the texts, historians can gain insights into the main issues and concerns of a particular time period or social group. Topic modeling can also be used to track changes in topics over time, identify relationships between different topics, and explore the connections between different documents in a corpus.

### Document Clustering
Document clustering is a technique used to group similar documents together based on their content. It is an unsupervised machine learning method that analyzes the words and phrases in the documents and identifies patterns of similarity.

### Sentiment Analysis
Sentiment analysis is a technique used to determine the emotional tone or sentiment expressed in a piece of text. It is a form of natural language processing (NLP) that involves analyzing the words and phrases in the text to identify whether the sentiment is positive, negative, or neutral. For example, you can use sentiment analysis to analyze letters, diaries, or newspaper articles from a particular time period to understand the emotional tone of the texts. This can provide insights into the attitudes and opinions of individuals or groups during that time period, as well as the social and political context in which the texts were written.

## Which to use for your research?
The choice of technique depends on your specific research question and the nature of the text data you are analyzing. Most of the time you will use a combination of these techniques to gain a comprehensive understanding of the text data. For example, you might start with text preprocessing to clean and prepare the data, then use word frequency analysis and n-gram analysis to identify common words and phrases, and finally apply TF-IDF or topic modeling to identify important words and topics in the text. You can also use named entity recognition (NER) to extract specific entities such as names, places, and dates from the text.
Always keep in mind that these techniques are tools to help you analyze and interpret the text data, but they should be used in conjunction with your own knowledge and expertise as a historian. It is important to critically evaluate the results of your analysis and consider the historical context in which the texts were written. Furthermore, most of the methods are not specialised for historical texts, so you might need to adapt them to the specific characteristics of your data. Today we will focus on NER, text preprocessing, word frequency analysis, n-gram analysis and TF-IDF.

## Libraries for Text Analysis Tasks

### spaCy
[SpaCy](https://spacy.io/) is an open-source library for advanced NLP in Python. It provides pre-trained models and tools for various NLP tasks, including tokenization, part-of-speech tagging, named entity recognition (NER), dependency parsing, and more. SpaCy is designed for performance and ease of use, making it a popular choice for NLP applications.

### NLTK
The [Natural Language Toolkit (NLTK)](https://www.nltk.org/) is a comprehensive library for NLP in Python. It offers a wide range of tools and resources for text processing, including tokenization, stemming, lemmatization, parsing, and classification. NLTK also provides access to various corpora and lexical resources, making it a valuable tool for researchers and developers working with text data.

### Gensim
[Gensim](https://radimrehurek.com/gensim/) is a library for topic modeling and document similarity analysis in Python. It is particularly well-suited for handling large text corpora and provides efficient implementations of algorithms such as Latent Dirichlet Allocation (LDA) and Word2Vec. Gensim is widely used for tasks such as topic modeling, document clustering, and semantic similarity analysis.
