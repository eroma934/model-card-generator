import streamlit as st
from utilities.markdown_utils import parse_into_jinja_markdown as pj

for k, v in st.session_state.items():
    st.session_state[k] = v

def main(): 
    st.markdown('# Download Model Card')   

if __name__ == '__main__':
    main()    
    if "model_name" in st.session_state:
        downloaded_file_name = st.session_state.model_name+'_'+'model_card.md'
        st.download_button(label = 'Download Model Card', data =  pj(),file_name = downloaded_file_name, help = "The current model card will be downloaded as a markdown (.md) file")