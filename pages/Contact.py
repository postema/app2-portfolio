import streamlit as st

st.header("Contact Aanvraag")

with st.form(key="email_form"):
    user_email = st.text_input("Uw email adres")
    message = st.text_area("Uw bericht")
    button = st.form_submit_button("Indienen")
    if button:
        print(user_email)
        print(message)
