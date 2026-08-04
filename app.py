import streamlit as st

st.set_page_config(
    page_title="AI Career Learning Mentor",
    page_icon="🎓",
    layout="wide"
)

# ---------------- Session ---------------- #
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- Login ---------------- #
if not st.session_state.logged_in:

    st.title("🎓 AI Career Learning Mentor")

    st.markdown("### Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", use_container_width=True):

        if username == "admin" and password == "admin123":

            st.session_state.logged_in = True
            st.success("Login Successful!")
            st.switch_page("pages/Dashboard.py")

        else:
            st.error("Invalid Username or Password")

    st.divider()

    st.info("""
Demo Login

Username: admin

Password: admin123
""")

else:
    st.switch_page("pages/Dashboard.py")