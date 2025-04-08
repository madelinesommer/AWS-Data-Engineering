import streamlit as st
import boto3
from io import BytesIO
from datetime import date
from dateutil.relativedelta import relativedelta

s3 = boto3.client('s3')

bucket_name = "maddy-sommer-app-data"

st.title("Budget Calculator")

with st.form("budget_form", enter_to_submit=True) as form:
    #choices = st.multiselect(label="Pick an item", options=["Apple", "Banana"])
    project_title = st.text_input("Please enter the project title:")

    start_date = st.date_input(label="Please enter the start date of the project:", value="today", format="DD/MM/YYYY")
    
    end_date = st.date_input(label="Please enter the end date of the project:", value="today", format="DD/MM/YYYY")
    
    submitted = st.form_submit_button("Submit")

    if submitted and start_date and end_date:
        period = relativedelta(end_date, start_date)

        years = period.years
        months = period.months
        days = period.days

        st.write(f"The length of the project is: {years} years, {months} months, {days} days")

        rows = int(years)
        for row in range(rows):
            cols = st.columns(3)
            with cols[0]:
                st.markdown(f"### Year {row + 1}") 

            with cols[1]:
                choices = st.multiselect(label="Pick an item", options=["Apple", "Banana"],  key=f"year_{row}_item" )
            
        