import streamlit as st
from llm import llm_db_chain

st.title("COOL Shirts: Database Q&A")

question = st.text_input("Question: ")

if question:
    chain = llm_db_chain()
    response = chain.invoke(question)

    st.header("Answer")
    st.write(response)
