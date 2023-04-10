import streamlit as st
from persist import load_widget_state



global variable_output

def main():
    cs_body()

def cs_body():
    
    st.markdown('# Bias, Risks, and Limitations')
    st.text_area("What are the known or foreseeable issues stemming from this model? Use this section to convey both technical and sociotechnical limitations",help="Provide an overview of the possible Limitations and Risks that may be associated with this model", key="risks")

if __name__ == '__main__':
    load_widget_state()
    main()