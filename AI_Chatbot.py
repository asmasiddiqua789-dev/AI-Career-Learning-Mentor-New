import streamlit as st
from gemini import model

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Career Chatbot")

st.write("Ask anything about AI, careers, programming, interviews, resumes, or learning.")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
prompt = st.chat_input("Ask your AI Mentor...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = model.generate_content(
                    f"""
You are an AI Career Mentor.

Answer the following question professionally and clearly.

Question:
{prompt}

Provide practical, beginner-friendly guidance.
"""
                )

                reply = response.text

                st.markdown(reply)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": reply
                    }
                )

            except Exception as e:

                st.error(f"❌ {e}")

st.divider()

if st.button("⬅ Back to Dashboard"):
    st.switch_page("pages/Dashboard.py")

st.divider()

st.subheader("👩‍💻 About Developer")

st.info("""
**Asma Siddiqua**

🎓 B.Tech CSE (AI & ML)

🏫 Bharat Institute of Engineering & Technology

💡 Passionate about Artificial Intelligence, Machine Learning and Python.
""")

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "💻 GitHub",
        "https://github.com/asmasiddiqua789-dev",
        use_container_width=True
    )

with col2:
    st.link_button(
        "💼 LinkedIn",
        "https://www.linkedin.com/in/asma-siddiqua-7451b83a5/",
        use_container_width=True
    )

st.divider()

st.caption("© 2026 AI Career & Learning Mentor")
st.caption("Developed by Asma Siddiqua")