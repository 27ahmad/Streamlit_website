import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title="My website", page_icon=":male-student:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/70ba62be-d613-4b73-9947-416041f43636/Q9HQwXi3qC.json")
image_1 = Image.open("images/lap.png")
image_2 = Image.open("images/mac.png")

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

with st.container():
    st.write("---")
    st.header("My Projects")
    image_column, text_column = st.columns((1,2))
    st.write("##")

    with image_column:
        st.image(image_1)

    with text_column:
        st.subheader("Integrate Python and Streamlit to build a website")
        st.write(
            """
            Here we use Python and its libraries to build a website in a short amout of time.
            Streamlit is a library which makes building and hosting a website much easier.
            You can build and host your projects there.
             """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(image_2)
    with text_column:
        st.subheader("Creating an Online Store")
        st.write (
            """
            There are many ways to create an online store:
            - Code everything from Scratch using your preffered stack (Pro level and more customization)
            - Build your own website using third party websites like wordpress, hostinger, wix etc(Minimal to no coding required)
            """
        )

with st.container():
    st.write("---")
    st.header("Get In touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/shahma27@gmail.com" method="POST">
     <input type="text" name="name" required placeholder ="Your name"> 
     <input type="email" name="email" required placeholder = "Your email"> 
     <textarea name="message" placeholder="Write message here"></textarea>
     <button type="submit">Send</button>
    </form>"""

    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

