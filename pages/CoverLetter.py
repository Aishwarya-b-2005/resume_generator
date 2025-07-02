import streamlit as st
from utils.openai_helper import generate_cover_letter
from utils.pdf_converter import save_cover_letter_as_pdf

st.set_page_config(page_title="AI Cover Letter Generator", layout="wide")
st.title("✉️ Cover Letter Generator")

# Inputs
resume_text = st.text_area("Paste your Resume",height=250)
job_description = st.text_area("Paste the Job Description",height=200)

# Initialize cover_letter in session state
if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = ""

# Button to generate
if st.button("Generate Cover Letter"):
    required_fields = [resume_text,job_description]
    if any(field == "" for field in required_fields):
            st.error("Please fill in all required fields.")

    else:
        with st.spinner("Generating your cover letter..."):
            cover_letter = generate_cover_letter(resume_text, job_description)
            st.session_state.cover_letter = cover_letter
            st.success("Here is your cover letter. You can edit it before downloading:")

# Cover Letter Editing
if st.session_state.cover_letter:
    edited_cover_letter = st.text_area(
        "Edit Cover Letter:", 
        value=st.session_state.cover_letter, 
        height=300
    )
    st.session_state.cover_letter = edited_cover_letter  # Save any edits

    # Button for downloading the edited version
    if st.button("Download as PDF"):
        pdf_file = save_cover_letter_as_pdf(st.session_state.cover_letter)
        with open(pdf_file, "rb") as f:
            st.download_button(
                label="Click here to download Cover Letter as PDF",
                data=f.read(),
                file_name="cover_letter.pdf",
                mime="application/pdf"
            )

# Styling
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
