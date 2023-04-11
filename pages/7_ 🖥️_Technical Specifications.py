import streamlit as st
import json

for k, v in st.session_state.items():
    st.session_state[k] = v

with open("./static/model-tags.json") as f:
    tags_json = json.load(f)
    library = tags_json["library"]
    libraries = [x["id"] for x in library]

def main():
    
    st.markdown('# Technical Specifications')
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
        st.markdown('#### Compute Infrastructure:')
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
        st.markdown('##### Libraries:')
        
    with right:
        st.text_area(" ", key="model_specs")
        st.text_area(" ",key="compute_infrastructure")
        st.text_area(" ", key="model_hardware")
        st.multiselect(" ",[""]+libraries, key="libraries", help="Select the main libraries for the model.")
         
if __name__ == '__main__':
    main()