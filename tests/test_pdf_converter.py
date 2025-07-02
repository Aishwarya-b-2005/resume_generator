import unittest
from utils import pdf_converter
import os

class TestPDFConverter(unittest.TestCase):
    def test_pdf_generation(self):
        output_file = "test_resume.pdf"
        resume_text = "JOHN DOE\nSoftware Engineer\n\nEDUCATION\nB.Tech in Computer Science\n\nSKILLS\nPython, JavaScript"
        
        result = pdf_converter.save_resume_as_pdf(resume_text, output_file=output_file)

        # Check that file was created
        self.assertTrue(os.path.exists(result))

        # Clean up after test
        os.remove(result)

if __name__ == '__main__':
    unittest.main()
