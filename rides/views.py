from django.shortcuts import render,HttpResponse,redirect
from .forms import myForm
from .models import Student

# Create your views here.
def myView(request):
    if request.method == "POST":
        form = myForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
        else:
            form = myForm()

    return render(request,'index.html',{'form':myForm()})


def successView(request):
    return render(request, "feedback.html")

def listOfStudents(request):
    students = Student.objects.all()
    print("All students")
    print(students)
    return render(request,'studentList2.html',{'students':students})