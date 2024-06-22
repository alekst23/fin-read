import PyPDF2
import os

input_directory = "data"
output_directory = "output"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(input_directory):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(input_directory, filename)
        pdf_obj = open(pdf_path, 'rb')
        reader = PyPDF2.PdfReader(pdf_obj, strict=True)
        total_pages = len(reader.pages)

        output_text = []
        for page_num in range(total_pages):
            page = reader.pages[page_num]
            output_text.append(page.extract_text())

        output_filename = os.path.join(output_directory, filename.replace('.pdf', '.txt'))
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write("\n".join(output_text))

        pdf_obj.close()
