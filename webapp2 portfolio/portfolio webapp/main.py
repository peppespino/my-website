import streamlit as st
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image('images/photo.png',width=550)
with col2:
    st.title("Giuseppe D'Aiello")
    contest="""
    Mi chiamo Giuseppe D'Aiello,
     sono un appassionato di informatica con un forte interesse per la programmazione e sto attualmente studiando Python,
      con l'obiettivo di diventare un esperto specializzato in intelligenza artificiale. 
      Questo sito è una raccolta dei miei progetti in Python, 
      una sorta di repository per esplorare le app che ho sviluppato lungo il mio percorso di apprendimento e crescita.
    
    """
    st.info(contest)