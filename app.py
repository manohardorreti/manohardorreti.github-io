import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | John Doe"
PAGE_ICON = ":wave:"
NAME = "John Doe"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "johndoe@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Excel & Power BI": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web App": "https://youtu.be/3gaPrT7vwNQ",
    "🏆 Desktop Application - Excel2CSV Converter": "https://youtu.be/LzCfNanQ_9c",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
# Note: In a real deployment, you might want to load a local CSS file here
st.markdown("""
<style>
    /* Simple CSS to center the profile image */
    [data-testid="stImage"] {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
</style>
""", unsafe_allow_html=True)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    # Use a placeholder image or replace 'assets/profile-pic.png' with your file
    # st.image("assets/profile-pic.png", width=230) 
    st.markdown("##") # Spacer
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data="PDF_DATA_HERE", # Replace with open("resume.pdf", "rb")
        file_name="resume.pdf",
        mime="application/pdf",
    )
    st.write("📫", EMAIL)

with col2:
    # You can put a profile picture here, or a Lottie animation
    st.write("") 

# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 7 Years experience extracting actionable insights from data
- ✔️ Strong hands-on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.markdown(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write(
    """
- ► Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rates by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing strategies for the upcoming quarter
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write("#")
st.write("🚧", "**Data Analyst | Liberty Mutual**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales efforts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled data reports and delivered to teams across departments who helped identify areas for improvement
"""
)


# --- PROJECTS & ACCOMPLISHMENTS ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
