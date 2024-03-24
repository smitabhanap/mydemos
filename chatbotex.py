import streamlit as st
import pandas as pd

 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("D:/AY 23-24/QA.csv")
st.line_chart(df)




print(pd. __version__)
