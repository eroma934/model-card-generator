import streamlit as st

for k, v in st.session_state.items():
    st.session_state[k] = v
  

def main():
    st.markdown('# Training Details')
    st.write("Provide an overview of the Training Data and Training Procedure for this model")
    left, middle, right = st.columns([2,1,7])

    with left: 
        st.write("\n")
        st.write("\n")
        st.markdown('## Training Data:')
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
    with middle:
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown(' \n ## Training Procedure')
    with left:
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
       
        st.markdown('#### Preprocessing Steps:')
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown('#### Training Time:')
        
    with right:
        #soutput_jinja = parse_into_jinja_markdown()
        
        st.text_area(" ", help ="Ideally this links to a Dataset Card.", key="training_data")
        #st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        
        st.text_area(" ",key="model_preprocessing")
        st.text_area(" ", help = "This section provides information about throughput, start/end time, checkpoint size if relevant, etc.", key="training_time")
   
   
   
   
    

if __name__ == '__main__':
    main()
    if "model_name" in st.session_state:
        downloaded_file_name = st.session_state.model_name+'_'+'model_card.md'
        st.sidebar.download_button(label = 'Download Model Card', data = '''this is a test''',file_name = downloaded_file_name, help = "The current model card will be downloaded as a markdown (.md) file")