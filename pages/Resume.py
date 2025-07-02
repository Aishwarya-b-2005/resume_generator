import streamlit as st
from utils.openai_helper import generate_resume
from utils.pdf_converter import save_resume_as_pdf

st.set_page_config(page_title="AI Resume Generator", layout="wide")

# ---- STEP TRACKER ----
if "step" not in st.session_state:
    st.session_state.step = 1

def next_step():
    if st.session_state.step < 4:
        st.session_state.step += 1
        # Reset resume when entering the generation page
        if st.session_state.step == 4:
            st.session_state.pop("resume", None)

def prev_step():
    if st.session_state.step > 1:
        st.session_state.step -= 1
        # Optional: Reset resume when going backwards
        if st.session_state.step != 4:
            st.session_state.pop("resume", None)


# ---- STEP 1: PERSONAL INFO ----
if st.session_state.step == 1:
    st.title("Step 1: Personal Information")
    name = st.text_input("Full Name", value=st.session_state.get("name", ""))
    email = st.text_input("Email", value=st.session_state.get("email", ""))
    phone = st.text_input("Phone Number", value=st.session_state.get("phone", ""))
    linkedin = st.text_input("LinkedIn Profile URL", value=st.session_state.get("linkedin", ""))
    degree = st.text_area("Education Details alongside year and grades (e.g., B.Tech 2000-2004)", 
                           value=st.session_state.get("degree", ""), height=100)

    photo = st.file_uploader("Upload your photo (JPEG/PNG)", type=["jpg", "jpeg", "png"])
    if photo is not None:
        st.session_state["photo"] = photo.getvalue()

    if st.button("Next", key="next1"):
        required_fields = [name, email, phone, linkedin, degree]
        if any(field == "" for field in required_fields):
            st.error("Please fill in all required fields.")

        else:
            st.session_state.name = name
            st.session_state.email = email
            st.session_state.phone = phone
            st.session_state.linkedin = linkedin
            st.session_state.degree = degree
            next_step()


# ---- STEP 2: WORK EXPERIENCE ----
elif st.session_state.step == 2:
    st.title("Step 2: Work Experience")
    experience = st.text_area(
        "Describe your past jobs, internships, or major projects.",
        value=st.session_state.get("experience", ""), height=250
    )
    st.session_state.experience = experience

    col1, col2 = st.columns(2)
    col1.button("Previous", on_click=prev_step, key="prev2")
    if col2.button("Next", key="next2"):
        if not experience.strip():
            st.error("Please provide your work experience.")
        else:
            next_step()


# ---- STEP 3: SKILLS ----
elif st.session_state.step == 3:
    st.title("Step 3: Skills")
    skills = st.text_area(
        "List your skills (technical, soft skills, tools, etc.)",
        value=st.session_state.get("skills", ""), height=250
    )
    st.session_state.skills = skills

    col1, col2 = st.columns(2)
    col1.button("Previous", on_click=prev_step, key="prev3")
    if col2.button("Next", key="next3"):
        if not skills.strip():
            st.error("Please provide your skills.")
        else:
            next_step()


# ---- STEP 4: GENERATE RESUME ----
elif st.session_state.step == 4:
    st.title("Step 4: Generate Resume")
    st.write("Review your details and click below to generate your resume.")

    col1, col2 = st.columns(2)
    col1.button("Previous", on_click=prev_step, key="prev4")

    if col2.button("Generate Resume", key="generate"):
        with st.spinner("Generating your resume..."):
            resume = generate_resume(
                name=st.session_state.name,
                email=st.session_state.email,
                phone=st.session_state.phone,
                linkedin=st.session_state.linkedin,
                degree=st.session_state.degree,
                experience=st.session_state.experience,
                skills=st.session_state.skills,
            )
            st.session_state["resume"] = resume 

    # ---- DISPLAY RESULTS IF THEY EXIST ----
    if "resume" in st.session_state:
        if "photo" in st.session_state:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(st.session_state["photo"], use_container_width=True)
            with col2:
                st.markdown(f"```\n{st.session_state['resume']}\n```")
        else:
            st.markdown(f"```\n{st.session_state['resume']}\n```")

        if st.button("Download as PDF"):
            pdf_file = save_resume_as_pdf(st.session_state["resume"],photo_data=st.session_state.get("photo"))
            with open(pdf_file, "rb") as f:
                st.download_button(
                    label="Click here to download PDF",
                    data=f.read(),
                    file_name="resume.pdf",
                    mime="application/pdf"
                )

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

