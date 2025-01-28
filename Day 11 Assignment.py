#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Tokenize a sample paragraph into words and sentences


# In[9]:


pip install nltk


# In[10]:


import nltk
nltk.download('punkt')


# In[11]:


nltk.download('punkt_tab')


# In[12]:


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK resources
nltk.download('punkt')  # This ensures the punkt tokenizer models are available

# Sample paragraph
paragraph = """
Natural Language Processing (NLP) is a field of artificial intelligence concerned with the interaction between 
computers and human language. It involves tasks like language understanding, text generation, and language translation. 
In recent years, NLP techniques have improved significantly due to advancements in machine learning and deep learning.
"""

# Tokenize into sentences
sentences = sent_tokenize(paragraph)
print("Sentences:")
for sentence in sentences:
    print(f"- {sentence}")

# Tokenize into words
words = word_tokenize(paragraph)
print("\nWords:")
print(words)

