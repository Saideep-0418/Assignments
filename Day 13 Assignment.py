#!/usr/bin/env python
# coding: utf-8

# In[4]:


# function to clean a given text by removing special characters and converting it to lowercase. 
# Test it with the input: 'Hello, World! Welcome to NLP 101.'

import re
def clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
    return cleaned_text
input_text = 'Hello, World! Welcome to NLP 101.'
cleaned_text = clean_text(input_text)
print(cleaned_text)

