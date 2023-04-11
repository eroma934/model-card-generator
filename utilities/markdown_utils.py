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
    # to add: 
    # - parent model
    # to fix:
        # citation on form: check box for bibtex or apa: then parse 
    return (temp.render(model_id = st.session_state["model_name"], developers = st.session_state["model_developers"]
            ))