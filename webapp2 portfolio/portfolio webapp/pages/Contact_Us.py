import streamlit as st
from send_email import send_email


st.header('Contact Me')

with st.form(key='email_forms'):
    user_email = st.text_input('Il tuo indirizzo Mail',placeholder='utente@esempio.com')
    message = st.text_area('IL tuo messaggio',placeholder='Ciao Giuseppe...')
    #message = message + '\n' + user_email
    message=f"""\
Subject: New email from {user_email}
{message}
inviata da: {user_email}

"""
    button = st.form_submit_button('Submit')
    if button:
        send_email(message)
        st.success("Email inviata con successo!")