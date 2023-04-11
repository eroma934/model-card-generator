import streamlit as st

for k, v in st.session_state.items():
    st.session_state[k] = v

def main():

    st.markdown('# Citation [Optional]')
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
        st.text_area(" ", key="citation_bibtex")
        st.text_area(" ", key="citation_apa")

if __name__ == '__main__':
    main()