import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate
from google.colab import userdata
import os

GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

foodoptions_template = """Suggest [number] food options for {meal_type} that are {diet_type} and high in protein. The options should be varied, tasty, and practical to prepare. Present the output in a table with the following columns:

| Dish Name | Short Description | Main Ingredients | Approx. Protein (g/serving) |


Variables:

{meal_type} : breakfast / lunch / dinner

{diet_type} : vegetarian / non-vegetarian

⚡ Example Usage:
"Suggest 5 food options for dinner that are vegetarian and high in protein. Present the output in a table with columns: Dish Name, Short Description, Main Ingredients, Approx. Protein (g/serving)."
"""

prompt = PromptTemplate(template=foodoptions_template, input_variables=["meal_type", "diet_type", "number"])
chain = prompt | llm

st.header("Protein Rich Food Options")

st.subheader("Generate food options for your day using Generative AI 🤖")

meal_type = st.text_input("Meal Type")

diet_type = st.text_input("Diet Type")

number = st.number_input("Number of foodoptions", min_value = 1, max_value = 10, value = 1, step = 1)

if st.button("Generate"):
    foodoptions = chain.invoke({"number" : number, "meal_type" : meal_type, "diet_type" : diet_type})
    st.write(foodoptions.content)
