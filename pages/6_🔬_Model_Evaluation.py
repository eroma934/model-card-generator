import streamlit as st
import json
    
for k, v in st.session_state.items():
    st.session_state[k] = v

with open("./static/metrics.json") as f:
    available_metrics = [x['id'] for x in json.load(f)]

def main():
    st.markdown('# Evaluation')
    st.markdown(" This section describes the evaluation protocols and provides the results.")
    st.markdown('## Testing Data & Metrics:')
    left, right = st.columns([2,4])
    
    #st.markdown('### Model Description')

    with left: 
        st.write("\n")
        st.write("\n")
        st.markdown('#### Testing Data:')
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown('#### Metrics:')
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown('#### Results:')
        
    with right:
        st.text_area(" ", help="Ideally this links to a Dataset Card.",key="testing_data")
        st.multiselect(" ",[""]+available_metrics, key="metrics", help="What metrics will be used for evaluation in light of tradeoffs between different errors?")
        st.text_area(" ", key="model_results")   

if __name__ == '__main__':
    main()