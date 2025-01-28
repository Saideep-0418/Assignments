#!/usr/bin/env python
# coding: utf-8

# In[4]:


# function using regular expressions to extract all email addresses from a given string
import re
def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails
input_text = 'Contact us at support@example.com and sales@example.org.'
emails = extract_emails(input_text)
print(emails)

