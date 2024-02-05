import os 
import json 
import traceback
import pandas as pd 
from dotenv import load_dotenv
from src.MCQ_Generator.utils import read_file, get_table_data
import streamlit as st 
from langchain.callbacks import get_openai_callback
from src.MCQ_Generator.MCQGenerator import generate_evaluate_chain
from src.MCQ_Generator.logger import logging


# load json file
with open ('C:/Users/6917/PycharmProjects/Generative AI/MCQ_Generator/Response.json','r') as f:
    RESPONSE_JSON = json.load(f)


# creating the title of for the app 
st.title("MCQs Creator Application with LangChain 🦜🔗")

# create form 
with st.form("user_inputs"):
    # upload a file
    uploaded_file = st.file_uploader("Upload a PDF or txt file")

    # Input fields
    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=50)

    # subject 
    subject = st.text_input("Insert subject", max_chars=20)

    # Quiz Tone
    tone = st.text_input("Complexity level of Questions", max_chars=20, placeholder="Simple")

    # button 
    button = st.form_submit_button("Create MCQs")


    # check if the button is clicked and all the fields have input
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Loading 🏃🏿🏃‍♂️🏃‍♀️"):
            try:
                text = read_file(uploaded_file)

                # count tokens and the cost of the API Call
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain({
                        "text": text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone": tone, 
                        "response_json": json.dumps(RESPONSE_JSON)
                    })
            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                raise e
            else:
                print(f"Total Tokens: {cb.total_tokens}")
                print(f"Prompt Tokens: {cb.prompt_tokens}")
                print(f"Completion Tokens: {cb.completion_tokens}")
                print(f"Total Costs: {cb.total_cost}")

                if isinstance(response, dict):
                    # extract the quiz data from the response
                    quiz = response.get("quiz", None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index +1
                            st.table(df)
                            # display the review in a text box
                            st.text_area(label="Review", value=response["review"])
                        else: 
                            st.error("Error is the table data")
                else:
                    st.write(response)

    



