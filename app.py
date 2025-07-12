import streamlit as st
from utils import load_text
from summarizer import summarize_text
from qa_system import answer_question

st.title("LLM-Powered Doc Summarizer & QA")

uploaded_file = st.file_uploader("Upload a document", type=["txt", "pdf"])
if uploaded_file:
    text = load_text(uploaded_file)
    st.subheader("Document Preview")
    st.write(text[:1000] + "...")

    if st.button("Summarize"):
        summary = summarize_text(text)
        st.subheader("Summary")
        st.write(summary)

        question = st.text_input("Ask a question about the document")
        if question:
            answer = answer_question(text, question)
            st.subheader("Answer")
            st.write(answer)
