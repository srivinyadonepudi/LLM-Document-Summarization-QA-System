from PyPDF2 import PdfReader

def load_text(uploaded_file):
    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    else:
        return uploaded_file.read().decode("utf-8")
