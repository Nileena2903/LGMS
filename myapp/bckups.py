def generate_pdf(data):
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors

    # Create a PDF document
    pdf_file = "jobcard.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    story = []

    # Define styles
    styles = getSampleStyleSheet()
    style_heading = styles["Heading1"]
    style_body = styles["BodyText"]

    # Add heading
    heading = Paragraph("<b>JOBCARD DETAILS</b>", style_heading)
    story.append(heading)

    # Add table for job card details
    table_data = [
        ["Head of the House", data[0]['JOBCARD']['JOBCARDREQUEST']['Head']],
        ["Rationcar Number", data[0]['JOBCARD']['JOBCARDREQUEST']['Rationcard']]
    ]
    table = Table(table_data, colWidths=[200, 200])
    story.append(table)

    # Add table for members
    member_data = [["sl.no", "Name", "Gender", "Age", "Adhar Number", "Relation"]]
    for index, member in enumerate(data):
        member_data.append([
            index + 1,
            member['Name'],
            member['Gender'],
            member['Age'],
            member['Adharno'],
            member['Relation']
        ])
    member_table = Table(member_data, colWidths=[40, 100, 100, 40, 100, 100])
    member_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                      ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                      ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                      ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                      ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                      ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                      ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    story.append(member_table)

    # Build the PDF
    doc.build(story)

#
# # Usage
# data2 = []
# data3 = Jobcardmembers.objects.filter(JOBCARD__JOBCARDREQUEST_id=10)
# for i in data3:
#     data2.append({
#         "Name": i.Name,
#         "Gender": i.Gender,
#         "Age": i.Age,
#         "Adharno": i.Adharno,
#         "Relation": i.Relation,
#         'Photo': i.Photo,
#         'JOBCARD': i.JOBCARD,
#     })
#
# generate_pdf(data2)
