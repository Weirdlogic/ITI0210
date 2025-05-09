from PyPDF2 import PdfReader

reader = PdfReader(r"C:\Users\adetunji\Documents\ITI0210\harry-potter-and-the-half-blood-prince-j.k.-rowling.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text()

with open("harry-potter-and-the-half-blood-prince-j.k.-rowling.txt", "w", encoding="utf-8") as f:
    f.write(text)
