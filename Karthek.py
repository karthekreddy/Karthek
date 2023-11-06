#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[8]:


import random
number= random.randint(1,100)
your_number=0
chance=0

while chance < 5:
    your_number= int(input("enter your_number"))
    if(your_number == number):
        print("congratulations, ur guess is correct", number)
        break;
    elif(your_number>number):
        print("choose a lesser number")
    else:
        print("choose a higher number")


# In[ ]:




