import streamlit as st
from chatbot_backend import ask_bot

st.set_page_config(page_title="CampusConnect", layout="centered")
st.title("🎓 CampusConnect - Academic Assistant Chatbot")

with st.form("chat_form"):
    user_input = st.text_input("Ask a question:")
    submitted = st.form_submit_button("Ask")

if submitted and user_input:
    with st.spinner("Getting answer..."):
        response = ask_bot(user_input)
        st.markdown(f"**🤖 Bot:** {response}")
