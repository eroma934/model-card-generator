import streamlit as st

for k, v in st.session_state.items():
    st.session_state[k] = v

def main():

    st.markdown('# Glossary [optional]')
    st.text_area("Terms used in the model card that need to be clearly defined in order to be accessible across audiences go here.",height = 200, key="glossary")
   

if __name__ == '__main__':
    main()
    if "model_name" in st.session_state:
        downloaded_file_name = st.session_state.model_name+'_'+'model_card.md'
        st.sidebar.download_button(label = 'Download Model Card', data = '''this is a test''',file_name = downloaded_file_name, help = "The current model card will be downloaded as a markdown (.md) file")