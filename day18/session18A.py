import streamlit as st
st.title('Agentic UI Demo')

home_page = st.Page('session18B.py',title='Home',icon='🏠')
chat_page = st.Page('session18C.py',title='AI chat')
patients_page = st.Page('session18D.py',title='Patients')

pg = st.navigation([home_page,chat_page,patients_page])
pg.run()