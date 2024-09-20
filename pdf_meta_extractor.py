import PyPDF2

def remove_metadata(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PfdReader(file)
        
        if reader.metaData is not None:
            print("Metadata has been found in the file.")
            writer = PyPDF2.PdfWriter() #creates a new PDF file without metadata
            for page_num in range(len(reader.pages)):#copies pages freom original PDF to the new PDF
                page = reader.pages[page_num]
                writer.add_page(page)
            new_pdf_file = f"{pdf_file.split('.')[0]}_no_metadata.pdf"
            with open(new_pdf_file, 'wb') as output_file:
                writer.write(output_file)
            print(f"PDF file without metadata saved as '{new_pdf_file}'.")
        else:
            print("No metadata found in the PDF file.")
# Specifies the path to the PDF file.
pdf_file_path = "test.pdf" 
# Calls the function to remove metadata.
remove_metadata(pdf_file_path)
            