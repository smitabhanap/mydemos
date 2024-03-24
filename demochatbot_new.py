#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install streamlit


# In[5]:


# Define a function to handle user questions and return answers
#import streamlit as st
def get_answer(question):
    # Replace this with your actual logic to generate answers
    if "hello" in question.lower():
        return "Hi there! How can I help you?"
    elif "goodbye" in question.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that question."


# In[6]:


# Define the Streamlit app
#def main():
    st.title("Question-Answer Chatbot")
    st.write("Ask me anything!")

    # Add a text input for the user to type their question
    user_question = st.text_input("Enter your question here:")

    # When the user submits a question, display the answer
    if st.button("Ask"):
        answer = get_answer(user_question)
        st.text_area("Answer:", value=answer, height=100)
        # Run the Streamlit app
if __name__ == "__main__":
    main()


# In[8]:


#streamlit run demochatbot.py


# In[9]:


#streamlit run C:\Users\Smita\anaconda3\lib\site-packages\demochatbot.py 


# In[10]:


#streamlit run C:/Users/Smita/anaconda3/lib/site-packages/demochatbot.py 


# In[11]:


#pip install streamlit


# In[12]:


#streamlit hello


# In[16]:


import streamlit as st
import pandas as pd

 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("D:/AY 23-24/QA.csv")
st.line_chart(df)


# In[15]:


print(pd. __version__)


# In[17]:


streamlit demochatbot.py


# In[ ]:




