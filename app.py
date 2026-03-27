import streamlit as st
from request_handler import execute_request
from ui_components import render_sidebar, render_response_section
from history_manager import load_history, save_to_history
from utils import is_valid_url

st.set_page_config(page_title="Local API Tester", layout="wide")
st.caption("Name: Gaurav Sambhaji Deshmukh | Class: CSE | Enrollment: MH2025SDAF4030513 | Topic: Local API Tester | Subject: Python")
st.title("⚡ Local API Tester")

history = load_history()
render_sidebar(history)

c1, c2 = st.columns([1, 4])
with c1:
    method = st.selectbox("Method", ["GET", "POST", "PUT", "DELETE", "PATCH"])
with c2:
    url = st.text_input("URL", value="https://jsonplaceholder.typicode.com/todos/1")

headers_in = st.text_area("Headers (Key: Value per line)", height=100)
body_in = st.text_area("Body (Payload)", height=150)

if st.button("Send", type="primary"):
    if not is_valid_url(url):
        st.error("Invalid URL.")
    else:
        with st.spinner("Processing..."):
            res, err = execute_request(method, url, headers_in, body_in)
            if res is not None:
                save_to_history(method, url, res.status_code)
            else:
                save_to_history(method, url, "ERR")
            render_response_section(res, err)
