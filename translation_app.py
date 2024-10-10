import os
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import streamlit as st

llm_model = ChatGroq(model='gemma2-9b-it', groq_api_key=os.environ['GROQ_API_KEY'])

generic_prompt = """Translate the following text from English to 
{language}"""

prompt = ChatPromptTemplate.from_messages([
    ("system", generic_prompt),
    ("user", "{input}")
])

parser = StrOutputParser()

chain = prompt | llm_model | parser

st.title('Language Translation App using GROQ')
input_text = st.text_area('Enter the text to translate')

if input_text:
    language = st.selectbox('Select the language', ['French', 'Spanish', 'German','Hindi','Kannada'])
    language_code = {'French': 'fr', 'Spanish': 'es', 'German': 'de','Hindi':'hn','Kannada':'kn'}[language]
    translated_text = chain.invoke({'input': input_text, 'language': language_code})
    st.write(translated_text)

