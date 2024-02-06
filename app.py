import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Into", page_icon=":male-student:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/21e3f22a-58fd-44ed-8419-4c50ed406d7f/Wk89A1PCrE.json")

with st.container():
    st.subheader("Hi, I am Ahmad :wave: ")
    st.title("A Computer Science Student ")
    st.write("I am passionate about using Python and AI to help solve real-world problems")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """ I'm a final year BCA Grad student who is looking to break into the field of AI and solve problems.
        If this sounds interesting, let's connect and bring change! """
        )

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")