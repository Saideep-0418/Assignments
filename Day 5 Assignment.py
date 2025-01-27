#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Function to calculate word frequency
def word_frequency(text):
    text = text.lower()
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    for word, count in word_count.items():
        print(f"'{word}': {count}")
text = """Python is great, and Python is easy to learn. Learning Python is fun."""
word_frequency(text)

