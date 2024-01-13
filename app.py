# Q&A ChatBot

# Using langenv here
from langchain.llms import OpenAI

#from dotenv import load_dotenv

#load_dotenv() # take environment variables from .env

import streamlit as st
import os

## Function to load OpenAI model and get responses

def get_openai_response(question, input_key):
    llm = OpenAI(openai_api_key=input_key,
                 # Currently uses Base Model
                 #model_name="gpt-3.5-turbo-instruct",
                 temperature=0.5)

    response = llm(question)
    return response

## initialize our streamlit app
    
st.set_page_config(page_title = "Q&A Demo")

st.header("Langchain Application")

input_key = st.text_input("Enter OpenAI Key: ", key="input_key", type="password")

input = st.text_input("Input Question: ", key="input")

if input_key != "":
    try: 
        response = get_openai_response(input, input_key)

        submit = st.button("Ask the question")

        ## If ask button is clicked

        if submit:
            st.subheader("The Response is")
            st.write(response)
    except:
        st.write("Incorrect API Key")


            