#!/usr/bin/env python
import fitz  # PyMuPDF

def extract_raw_bytes(pdf_path):
    doc = fitz.open(pdf_path)
    for page in doc:
        text_instances = page.search_for("some part of visible text you know")
        for inst in text_instances:
            raw_text = page.get_text("rawdict", clip=inst)
            print(raw_text)  # Inspect the raw output

extract_raw_bytes("path_to_your_pdf.pdf")


