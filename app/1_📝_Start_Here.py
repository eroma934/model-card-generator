import streamlit as st
from pathlib import Path
from streamlit_extras.switch_page_button import switch_page


for k, v in st.session_state.items():
    st.session_state[k] = v

def main():
    st.header("About")
    st.markdown(Path('about.md').read_text(), unsafe_allow_html=True)
    st.header("Get Started")
    st.text_input("Enter Model Name", key="model_name")
    if st.session_state["model_name"] != "":
        switch_page("Model Details")

if __name__ == '__main__':
    main()