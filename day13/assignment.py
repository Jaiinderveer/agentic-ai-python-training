import streamlit as st
from session13C import User
from session13 import DBHelper

st.title("User Registration")

# Form
with st.form("registration_form"):

    name = st.text_input("Enter Full Name")
    phone = st.text_input("Enter Phone")
    email = st.text_input("Enter Email")
    password = st.text_input("Enter Password", type="password")

    submitted = st.form_submit_button("Register")

if submitted:
    if name.strip() == "":
        st.error("Name cannot be empty.")

    elif phone.strip() == "":
        st.error("Phone number cannot be empty.")

    elif email.strip() == "":
        st.error("Email cannot be empty.")

    elif "@" not in email or "." not in email:
        st.error("Enter a valid email address.")

    elif len(password) < 6:
        st.error("Password must contain at least 6 characters.")

    else:
        try:
            user = User(name, phone, email, password)

            document = user.to_dictionary()

            db_helper = DBHelper()
            db_helper.select_collection()
            db_helper.save(document)

            st.success("✅ User Registered Successfully!")

            st.info(f"Welcome {name}!")

        except Exception as e:
            st.error(f"Database Error: {e}")