#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install spacy


# In[ ]:


python -m spacy download en_core_web_sm


# In[7]:


# perform Named Entity Recognition (NER) on a given text using SpaCy. Print the entities and their types
import spacy
nlp = spacy.load("en_core_web_sm")
text = """Apple is looking to buy a startup in the United Kingdom for $1 billion. 
          Microsoft, on the other hand, is planning to invest in a new AI project next year."""
doc = nlp(text)
print("Entities and their types:")
for ent in doc.ents:
    print(f"{ent.text} -> {ent.label_}")

