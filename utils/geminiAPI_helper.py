import os
import google.generativeai as genai

genai.configure(api_key="") #fill with your api key
model = genai.GenerativeModel("models/gemini-1.5-flash")

def generate_resume(name, email, phone, linkedin, degree, experience, skills):
    prompt = f"""
    You are an expert resume writer. Use the following details to create a highly polished, ATS-friendly resume.

    Format clearly with sections:
    - Name and Contact Info
    - Professional Summary (2-3 lines, crisp and impactful)
    - Education
    - Experience (with bullet points for accomplishments and results, using action verbs)
    - Skills (split into two sections: Hard Skills and Soft Skills)

    Instructions:
    - Maintain a neutral, confident, and professional tone.
    - Do NOT use any special symbols, Markdown formatting, asterisks (*), or stars. 
    - Do NOT use Markdown-style syntax. Output plain text only.
    - Output section headers in ALL CAPS and bold-like plain text (without special Markdown).
    - Ensure work experience mentions accomplishments and results (e.g., "Led a team of 5 engineers...").
    - List Hard Skills and Soft Skills in separate sections under SKILLS.
    - Avoid filler words.
    - Output plain text only.

    Here are the candidate details:

    Name: {name}
    Email: {email}
    Phone: {phone}
    LinkedIn: {linkedin}
    Degree: {degree}
    Experience:
    {experience}
    Skills:
    {skills}
    """
    response = model.generate_content(prompt)  
    return response.text

def generate_cover_letter(resume, job_description):
    prompt = f"""
You are a career coach. Based on the resume and the job description below, write a customized, formal, and compelling cover letter that shows alignment between the candidate’s experience and the job requirements.

Resume:
{resume}

Job Description:
{job_description}

The cover letter should:
- Start with a formal greeting
- Mention the role being applied for
- Highlight key skills and experience relevant to the job
- Show enthusiasm and fit for the company
- Be 3-4 short paragraphs in length
- End with a professional closing

Only return the cover letter text, no extra commentary.
    """
    response = model.generate_content(prompt)
    return response.text
