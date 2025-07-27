import streamlit as st
from connect_memory_to_llm import chain as qa_chain

st.title("Wikipedia chatbot")
st.write("A ai chatbot that can answer questions related to Python, Artificial intellignece and Internet of things using a knowledge base from wikipedia.")
text_query = st.text_area(height=250,placeholder="Enter your query here..",label="Write your query")
submit_button = st.button("Enter")


if submit_button or text_query:
   response = qa_chain.invoke({"input":text_query})
   st.chat_message("ai").markdown(response["answer"])