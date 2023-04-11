import streamlit as st

for k, v in st.session_state.items():
    st.session_state[k] = v

def main(): 
    st.markdown('# More Information [optional]')
    st.text_area("Any additional information",height = 200, key="more_info")
     

if __name__ == '__main__':
    main()