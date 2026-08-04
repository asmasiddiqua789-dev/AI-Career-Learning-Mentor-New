import streamlit as st
from gemini import model

st.set_page_config(
    page_title="Career Guidance",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Career Guidance")

st.write("Get personalized career guidance powered by AI.")

career_question = st.text_area(
    "Ask your career question",
    placeholder="Example: How can I become an AI Engineer?"
)

if st.button("🚀 Get Career Guidance", use_container_width=True):

    if career_question.strip():

        with st.spinner("Generating Career Guidance..."):

            prompt = f"""
You are an expert AI Career Mentor.

Answer the following career question.

Question:
{career_question}

Provide:

1. Career Overview
2. Required Skills
3. Learning Roadmap
4. Best Certifications
5. Internship Opportunities
6. Salary Range
7. Future Scope
8. Final Advice

Keep the answer clear, structured, and beginner-friendly.
"""

            try:
                response = model.generate_content(prompt)

                st.success("✅ Career Guidance Generated!")

                st.markdown(response.text)

            except Exception as e:
                st.error(f"❌ {e}")

    else:
        st.warning("Please enter your question.")

st.divider()

if st.button("⬅ Back to Dashboard"):
    st.switch_page("pages/Dashboard.py")

st.divider()

st.subheader("👩‍💻 About Developer")

st.info("""
**Asma Siddiqua**

🎓 B.Tech CSE (AI & ML)

🏫 Bharat Institute of Engineering & Technology

💡 Passionate about AI, Machine Learning and Python.
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