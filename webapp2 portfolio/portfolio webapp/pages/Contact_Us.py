import streamlit as st
st.header('Contact Me')

with st.form(key='email_forms'):
    user_email = st.text_input('Il tuo indirizzo Mail',placeholder='utente@esempio.com')
    message = st.text_area('IL tuo messaggio',placeholder='Ciao Giuseppe...')
    button = st.form_submit_button('Submit')
    if button:
        print('hello')