import streamlit as st
from datetime import datetime
import csv
import os
import pandas as pd

# Initialize dark mode state
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

# CSS for light and dark modes
light_css = """
body, .block-container {
    background-color: white;
    color: black;
}
textarea, select, input, button {
    background-color: #f0f0f0 !important;
    color: black !important;
    border-radius: 8px !important;
    border: 1px solid #cccccc !important;
}
.stButton>button {
    background-color: #6200ee !important;
    color: white !important;
    border-radius: 8px !important;
}
.journal-container {
    background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(102, 166, 255, 0.6);
}
.journal-textarea textarea {
    background: white !important;
    color: #333333 !important;
    border-radius: 10px !important;
    padding: 10px !important;
    height: 150px !important;
    font-size: 16px !important;
    box-shadow: inset 0 2px 5px rgba(0,0,0,0.1);
}
"""

dark_css = """
body, .block-container {
    background-color: #121212;
    color: #e0e0e0;
}
textarea, select, input, button {
    background-color: #333333 !important;
    color: #e0e0e0 !important;
    border-radius: 8px !important;
    border: 1px solid #555555 !important;
}
.stButton>button {
    background-color: #bb86fc !important;
    color: black !important;
    border-radius: 8px !important;
}
.journal-container {
    background: linear-gradient(135deg, #4b6cb7 0%, #182848 100%);
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(27, 38, 56, 0.9);
}
.journal-textarea textarea {
    back
