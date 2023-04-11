import streamlit as st

for k, v in st.session_state.items():
    st.session_state[k] = v

def main():

    st.markdown('# Citation')
    st.write("If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section")
    left, right = st.columns([2,4])

    with left: 
        st.write("\n")
        st.write("\n")
        st.markdown('### BibTeX:')
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown('### APA:')
        
        
    with right:
        st.text_area(" ", key="bibtex_citation")
        st.text_area(" ", key="apa_citation")

if __name__ == '__main__':
    main()
    if "model_name" in st.session_state:
        downloaded_file_name = st.session_state.model_name+'_'+'model_card.md'
        st.sidebar.download_button(label = 'Download Model Card', data = '''this is a test''',file_name = downloaded_file_name, help = "The current model card will be downloaded as a markdown (.md) file")