import streamlit as st
import pandas as pd
st.title('Home Page')
# st.markdown('Welcome to the Home Page')
st.write('Welcome to the Home Page')

st.divider()
col1,col2,col3,col4 = st.columns(4)
col1.metric('Patients',326)
col2.metric('Doctors',21)
col3.metric('Appointments',54)
col4.metric('Revenue','12.5 Lakhs' )
st.divider()

left,right = st.columns([2,1])
with left:
    st.subheader('Monthly Patients')
    chart = pd.DataFrame({
        'Month':['Jan','Feb','Mar','Apr','May','Jun'],
        'Patients': [120,430,230,180,234,321]
    })
    st.line_chart(chart.set_index('Month'))
with right:
    st.subheader('Departments')
    departments = pd.DataFrame({
        'Department': [
            'Cardiology',
            'Dental',
            'Neurology',
            'Orthopedistry'
        ],
        'Doctors':[5,4,7,3]
    })
    st.dataframe(
        departments,
        use_container_width=True
    )