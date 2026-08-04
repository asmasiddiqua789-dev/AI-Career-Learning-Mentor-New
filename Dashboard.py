import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏠",
    layout="wide"
)
#---------------navigation----------------
st.markdown("""
<div style="
display:flex;
justify-content:space-between;
align-items:center;
padding:10px;
border-bottom:1px solid #ddd;
">

<div style="font-size:26px;font-weight:bold;">
🤖 AI Career Mentor
</div>

<div>
<a href="#" style="margin-right:25px;text-decoration:none;">Home</a>
<a href="#" style="margin-right:25px;text-decoration:none;">Features</a>
<a href="#" style="margin-right:25px;text-decoration:none;">About</a>
<a href="#" style="text-decoration:none;">Contact</a>
</div>

</div>
""", unsafe_allow_html=True)

search = st.text_input(
    "🔍 Search",
    placeholder="Search AI tools, careers, learning..."
)
st.divider()


# ---------------- Modern CSS ----------------

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.stApp{
background:linear-gradient(
135deg,
#F8FAFC,
#EEF4FF,
#F5F7FF
);
}

.block-container{
padding-top:2rem;
padding-left:3rem;
padding-right:3rem;
}

.hero{
background:linear-gradient(
135deg,
#3B82F6,
#60A5FA
);
padding:35px;

border-radius:22px;

box-shadow:0px 10px 35px rgba(0,0,0,.30);

margin-bottom:30px;

color:white;

}

.hero h1{

font-size:42px;

font-weight:700;

margin-bottom:10px;

}

.hero p{

font-size:18px;

opacity:.95;

}

.metric-card{

background:white;

padding:20px;

border-radius:18px;

text-align:center;

box-shadow:0 8px 20px rgba(0,0,0,.15);

transition:0.3s;

}

.metric-card:hover{

transform:translateY(-8px);

}

.feature-card{

background:white;

color:#1F2937;

border:1px solid #E5E7EB;

box-shadow:0 4px 12px rgba(0,0,0,0.08);

}

.feature-card:hover{

border:1px solid #3B82F6;

}

</style>
""", unsafe_allow_html=True)

# ---------------- Hero Banner ----------------

st.markdown("""

<div class="hero">

<h1>🤖 AI Career & Learning Mentor</h1>

<p>

Welcome back <b>Asma Siddiqua</b> 👋

<br><br>

Build your Resume • Learn AI • Find Internships • Chat with AI

</p>

</div>

""", unsafe_allow_html=True)
    
st.markdown("## ⚡ Quick Access")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("📄\n\nResume Analyzer")

with col2:
    st.info("🤖\n\nAI Chatbot")

with col3:
    st.info("🎯\n\nCareer Guidance")

with col4:
    st.info("📚\n\nLearning Roadmap")
    
    #-------------welcome card----------------
    st.markdown("""
<div style="
background:white;
padding:25px;
border-radius:20px;
box-shadow:0 5px 15px rgba(0,0,0,0.08);
margin-bottom:20px;
">

<h2 style="color:#2563EB;">👋 Welcome, Asma Siddiqua</h2>

<p style="font-size:18px;color:#4B5563;">
Your personal AI assistant is ready to help you with
resume analysis, career guidance, internships, AI learning,
and interview preparation.
</p>

</div>
""", unsafe_allow_html=True)
    
    
    st.markdown("## ⭐ Why Use AI Career & Learning Mentor?")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
🤖 **AI Career Guidance**

Get personalized career advice.
""")

with col2:
    st.info("""
📄 **Resume Analysis**

Improve your ATS score using AI.
""")

with col3:
    st.warning("""
💼 **Internship Finder**

Discover internships based on your skills.
""")
    
    #-------------------- Today's Learning Goal--------------------
    st.markdown("## 🎯 Today's Learning Goal")

st.progress(70)

st.write("""
✅ Complete Python practice

✅ Improve Resume

✅ Learn one AI concept

⬜ Apply for internships

⬜ Solve interview questions
""")
    
    #-----AI News & Tips-----
st.markdown("## 📰 Latest AI Updates")

col1, col2 = st.columns(2)

with col1:
    st.info("""
### 🤖 AI Tip of the Day

Keep your GitHub updated with projects.

Recruiters prefer candidates who show practical work.
""")

with col2:
    st.success("""
### 💡 Career Tip

Practice Data Structures & Algorithms regularly.

Build 3-5 AI projects before placements.
""")
    
    #----upcoming goals----
    st.markdown("## 📅 Upcoming Goals")

goals = [
    "📄 Improve Resume Score to 90%",
    "🤖 Build AI Chatbot",
    "💼 Apply for 20 Internships",
    "📚 Complete Machine Learning",
    "🎯 Prepare for Placements"
]

for goal in goals:
    st.checkbox(goal)
# -------------------- Header --------------------

st.title("🤖 AI Career & Learning Mentor")

st.caption("Your Personal AI Career Assistant")

st.success("Welcome back! Continue your AI learning journey.")

st.divider()

# -------------------- Metrics --------------------

st.markdown("## 📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

cards = [
    ("🔥", "Learning Streak", "14 Days"),
    ("📄", "Resume Score", "86%"),
    ("💼", "Internship Matches", "12"),
    ("🎯", "Career Readiness", "78%")
]

for col, (icon, title, value) in zip([col1, col2, col3, col4], cards):
    with col:
        st.markdown(f"""
        <div style="
            background:white;
            padding:25px;
            border-radius:18px;
            text-align:center;
            box-shadow:0 4px 15px rgba(0,0,0,0.08);
            border:1px solid #E5E7EB;
        ">
            <div style="font-size:35px;">{icon}</div>
            <div style="font-size:16px;color:#6B7280;">{title}</div>
            <div style="font-size:28px;font-weight:bold;color:#2563EB;">{value}</div>
        </div>
        """, unsafe_allow_html=True)
st.divider()


st.markdown("## 📈 AI Insights")

left, right = st.columns([2,1])

with left:
    st.success("""
### 🚀 AI Recommendation

✅ Improve your Resume Score

✅ Complete SQL Learning

✅ Build one AI Project

✅ Apply for 5 Internships
""")

with right:
    st.info("""
### 📅 Today's Goal

🎯 Learn Python

📄 Update Resume

🤖 Practice Interview

💼 Apply Internship
""")

# -------------------- AI Tools --------------------

st.markdown("## 🚀 AI Features")

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):

        st.subheader("📄 Resume Analyzer")

        st.write("Analyze your resume using AI and get ATS score.")

        if st.button("Open Resume Analyzer", use_container_width=True):
            st.switch_page("pages/Resume_Analyser.py")

    with st.container(border=True):

        st.subheader("🎯 Career Guidance")

        st.write("Receive AI-powered career guidance and recommendations.")

        if st.button("Open Career Guidance", use_container_width=True):
            st.switch_page("pages/Career_Guidance.py")

    with st.container(border=True):

        st.subheader("📚 Learning Roadmap")

        st.write("Generate personalized learning paths.")

        if st.button("Open Learning Roadmap", use_container_width=True):
            st.switch_page("pages/Learning_Roadmap.py")

with col2:

    with st.container(border=True):

        st.subheader("🤖 AI Chatbot")

        st.write("Chat with your personal AI Career Mentor.")

        if st.button("Open AI Chatbot", use_container_width=True):
            st.switch_page("pages/AI_Chatbot.py")

    with st.container(border=True):

        st.subheader("💼 Internship Finder")

        st.write("Find internships based on your skills.")

        if st.button("Open Internship Finder", use_container_width=True):
            st.switch_page("pages/Internship_Finder.py")

    with st.container(border=True):

        st.subheader("🚪 Logout")

        st.write("Sign out of your account.")

        if st.button("Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.switch_page("app.py")

st.divider()

# -------------------- Progress --------------------

left,right=st.columns([2,1])

with left:

    st.subheader("📈 Career Progress")

    st.progress(78)

    st.success("Career Readiness : 78%")

    st.info("Keep learning Python, Machine Learning, Deep Learning and Generative AI to reach 100%.")

with right:

    st.subheader("🏆 Achievements")

    st.write("✅ Python Basics")

    st.write("✅ Machine Learning")

    st.write("✅ AI Chatbot")

    st.write("🏅 Streamlit Project")

st.divider()

# -------------------- Checklist --------------------

st.subheader("📚 Learning Checklist")

st.checkbox("Python Programming",True)

st.checkbox("Machine Learning",True)

st.checkbox("Deep Learning")

st.checkbox("Generative AI")

st.checkbox("Data Structures")

st.checkbox("SQL")

st.checkbox("Build 5 Projects")

st.checkbox("Interview Preparation")

st.divider()

# -------------------- Developer --------------------

st.subheader("👩‍💻 Developer")

st.info("""
### Asma Siddiqua

🎓 B.Tech CSE (AI & ML)

🏫 Bharat Institute of Engineering & Technology

💡 Python | AI | Machine Learning | Streamlit
""")

g,l=st.columns(2)

with g:
    st.link_button(
        "💻 GitHub",
        "https://github.com/asmasiddiqua789-dev",
        use_container_width=True
    )

with l:
    st.link_button(
        "💼 LinkedIn",
        "https://www.linkedin.com/in/asma-siddiqua-7451b83a5/",
        use_container_width=True
    )

st.divider()

#----------profile card----------------
st.markdown("## 👩‍💻 Profile")

st.container(border=True)

col1, col2 = st.columns([1,3])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=120
    )

with col2:
    st.markdown("""
### Asma Siddiqua

🎓 B.Tech CSE (AI & ML)

🏫 Bharat Institute of Engineering & Technology

📍 Hyderabad, India

🚀 Passionate about Artificial Intelligence & Machine Learning
""")
#-------------------- Footer --------------------
st.markdown("""
<div style='text-align:center;color:gray;'>

### 🤖 AI Career & Learning Mentor

Made with ❤️ using Streamlit & OpenRouter

Developed by <b>Asma Siddiqua</b>

</div>
""", unsafe_allow_html=True)