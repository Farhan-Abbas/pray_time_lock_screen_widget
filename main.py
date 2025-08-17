import requests
import PyPDF2
import io
import pdfplumber
from datetime import datetime

def extract_prayer_times_from_pdf():
    # Download the PDF
    pdf_url = "https://www.az-zahraa.org/salaat-timings/?action=print"
    response = requests.get(pdf_url)
    
    # Parse PDF content
    with pdfplumber.open(io.BytesIO(response.content)) as pdf:
        text = pdf.pages[0].extract_text()
        print(text)
        return parse_prayer_times(text)

extract_prayer_times_from_pdf()