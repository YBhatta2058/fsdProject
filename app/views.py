from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,DetailView
from .models import Student
import csv
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = "studentlist.html"
    context_object_name = "students" 

class DetailListView(DetailView):
    model = Student
    template_name = "studentdetail.html"
    context_object_name = "student" 


def generateCSV(self):
    students = Student.objects.all()
    response = HttpResponse(content_type='text/csv')
    
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    csv_writer = csv.writer(response)

    csv_writer.writerow(['ID', 'Name', 'Age'])

    for student in students:
        csv_writer.writerow([student.id, student.name, student.age])

    return response

def generatePDF(request):
    students = Student.objects.all()
    data = [['Name', 'Age']]

    for student in students:
        data.append([student.name, student.age])

    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    

    # style = TableStyle([
    #     ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    #     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    #     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #     ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    #     ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    #     ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    # ])

    table = Table(data)
    # table.setStyle(style)

    elements = [table]

    pdf.build(elements)

    pdf_value = buffer.getvalue()
    buffer.close()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="example.pdf"'

    response.write(pdf_value)

    return response
