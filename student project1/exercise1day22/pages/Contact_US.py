import pandas
import streamlit as st
import pandas as pd
from send_email import send_email


st.header('Contact Me')

with st.form(key='email_forms'):
    user_email = st.text_input('Il tuo indirizzo Mail',placeholder='utente@esempio.com')

    topics=pandas.read_csv('topics.csv',)

    opzione_selezionata = st.selectbox("Di cosa vuoi parlarmi:", topics['topic'])


    st.write(f"Hai selezionato: {opzione_selezionata}")

    message = st.text_area('IL tuo messaggio',placeholder='Ciao Giuseppe...')
    #message = message + '\n' + user_email
    message=f"""\
Subject: New email from {user_email}

topic: {opzione_selezionata}
{message}
inviata da: {user_email}

"""
    button = st.form_submit_button('Submit')
    if button:
        send_email(message)
        st.success("Email inviata con successo!")