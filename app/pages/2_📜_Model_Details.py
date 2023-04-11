import streamlit as st

for k, v in st.session_state.items():
    st.session_state[k] = v

def main():
    learning_method_list = ["Supervised", "Unsupervised", "Rule-Based System", "Reinforcement Learning", "Hybrid"]
    algorithm_type = ["Neural Network", "Traditional Algorithm"]
    modality_list = ["Natural Language", "Computer Vision", "Audio", "Multimodal", "Tabular"]
    nlp_tasks = ["Text Classification", "Sentence Similarity", "Generative", "Token Classification", "Conversational", "Fill-Mask", "Question Answering",  "Summarization", "Table Question Answering", "Translation"]
    cv_tasks = ["Image Classification", "Object Detection", "Event Detection", "Navigation", "Generative", "Image Restoration", "Augmented/virtual reality"]
    audio_tasks = ["Audio Classification", "Voice Forensics", "Speech-to-Text", "Audio-to-Audio"]
    tabular_tasks = ["Tabular Classification", "Tabular Regression"]
        
    # #st.set_page_config(layout="wide") ## not yet supported on the hub
    st.markdown('## Model Details')
    st.markdown('### Model Description')
    st.text_area("Provide a 2-3 sentence summary of what this model is.", key="model_description", help="The model description provides basic details about the model. This includes the architecture, version, if it was introduced in a paper, if an original implementation is available, the author, and general information about the model. Any copyright should be attributed here. General information about training procedures, parameters, and important disclaimers can also be mentioned in this section.")

    left, right = st.columns([4,6])
    sub_col1, sub_col2, sub_col3 = st.columns(3)
    with st.container():
        with left: 
            st.write("\n")
            st.write("\n")
            st.markdown('### Developed By:')
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.markdown('### Model & Repo Links:')
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.markdown('### Model Type:')
            
        with right:
            st.text_input(" ",help="List the people who built the model.", key="model_developers")
            st.write("\n")
            st.text_input(" ",help="Provide links to the model weights and underlying codebase.", key="repo_link")
        
        with st.container():
            with sub_col1:
                st.selectbox("Learning Method", [""]+ learning_method_list, key="learning_method")
            with sub_col2:
                st.selectbox("Algorithm Type",[""]+algorithm_type, key="algo_type")
            with sub_col3:
                st.selectbox("Modality",[""]+modality_list, key="modality")
                if st.session_state["modality"] == "Natural Language":
                    st.selectbox("Task",[""]+nlp_tasks, key="task")
                elif st.session_state["modality"] == "Computer Vision":
                    st.selectbox("Task",[""]+cv_tasks, key="task")
                elif st.session_state["modality"] == "Audio":
                    st.selectbox("Task",[""]+audio_tasks, key="task")
                elif st.session_state["modality"] == "Tabular":
                    st.selectbox("Task",[""]+tabular_tasks, key="task")


if __name__ == '__main__':
    main()