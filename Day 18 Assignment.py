#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests beautifulsoup4


# In[2]:


# fetch and print the title of a webpage using the 'requests' and 'BeautifulSoup' libraries
import requests
from bs4 import BeautifulSoup

def fetch_title(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the title tag and get its text
        title = soup.title.string if soup.title else 'No title found'
        return title
    else:
        return f"Failed to retrieve webpage. Status code: {response.status_code}"

# Test the function with the URL 'https://example.com'
url = 'https://example.com'
title = fetch_title(url)
print(f"Title of the webpage: {title}")

