#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install scikit-learn


# In[9]:


#calculate the cosine similarity between two strings using the Scikit-learn library
#You can use the 'TfidfVectorizer' class to transform the text into vectors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
text1 = "Data science is an interdisciplinary field."
text2 = "Machine learning is a key component of data science."
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([text1, text2])
cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
print(f'Cosine Similarity between the two strings: {cosine_sim[0][0]}')

