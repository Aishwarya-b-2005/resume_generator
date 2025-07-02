
import streamlit as st

st.set_page_config(page_title="AI Resume and Cover Letter Generator", layout="wide")

st.title("AI Resume and Cover Letter Generator")

st.header("Get Started with AI Resume and Cover Letter Generator")
st.markdown("""
 Welcome to the AI Resume and Cover Letter Generator! This tool helps you create tailored resumes and cover letters for your job applications using advanced AI technology.

 ### Features:
1. **Resume Generation**: Input your personal details, work experience, and skills to generate a professional resume.
2. **Cover Letter Generation**: Paste your resume and the job description to create a customized cover letter.
3. **User-Friendly Interface**: Simple and intuitive design for easy navigation.
         
### How to Use:
1. Generate a resume by providing your personal details, work experience, and skills.
2. Generate a cover letter by pasting your resume and the job description.
3. Click the "Generate" button to create your documents.
4. Review the generated content and make any necessary edits.
""")

# Two columns for buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Generate Resume"):
        st.query_params["page"] = "resume"

with col2:
    if st.button("Generate Cover Letter"):
        st.query_params["page"] = "coverletter"

# Redirect based on query param
if "page" in st.query_params:
    if st.query_params["page"] == "resume":
        st.switch_page("pages/Resume.py")
    elif st.query_params["page"] == "coverletter":
        st.switch_page("pages/CoverLetter.py")

#Custom styling
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #2196F3;
    color: white;
    border-radius: 8px;
    font-size: 16px;
    height: 3em;
    width: 100%;
}
div.stButton > button:first-child:hover {
    background-color: #8976D2;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)
