from operator import indexOf
import streamlit as st
import utils as utl
from pages import problem, cleaning, processing, analysis, polate, advanced, prediction, conclude, references, code

st.set_page_config(layout="wide", page_title='Navbar sample')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():
    route = utl.get_current_route()
    if route == "problem":
        problem.load_view()
    elif route == "cleaning":
        cleaning.load_view()
    elif route == "processing":
        processing.load_view()
    elif route == "analysis":
        analysis.load_view()
    elif route == "polate":
        polate.load_view()
    elif route == "advanced":
        advanced.load_view()
    elif route == "prediction":
        prediction.load_view()
    elif route == "conclude":
        conclude.load_view()
    elif route == "references":
        references.load_view()
    elif route == "code":
        code.load_view()
    elif route == None:
        indexOf.load_view()
        
navigation()