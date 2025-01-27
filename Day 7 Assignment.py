#!/usr/bin/env python
# coding: utf-8

# In[3]:


#program to using NLTK and Spacy. Convert text to lowercase, Remove stopwords using NLTK.
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nlp = spacy.load("en_core_web_sm")
def process_text(text):
    text = text.lower()
    doc = nlp(text)
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token.text for token in doc if token.text not in stop_words and not token.is_punct]
    return " ".join(filtered_tokens)
text = """Python is great for natural language processing. It is easy to learn and very powerful."""
processed_text = process_text(text)
print("Processed Text:", processed_text)

