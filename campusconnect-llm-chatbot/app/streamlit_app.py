import streamlit as st
from chatbot_backend import ask_bot

PORT = int(os.environ.get("PORT", 8000))
st.set_page_config(page_title="CampusConnect AI Assistant", page_icon="🎓")

st.markdown("""
    <h1 style='text-align: center; color: #4F8BF9;'>🎓 CampusConnect Chatbot</h1>
    <p style='text-align: center;'>Ask about university degrees, courses, admissions, and more!</p>
""", unsafe_allow_html=True)

user_input = st.text_input("Ask me anything about your university 👇")

if user_input:
    with st.spinner("Thinking... 🤔"):
        response = ask_bot(user_input)
    st.markdown("### 📬 Bot Response")
    st.success(response)
