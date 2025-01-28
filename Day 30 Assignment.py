#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install textblob


# In[6]:


#perform sentiment analysis on a given text using the TextBlob library 
#Display whether the sentiment is positive, negative, or neutral.

from textblob import TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
text = """I love the new design of the product! It is absolutely amazing and works perfectly."""
sentiment = analyze_sentiment(text)
print(f"Sentiment: {sentiment}")


# In[7]:


from textblob import TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
text = """I am not happy with the service, it was disappointing."""
sentiment = analyze_sentiment(text)
print(f"Sentiment: {sentiment}")


# In[ ]:





# In[ ]:




