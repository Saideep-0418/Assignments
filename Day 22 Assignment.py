#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install spacy


# In[5]:


#perform part-of-speech tagging on the sentence: 'NLP is amazing and fun to learn.' using SpaCy
import spacy
nlp = spacy.load('en_core_web_sm')
sentence = 'NLP is amazing and fun to learn.'
doc = nlp(sentence)
for token in doc:
    print(f'{token.text}: {token.pos_}')

