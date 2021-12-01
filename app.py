import streamlit as st

# from python_engine.src import get_answer_with_timestamp
from python_engine.src.core import get_answer_with_timestamp_unbatched


subs_filename = "subs.vtt"

st.title("Video QnA System")
st.subheader("A simple tool to make searching through videos easy")


col1, col2 = st.columns([3, 1])

with col1:
    url = st.text_input("URL of your YouTube video:")
    placeholder = st.empty()

with col2:
    st.markdown("#")
    if st.button("Load"):
        placeholder.video(url)

question = st.sidebar.text_input("Whats your question?")
if st.sidebar.button("Submit"):
    answer, timestamp = get_answer_with_timestamp_unbatched(url, question)
    placeholder.video(url, start_time=timestamp)
    st.sidebar.write(answer)
if st.sidebar.button("Reset"):
    placeholder = st.empty()
