def readpdf(file_path):
    from pdfminer.high_level import extract_text
    text = extract_text(file_path)
    return text
