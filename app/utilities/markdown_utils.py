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
    temp = env.get_template('templates/modelcard_template.md')
    if "task" not in st.session_state:
        tmp_task = None
    else:
        tmp_task = st.session_state["task"]
    return (temp.render(
                model_id = st.session_state["model_name"], 
                model_description = st.session_state["model_description"],
                developers = st.session_state["model_developers"],
                repo_link = st.session_state["repo_link"],
                learning_method = st.session_state["learning_method"],
                algo_type = st.session_state["algo_type"],
                modality = st.session_state["modality"],
                task = tmp_task,
                direct_use = st.session_state["direct_use"],
                downstream_use = st.session_state["downstream_use"],
                oos_use = st.session_state["oos_use"],
                risks = st.session_state["risks"],
                training_data = st.session_state["training_data"],
                model_preprocessing = st.session_state["model_preprocessing"],
                training_time = st.session_state["training_time"],
                testing_data = st.session_state["testing_data"],
                metrics = st.session_state["metrics"],
                model_results = st.session_state["model_results"],
                citation_bibtex = st.session_state["citation_bibtex"],
                citation_apa = st.session_state["citation_apa"],
                model_specs = st.session_state["model_specs"],
                compute_infrastructure = st.session_state["compute_infrastructure"],
                model_hardware = st.session_state["model_hardware"],
                libraries = st.session_state["libraries"],
                how_to = st.session_state["how_to"],
                glossary = st.session_state["glossary"],
                more_info = st.session_state["more_info"]
            ))