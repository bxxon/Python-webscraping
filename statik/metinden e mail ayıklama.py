import re
from docx import Document

doc = Document("manas.docx")

text = ""
for para in doc.paragraphs:
    text += para.text + "\n"

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
for email in emails:
    print(email)
