import streamlit as st

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def submit_message():
    message = st.success('Formularz został przesłany!', icon="✅")
    return message

with st.form("form", clear_on_submit=True):
    imie = st.text_input("Proszę podać imię")
    nazwisko = st.text_input("Proszę podać nazwisko")

    submit = st.form_submit_button("Prześlij formularz", on_click=submit_message)

