import streamlit as st
from gemini import model

st.set_page_config(
    page_title="Internship Finder",
    page_icon="💼",
    layout="wide"
)

st.title("💼 AI Internship Finder")

st.write("Find the best internships based on your skills.")

skills = st.text_input(
    "Enter Your Skills",
    placeholder="Python, SQL, AI, Machine Learning, Streamlit..."
)

location = st.text_input(
    "Preferred Location (Optional)",
    placeholder="Hyderabad, Bangalore, Remote..."
)

if st.button("🔍 Find Internships", use_container_width=True):

    if skills.strip():

        with st.spinner("Finding the best internships..."):

            prompt = f"""
You are an AI Career Mentor.

A student has these skills:

Skills:
{skills}

Preferred Location:
{location if location else "Any"}

Suggest:

1. Suitable Internship Roles
2. Top Hiring Companies
3. Internship Platforms
4. Required Skills
5. Expected Stipend
6. Interview Preparation Tips
7. Recommended Projects
8. Final Recommendation

Format the answer clearly with headings and bullet points.
"""

            try:
                response = model.generate_content(prompt)

                st.success("✅ Internship Suggestions Ready!")

                st.markdown(response.text)

            except Exception as e:
                st.error(f"❌ {e}")

    else:
        st.warning("Please enter your skills.")

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