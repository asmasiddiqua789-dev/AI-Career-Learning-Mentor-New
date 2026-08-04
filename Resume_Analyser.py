import streamlit as st
from PyPDF2 import PdfReader
from gemini import model

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and receive an AI-powered ATS analysis.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    try:
        reader = PdfReader(uploaded_file)

        resume_text = ""

        for page in reader.pages:
            text = page.extract_text()
            if text:
                resume_text += text + "\n"

        if resume_text.strip() == "":
            st.error("❌ No readable text found in the PDF.")
            st.stop()

        st.success("✅ Resume uploaded successfully!")

        with st.expander("📄 View Resume"):
            st.write(resume_text)

        if st.button("🚀 Analyze Resume", use_container_width=True):

            with st.spinner("Analyzing Resume..."):

                prompt = f"""
You are an ATS Resume Expert.

Analyze the following resume.

Provide the result in this format:

# ATS Score
(out of 100)

# Strengths

# Missing Skills

# Weaknesses

# Suggestions to Improve

# Final Recommendation

Resume:

{resume_text}
"""

                try:
                    response = model.generate_content(prompt)

                    st.success("✅ Analysis Completed!")

                    st.markdown(response.text)

                except Exception as e:
                    st.error(f"❌ {e}")

    except Exception as e:
        st.error(f"Unable to read PDF.\n\n{e}")

st.divider()

if st.button("⬅ Back to Dashboard"):
    st.switch_page("pages/Dashboard.py")

st.divider()

st.subheader("👩‍💻 About Developer")

st.info("""
**Asma Siddiqua**

🎓 B.Tech CSE (AI & ML)

🏫 Bharat Institute of Engineering & Technology
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