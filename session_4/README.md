# Session 4: Data Visualization techniques

In this session, we will explore the fundamentals of data visualization and learn how to use Python tools to represent information graphically.
We will discuss why visualization is important in research, what types of data can be visualized, and how to design effective visualizations that clearly communicate insights.
The practical exercises will focus on Matplotlib (for static visualizations) and DisplaCy (for linguistic visualizations).

## Some important concepts

###Why Visualizations?

Data visualization transforms complex datasets into clear, interpretable, and engaging visual forms.
In historical and textual research, visualizations help us:
- Reveal patterns, trends, and anomalies in the data.
- Communicate complex findings to others in an accessible way.
- Combine qualitative interpretation with quantitative evidence.
- Support storytelling and argumentation through visual means.

A good visualization does not decorate your data – it helps you think.

---

### What to Visualize
Depending on your research question and data type, you might visualize:
- Text-based data: word frequencies, named entities, or keyword distributions.
- Quantitative historical data: population trends, event counts, or changes over time.
- Relationships and structures: co-occurrences of people, places, or concepts.

The most important step is to match the data type with the right kind of visualization.
For example:
- Frequencies → bar charts or histograms
- Changes over time → line charts
- Relationships → network or dependency graphs
- Linguistic data → entity visualizations (using DisplaCy)

---

### Rules and Best Practices for Visualizations
When designing data visualizations, clarity and honesty are key.
Some essential principles include:
- Clarity first: Remove unnecessary elements and avoid clutter.
- Consistency: Use the same scales, units, and colors where possible.
- Label everything: Axes, titles, and legends make your data interpretable.
- Use color meaningfully: Highlight key insights rather than decorating.
- Provide context: Explain what the viewer is seeing.
- Avoid distortion: Never manipulate scales or proportions to change perception.
- Tell a story: Every chart should communicate a clear message.

Simplicity and clarity are more powerful than complexity.

---

## Libraries for Data Visualization Tasks

### Matplotlib
[Matplotlib](https://matplotlib.org/) is a widely used Python library for creating static visualizations.
It provides a flexible framework for generating a wide range of plots — including line plots, bar charts, scatter plots, and histograms.
Matplotlib is highly customizable, allowing full control over all visual elements such as colors, fonts, axes, and legends.

#### Typical use cases in this course:
- Visualizing word frequencies or term distributions.
- Displaying temporal changes in your data.
- Creating comparative bar charts or simple scatter plots.

#### Example:
```python
import matplotlib.pyplot as plt

plt.bar(words, counts)
plt.title("Word Frequency in Trial Records")
plt.xlabel("Word")
plt.ylabel("Count")
plt.savefig('my_file.png')
```

Use Matplotlib for clear, static visualizations suitable for reports and publications.


---
### DisplaCy
[DisplaCy](https://spacy.io/usage/visualizers) is a web-based visualization tool included in the spaCy library.
It is designed specifically for linguistic data, helping you visualize named entities and syntactic dependencies directly from your text.

#### Why use DisplaCy:
- It makes linguistic structure visible at a glance.
- You can highlight entities such as names, places, or dates.
- It’s excellent for exploring NER (Named Entity Recognition) results from your NLP pipeline.

#### Example:
```python
from spacy import displacy
doc = nlp("Goody Proctor was accused by Abigail Williams in Salem.")
displacy.serve(doc, style="ent")
```

Use DisplaCy when you want to visualize the results of your text analysis — especially entities and relationships.

---

## Choosing and Evaluating Visualizations
When deciding how to visualize your data, always start with your research question, not with a chart type.
Ask yourself:
1. What story do I want to tell?
2. Who is my audience?
3. What type of data am I working with?
4. Do I want the viewer to explore or to understand?

The best visualization is the one that answers your question most clearly.

## Summary
- Visualization is not decoration — it is a form of analysis.
- Every chart should have a clear purpose and message.
- Simplicity, clarity, and consistency are the keys to good visual design.
- Use Matplotlib for static, data-driven plots.
- Use DisplaCy for linguistic and text-structure visualizations.
