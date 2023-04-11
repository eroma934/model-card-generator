import streamlit as st

for k, v in st.session_state.items():
    st.session_state[k] = v

def main():
    st.markdown('# Uses')
    st.markdown("This section addresses questions around how the model is intended to be used, discusses the foreseeable users of the model (including those affected by the model), and describes uses that are considered out of scope or misuse of the model.")
    left, right = st.columns([2,4])
    
    with left: 
        st.write("\n")
        st.write("\n")
        st.markdown('### Direct Use:')
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        #st.write("\n")
        st.markdown('### Downstream Use [Optional]:')
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown('### Out-of-Scope Use:')
        
    with right:
        st.text_area(" ",help="How can this model be used, without additional post-processing or further pipeline work?", key="direct_user")
        st.text_area(" ",help="How can this model be used, when incorporated into another system?",key="downstream_use")
        st.text_area(" ", help="What tasks will the model not work for?", key="oos_use")  

if __name__ == '__main__':
    main()
    if "model_name" in st.session_state:
        downloaded_file_name = st.session_state.model_name+'_'+'model_card.md'
        st.sidebar.download_button(label = 'Download Model Card', data = '''this is a test''',file_name = downloaded_file_name, help = "The current model card will be downloaded as a markdown (.md) file")