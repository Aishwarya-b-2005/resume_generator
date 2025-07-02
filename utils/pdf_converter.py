from fpdf import FPDF
from PIL import Image
import tempfile
import os

def save_resume_as_pdf(resume_text, photo_data=None, output_file="resume.pdf"):
    """Save the resume text and optional photo as a polished PDF."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Paths to your font files
    regular_font_path = "utils/DejaVuSans.ttf"
    bold_font_path = "utils/DejaVuSans-Bold.ttf"

    # Add fonts
    pdf.add_font("DejaVuSans", "", regular_font_path, uni=True)
    pdf.add_font("DejaVuSans", "B", bold_font_path, uni=True)

    # If a photo is uploaded, save it temporarily and embed
    if photo_data:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png" if photo_data and photo_data.startswith(b'\x89PNG') else ".jpeg") as temp_file:#suffix=".jpeg") as temp_file:
            temp_file.write(photo_data)
            temp_file.flush()
            # Place the image at the top-right
            pdf.image(temp_file.name, x=160, y=10, w=30, h=30)

    # Move down slightly if photo is present
    if photo_data:
        pdf.set_y(45)

    # Process the resume text
    lines = resume_text.split("\n")
    for line in lines:
        stripped = line.strip()
        if not stripped:
            pdf.ln(4)  # Small space for blank lines
            continue

        # If it's an ALL CAPS line, treat it as a Section Header
        if stripped.isupper():
            pdf.set_font("DejaVuSans", "B", 14)
            pdf.cell(0, 10, stripped, ln=True)
        else:
            pdf.set_font("DejaVuSans", "", 12)
            pdf.multi_cell(0, 8, stripped)

    pdf.output(output_file)

    # Cleanup temp image
    if photo_data:
        os.remove(temp_file.name)

    return output_file


def save_cover_letter_as_pdf(cover_letter_text, output_file="cover_letter.pdf"):
    """Save a cover letter text as a polished PDF."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Paths to your font files
    regular_font_path = "utils/DejaVuSans.ttf"
    bold_font_path = "utils/DejaVuSans-Bold.ttf"

    # Add fonts
    pdf.add_font("DejaVuSans", "", regular_font_path, uni=True)
    pdf.add_font("DejaVuSans", "B", bold_font_path, uni=True)

    lines = cover_letter_text.split("\n")
    for line in lines:
        stripped = line.strip()
        if not stripped:
            pdf.ln(4)  # Space for blank lines
            continue

        # All caps treated as a header
        if stripped.isupper():
            pdf.set_font("DejaVuSans", "B", 14)
            pdf.cell(0, 10, stripped, ln=True)
        else:
            pdf.set_font("DejaVuSans", "", 12)
            pdf.multi_cell(0, 8, stripped)

    pdf.output(output_file)
    return output_file