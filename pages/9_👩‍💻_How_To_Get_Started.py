import streamlit as st

for k, v in st.session_state.items():
    st.session_state[k] = v

def main():
    
    st.markdown('# How to Get Started with the Model')
    st.text_area("Code snippet to show how to use the model.",height = 300, key="how_to")
   
        

if __name__ == '__main__':
    main()
    if "model_name" in st.session_state:
        downloaded_file_name = st.session_state.model_name+'_'+'model_card.md'
        st.sidebar.download_button(label = 'Download Model Card', data = '''this is a test''',file_name = downloaded_file_name, help = "The current model card will be downloaded as a markdown (.md) file")