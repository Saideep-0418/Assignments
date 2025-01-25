#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program to calculate the sum of all even numbers between 1 and a given positive integer n
def sum_of_even_numbers(n):
    return sum(range(2, n+1, 2))

n = int(input("Enter a positive integer n: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    print(f"The sum of all even numbers between 1 and {n} is: {sum_of_even_numbers(n)}")

