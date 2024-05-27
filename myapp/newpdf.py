import pdfkit

# Path to the existing HTML file
html_file_path = "jobcarddetails.html"

# Path to save the PDF
pdf_path = "jobcard.pdf"

# Options for PDF generation (optional)
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}

# Generate PDF
pdfkit.from_file(html_file_path, pdf_path, options=options)

print("PDF created successfully at", pdf_path)
