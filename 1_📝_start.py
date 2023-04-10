from yaml import load
from persist import persist, load_widget_state
import streamlit as st
from pathlib import Path
import requests
import pandas as pd
from middleMan import parse_into_jinja_markdown as pj
from streamlit_extras.switch_page_button import switch_page


def main():
    st.header("About")
    st.markdown(Path('about.md').read_text(), unsafe_allow_html=True)
    st.header("Get Started")
    st.text_input("Enter Model Name", key="model_name")
    if st.session_state["model_name"] != "":
        switch_page("Model Details")

if __name__ == '__main__':
    load_widget_state()
    if 'runpage' not in st.session_state :
        st.session_state.runpage = main
    st.session_state.runpage()


# @st.cache_data
# def get_cached_data():
#     languages_df = pd.read_html("https://hf.co/languages")[0]
#     languages_map = pd.Series(languages_df["Language"].values, index=languages_df["ISO code"]).to_dict()

#     available_metrics = [x['id'] for x in requests.get('https://huggingface.co/api/metrics').json()]

#     r = requests.get('https://huggingface.co/api/models-tags-by-type')
#     tags_data = r.json()
#     libraries = [x['id'] for x in tags_data['library']]
#     tasks = [x['id'] for x in tags_data['pipeline_tag']]
#     return languages_map, available_metrics, libraries, tasks

# def main_page():

   
#     if "model_name" not in st.session_state:
#         # Initialize session state.
#         st.session_state.update({
#             "input_model_name": "",
#             "languages": [],
#             "library_name": "",
#             "datasets": "",
#             "metrics": [],
#             "task": "",
#             "tags": "",
#             "model_description": "Some cool model...",
#             "the_authors":"",
#             "Shared_by":"",
#             "Model_details_text": "",
#             "Model_developers": "",
#             "blog_url":"",
#             "Parent_Model_url":"",
#             "Parent_Model_name":"",

#             "Model_how_to": "",
            
#             "Model_uses": "",
#             "Direct_Use": "",
#             "Downstream_Use":"",
#             "Out-of-Scope_Use":"",

#             "Model_Limits_n_Risks": "",
#             "Recommendations":"",

#             "training_Data": "",
#             "model_preprocessing":"",
#             "Speeds_Sizes_Times":"",



#             "Model_Eval": "",
#             "Testing_Data":"",
#             "Factors":"",
#             "Metrics":"",
#             "Model_Results":"",

#             "Model_c02_emitted": "",
#             "Model_hardware":"",
#             "hours_used":"",
#             "Model_cloud_provider":"",
#             "Model_cloud_region":"",

#             "Model_cite": "",
#             "paper_url": "",
#             "github_url": "",
#             "bibtex_citation": "",
#             "APA_citation":"",

#             "Model_examin":"",
#             "Model_card_contact":"",
#             "Model_card_authors":"",
#             "Glossary":"",
#             "More_info":"",

#             "Model_specs":"",
#             "compute_infrastructure":"",
#             "technical_specs_software":"",

#             "check_box": bool,
#             "markdown_upload":" ",
#             "legal_view":bool,
#             "researcher_view":bool,
#             "beginner_technical_view":bool,
#             "markdown_state":"",
#         })
#     ## getting cache for each warnings 
#     languages_map, available_metrics, libraries, tasks = get_cached_data()

#     ## form UI setting 
#     st.header("Model Card Form")

#     warning_placeholder = st.empty()

#     st.text_area("Model Description", help="The model description provides basic details about the model. This includes the architecture, version, if it was introduced in a paper, if an original implementation is available, the author, and general information about the model. Any copyright should be attributed here. General information about training procedures, parameters, and important disclaimers can also be mentioned in this section.", key=persist('model_description'))
#     st.multiselect("Language(s)", list(languages_map), format_func=lambda x: languages_map[x], help="The language(s) associated with this model. If this is not a text-based model, you should specify whatever language that is used in the dataset. For instance, if the dataset's labels are in english, you should select English here.", key=persist("languages"))
#     st.selectbox("Library Name", [""] + libraries, help="The name of the library this model came from (Ex. pytorch, timm, spacy, keras, etc.). This is usually automatically detected in model repos, so it is not required.", key=persist('library_name'))
#     st.text_input("Parent Model (URL)", help="If this model has another model as its base, please provide the URL link to the parent model", key=persist("Parent_Model_name"))
#     st.text_input("Datasets (comma separated)", help="The dataset(s) used to train this model. Use dataset id from https://hf.co/datasets.", key=persist("datasets"))
#     st.multiselect("Metrics", available_metrics, help="Metrics used in the training/evaluation of this model. Use metric id from https://hf.co/metrics.", key=persist("metrics"))
#     st.selectbox("Task", [""] + tasks, help="What task does this model aim to solve?", key=persist('task'))
#     st.text_input("Tags (comma separated)", help="Additional tags to add which will be filterable on https://hf.co/models. (Ex. image-classification, vision, resnet)", key=persist("tags"))
#     st.text_input("Author(s) (comma separated)", help="The authors who developed this model. If you trained this model, the author is you.", key=persist("the_authors"))
#     st.text_input("Related Research Paper", help="Research paper related to this model.", key=persist("paper_url"))
#     st.text_input("Related GitHub Repository", help="Link to a GitHub repository used in the development of this model", key=persist("github_url"))
#     st.text_area("Bibtex Citation", help="Bibtex citations for related work", key=persist("bibtex_citations"))
#     st.text_input("Carbon Emitted:", help="You can estimate carbon emissions using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700)", key=persist("Model_c02_emitted"))
   
   
    
#     # warnings setting
#     languages=st.session_state.languages or None
#     task = st.session_state.task or None
#     markdown_upload = st.session_state.markdown_upload
#     #uploaded_model_card = st.session_state.uploaded_model 
#     # Handle any warnings...
#     do_warn = False
#     warning_msg = "Warning: The following fields are required but have not been filled in: "
#     if not languages:
#         warning_msg += "\n- Languages"
#         do_warn = True
#     if not task or not markdown_upload:
#         warning_msg += "\n- Please choose a task or upload a model card"
#         do_warn = True
#     if do_warn:
#         warning_placeholder.error(warning_msg)

#     with st.sidebar:

#         ######################################################
#         ### Uploading a model card from local drive
#         ######################################################
#         st.markdown("## Upload Model Card")
       
#         st.markdown("#### Model Card must be in markdown (.md) format.") 

#         # Read a single file 
#         uploaded_file = st.file_uploader("Choose a file", type = ['md'], help = 'Please choose a markdown (.md) file type to upload')
#         if uploaded_file is not None:
           
#             file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type} 
#             name_of_uploaded_file = save_uploadedfile(uploaded_file)
           
#             st.session_state.markdown_upload = name_of_uploaded_file ## uploaded model card

#         elif st.session_state.task =='fill-mask' or 'translation' or 'token-classification' or ' sentence-similarity' or 'summarization' or 'question-answering' or 'text2text-generation' or 'text-classification' or 'text-generation' or 'conversational':
#             #st.session_state.markdown_upload = open(
#              #   "language_model_template1.md", "r+"
#             #).read() 
#             st.session_state.markdown_upload = "language_model_template1.md" ## language model template
        
#         elif st.session_state.task:
            
#             st.session_state.markdown_upload =  "current_card.md" ## default non language model template
        
#         #########################################
#         ### Download model card
#         #########################################


#         st.markdown("## Download current Model Card")

#         if st.session_state.model_name is None or st.session_state.model_name== ' ':
#             downloaded_file_name = 'current_model_card.md'
#         else: 
#             downloaded_file_name = st.session_state.model_name+'_'+'model_card.md'
#         download_status = st.download_button(label = 'Download Model Card', data = pj(), file_name = downloaded_file_name, help = "The current model card will be downloaded as a markdown (.md) file")
#         if download_status == True:
#             st.success("Your current model card, successfully downloaded 🤗")
 

# def main():
    
#     st.header("About")
#     st.markdown(Path('about.md').read_text(), unsafe_allow_html=True)
#     st.header("Get Started")
#     st.text_input("Enter Model Name", key=persist("model_name"))
#     start_card = st.button('Create a Model Card 📝')
#     if start_card:
#         switch_page("Model Details")

# if __name__ == '__main__':
#     load_widget_state()
#     if 'runpage' not in st.session_state :
#         st.session_state.runpage = main
#     st.session_state.runpage()
