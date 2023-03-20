import streamlit as st
from send_email import send_email

st.header("Contact Aanvraag")

with st.form(key="email_form"):
    user_email = st.text_input("Uw email adres")
    raw_message = st.text_area("Uw bericht")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Indienen")
    if button:
        send_email(message)
        st.info("Uw bericht is verzonden.")
