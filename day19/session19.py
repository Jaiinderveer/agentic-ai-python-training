import streamlit as st
st.title('Agentic UI Demo')

home_page = st.Page('session19A.py',title='Home',icon='🏠')
chat_page = st.Page('session19B.py',title='AI chat')
patients_page = st.Page('session19C.py',title='Patients')
voice_page = st.Page('session19D.py',title='Agent')

pg = st.navigation([home_page,chat_page,patients_page,voice_page])
pg.run()