#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Creating a list with 5 elements
my_list = [10, 20, 30, 40, 50]
print("Element at index 2:", my_list[2])  # Accessing the 3rd element (30)
print("Element at index 0:", my_list[0])  # Accessing the 1st element (10)
print("Element at index -1:", my_list[-1])  # Accessing the last element (50)


# In[2]:


# Creating a tuple with 5 elements
my_tuple = (100, 200, 300, 400, 500)
print("Element at index 3:", my_tuple[3])  # Accessing the 4th element (400)
print("Element at index 1:", my_tuple[1])  # Accessing the 2nd element (200)
print("Element at index -2:", my_tuple[-2])  # Accessing the 2nd last element (400)


# In[3]:


# Creating a dictionary with 5 key-value pairs
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York',
    'job': 'Engineer',
    'country': 'USA'
}
print("Name:", my_dict['name'])  # Accessing value using key 'name'
print("Age:", my_dict['age'])  # Accessing value using key 'age'
print("City:", my_dict['city'])  # Accessing value using key 'city'

