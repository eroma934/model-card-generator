import streamlit as st
import json

for k, v in st.session_state.items():
    st.session_state[k] = v

with open("./static/model-tags.json") as f:
    tags_json = json.load(f)
    library = tags_json["library"]
    libraries = [x["id"] for x in library]

def main():
    
    st.markdown('# Technical Specifications [optional]')
    st.write("Provide an overview of any additional technical specifications for this model")
    left, right = st.columns([2,4])
    

    with left: 
        st.write("\n")
        st.write("\n")
        st.markdown('### Model Architecture and Objective:')
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown('### Compute Infrastructure:')
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
       
        st.markdown('##### Hardware:')
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown('##### Software:')
        
    with right:
        st.text_area(" ", key="model_specs")
        st.text_area(" ",key="compute_infrastructure")
        st.text_area(" ", key="model_hardware")
        st.multiselect(" ",[""]+libraries, key="libraries", help="Select the main libraries for the model.")
         
if __name__ == '__main__':
    main()
    if "model_name" in st.session_state:
        downloaded_file_name = st.session_state.model_name+'_'+'model_card.md'
        st.sidebar.download_button(label = 'Download Model Card', data = '''this is a test''',file_name = downloaded_file_name, help = "The current model card will be downloaded as a markdown (.md) file")