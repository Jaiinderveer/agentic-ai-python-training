import streamlit as st
import pandas as pd
st.title('All Patients')
st.markdown('Welcome to the All Patients Page')

patients = {
    'ID': [101,102,103,104,105],
    'NAME': ['John','Jim','Jack','Joe','Fionna'],
    'AGE': [34,23,56,77,31],
    'GENDER': ['male','male','male','male','female'],
    'DISEASE': ['Diabetes','BP','Asthma','BP','Diabetes'],
    'DOCTOR': ['Dr Rahul','Dr Anna','Dr George','Dr Anna','Dr Rahul']
}

patients_data = pd.DataFrame(patients)
st.dataframe(
    patients,
    use_container_width=True
)
st.divider()