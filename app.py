import streamlit as st
from python_engine.src import get_transcript_yt, vtt_to_corpus, search_transcript
from transformers import pipeline

model_name = "deepset/roberta-base-squad2"
question_answerer = pipeline(
    model=model_name, tokenizer=model_name, revision="v1.0", task="question-answering"
)

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
        with open(subs_filename, "w+") as subs:
            transcript = get_transcript_yt(url)["subtitles"]
            subs.write(transcript)
corpus = vtt_to_corpus(subs_filename)

question = st.sidebar.text_input("Whats your question?")
if st.sidebar.button("Submit"):
    answer = question_answerer(question=question, context=corpus)["answer"]
    timestamp = search_transcript(answer, subs_filename)[0]
    placeholder.video(url, start_time=timestamp)
    st.sidebar.write(answer)
text_answer = st.sidebar.text_area("Your answers will appear below:")
if st.sidebar.button("Reset"):
    placeholder = st.empty()
