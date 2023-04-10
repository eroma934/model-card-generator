import streamlit as st
from jinja2 import Environment, FileSystemLoader


def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

## Handles parsing jinja variable templates
def parse_into_jinja_markdown():
    env = Environment(loader=FileSystemLoader('.'), autoescape=True)
    temp = env.get_template(st.session_state.markdown_upload)
    # to add: 
    # - parent model
    # to fix:
        # citation on form: check box for bibtex or apa: then parse 
    return (temp.render(model_id = st.session_state["model_name"],
        language = st.session_state["languages"],
        the_model_description = st.session_state["model_description"],developers=st.session_state["Model_developers"],shared_by = st.session_state["Shared_by"],model_license = st.session_state['license'],
        parent_model_link = st.session_state['Parent_Model_url'],
            direct_use = st.session_state["Direct_Use"], downstream_use = st.session_state["Downstream_Use"],out_of_scope_use = st.session_state["Out-of-Scope_Use"],
            bias_risks_limitations = st.session_state["Model_Limits_n_Risks"], bias_recommendations = st.session_state['Recommendations'],
            model_examination = st.session_state['Model_examin'],
            speeds_sizes_times = st.session_state['Speeds_Sizes_Times'],
            hardware= st.session_state['Model_hardware'], hours_used = st.session_state['hours_used'], cloud_provider = st.session_state['Model_cloud_provider'], cloud_region = st.session_state['Model_cloud_region'], co2_emitted = st.session_state['Model_c02_emitted'],
            citation_bibtex= st.session_state["APA_citation"], citation_apa = st.session_state['bibtex_citation'],
            training_data = st.session_state['training_Data'], preprocessing =st.session_state['model_preprocessing'],
            model_specs = st.session_state['Model_specs'], compute_infrastructure = st.session_state['compute_infrastructure'],software = st.session_state['technical_specs_software'],
            glossary = st.session_state['Glossary'], 
            more_information = st.session_state['More_info'], 
            model_card_authors = st.session_state['the_authors'],
            model_card_contact = st.session_state['Model_card_contact'],
            get_started_code =st.session_state["Model_how_to"],
            repo_link = st.session_state["github_url"],
            paper_link = st.session_state["paper_url"],
            blog_link = st.session_state["blog_url"],
            testing_data = st.session_state["Testing_Data"],
            testing_factors = st.session_state["Factors"],
            results = st.session_state['Model_Results'],
            testing_metrics = st.session_state["Metrics"]
            ))