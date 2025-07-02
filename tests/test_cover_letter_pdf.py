import unittest
from utils import pdf_converter
import os

class TestCoverLetterPDF(unittest.TestCase):
    def test_cover_letter_generation(self):
        output_file = "test_cover_letter.pdf"
        cover_letter_text = """
JOHN DOE
1234 Main Street
City, Country

TO WHOM IT MAY CONCERN

I am writing to apply for the position of Software Engineer. I have strong experience in Python and web development.

I would appreciate the opportunity to contribute to your team.

Sincerely,
John Doe
"""
        result = pdf_converter.save_cover_letter_as_pdf(cover_letter_text, output_file=output_file)

        # Check that the file was created
        self.assertTrue(os.path.exists(result))

        # Clean up after test
        os.remove(result)

if __name__ == '__main__':
    unittest.main()
