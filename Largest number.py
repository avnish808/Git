#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# In[3]:


def app():
    # Seting the title of the app
    st.title('Find the largest number among these:')

    # Create input fields for the three numbers
    a = st.number_input('Enter the First number:')
    b = st.number_input('Enter the Second number:')
    c = st.number_input('Enter the Third number:')

    # Call the find_largest_num function to compute the largest number
    largest_num = largest_number(a, b, c)

    # Display the largest number to the user
    st.write('The largest number is:', largest_num)


# In[ ]:


if __name__ == '__main__':
    app()

