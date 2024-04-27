#!/usr/bin/env python
import pytesseract
from PIL import Image
import pdfplumber

# Customize Tesseract's configuration
custom_oem_psm_config = r'--oem 3 --psm 6'

# Function to perform OCR on a single page using advanced settings
def ocr_page(image):
    return pytesseract.image_to_string(image, config=custom_oem_psm_config)

# Read the PDF and perform OCR with advanced settings
with pdfplumber.open("/Users/whitney/Desktop/multitasking.pdf") as pdf:
    full_text = ""
    for page in pdf.pages:
        im = page.to_image(resolution=300)  # Increase resolution for better OCR
        text = ocr_page(im)
        full_text += text


breakpoint()

with open("output_text.txt", "w", encoding='utf-8') as text_file:
    text_file.write(full_text)
