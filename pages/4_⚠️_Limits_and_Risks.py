import streamlit as st

for k, v in st.session_state.items():
    st.session_state[k] = v

def main():
    st.markdown('# Bias, Risks, and Limitations')
    st.text_area("What are the known or foreseeable issues stemming from this model? Use this section to convey both technical and sociotechnical limitations",help="Provide an overview of the possible Limitations and Risks that may be associated with this model", key="risks")

if __name__ == '__main__':
    main()
    if "model_name" in st.session_state:
        downloaded_file_name = st.session_state.model_name+'_'+'model_card.md'
        st.sidebar.download_button(label = 'Download Model Card', data = '''this is a test''',file_name = downloaded_file_name, help = "The current model card will be downloaded as a markdown (.md) file")