import streamlit as st
from utilities.markdown_utils import parse_into_jinja_markdown as pj

for k, v in st.session_state.items():
    st.session_state[k] = v
  

def main():
    st.markdown('# Training Details')
    st.write("Provide an overview of the Training Data and Training Procedure for this model")
    left, right = st.columns([3,7])

    with left: 
        st.write("\n")
        st.write("\n")
        st.markdown('## Training Data:')
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown('## Training Procedure')
    with left:   
        st.markdown('#### Data Collection & Preprocessing Steps:')
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
        
        st.text_area("Training Data", help ="Ideally this links to a Dataset Card.", key="training_data", label_visibility="hidden")
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