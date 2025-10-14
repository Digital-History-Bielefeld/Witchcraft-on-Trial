# Session 5: Working with your own data

In this session, we will focus on applying the techniques and tools we have learned in previous sessions to your own historical text data. For this we will work with the Salem Witch Trial transcripts, which you can find in the `data/` folder. We will go through the process of loading, preprocessing, analyzing, and visualizing your own text data using Python and various libraries such as SpaCy, NLTK, Matplotlib, and others. 
You can choose to work with the entire dataset or select specific transcripts that interest you for your research. You can focus on one technique that you found particularly interesting in the previous sessions or combine multiple techniques to gain deeper insights into the text data. Try to formulate a specific research question that you want to answer using the text data. This will help you to focus your analysis and choose the appropriate techniques and tools.

## How to start
1. First, make sure you have all the necessary libraries installed in your codespace. We worked with the following libraries in the previous sessions:
   - SpaCy
   - NLTK
   - Gensim
   - Matplotlib
   - WordCloud

You can install any missing libraries using pip. 

NLTK:
```bash
pip install nltk
```

spaCy:
```bash
pip install -U pip setuptools wheelpip install -U pip setuptools wheel
pip install spacy
python -m spacy download en_core_web_md # choose the model you want to work with
```

gensim:
```bash
pip install --upgrade gensim
```

matplotlib:
```bash
pip install matplotlib
```

wordcloud:
```bash
pip install wordcloud
```

2. Next, you can create a new Python file in the `session_5/` folder. You can name it `exercise.py` or any other name you prefer. To create a new file, you can click on the "New File" button in the file explorer of your codespace and enter the desired name.

3. Now you can start writing your code in the new file. You can use the code snippets and functions from the previous exercises as a starting point. Make sure to import the necessary libraries at the beginning of your script. You can also copy and paste code from the previous exercises if you find it useful for your analysis. There is also a `helpers` folder, which contains all our functions from the previous sessions. You can just copy them into your new file and use them.
