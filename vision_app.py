from dotenv import load_dotenv # for access key from .env file
import os
import google.generativeai as genai
import streamlit as st
from PIL import Image # for image

load_dotenv()

# for run --> streamlit run filename
api_key=os.getenv("Google_Api_key")
genai.configure(api_key=api_key)

# this func take two input and pass to the gemini LLM model
# this model deal with image or message 

def get_gemini_response(prompt,uploaded_image):
    model=genai.GenerativeModel('gemini-1.5-flash')   # another model-->gemini-pro(to deal with chat message)
    if prompt !="":   # if prompt is given then both parameter give give in the output(image/peompt)
        response=model.generate_content([prompt,uploaded_image])
    else:   #only image is given if prompt not given 
        response=model.generate_content(uploaded_image)
    return response.text
    

st.set_page_config("gemini chatbot")  # work as a title
st.header("Chatbot Application Using Gemini")  # heading tag
# input box
input = st.text_input("Input here : ",key='input')
uploaded_file=st.file_uploader("Choose an image ...",type=['jpeg','jpg','png'])

# prompt--> messages which is pass to the llm model(generative ai)

image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    # image rendering on string
    st.image(image,'uploaded image',use_column_width=True)    # image function
    
# input,image---> pass to the LLM model

submit = st.button('SUBMIT')
# if submit button is clicked
if submit:
    response=get_gemini_response(prompt=input,uploaded_image=image)
    st.subheader("Your Response is ::")
    st.write(response)
    
    
    
    
    
    
