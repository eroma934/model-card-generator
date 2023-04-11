import streamlit as st

for k, v in st.session_state.items():
    st.session_state[k] = v

def main():
    st.markdown('# Bias, Risks, and Limitations')
    st.text_area("What are the known or foreseeable issues stemming from this model? Use this section to convey both technical and sociotechnical limitations",help="Provide an overview of the possible Limitations and Risks that may be associated with this model", key="risks")

if __name__ == '__main__':
    main()