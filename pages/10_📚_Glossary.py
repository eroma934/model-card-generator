import streamlit as st

for k, v in st.session_state.items():
    st.session_state[k] = v

def main():

    st.markdown('# Glossary [optional]')
    st.text_area("Terms used in the model card that need to be clearly defined in order to be accessible across audiences go here.",height = 200, key="glossary")
   

if __name__ == '__main__':
    main()