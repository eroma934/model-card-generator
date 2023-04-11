import streamlit as st

for k, v in st.session_state.items():
    st.session_state[k] = v

def main():
    
    st.markdown('# How to Get Started with the Model')
    st.text_area("Code snippet to show how to use the model.",height = 300, key="how_to")
   
        

if __name__ == '__main__':
    main()