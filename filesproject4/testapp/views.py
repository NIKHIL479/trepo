from django.shortcuts import render
from testapp.models import Student
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    if request.method=='POST':
        image=request.FILES['image']
        video=request.FILES['video']
        student=Student(image=image,video=video)
        student.save()
        return HttpResponseRedirect('/')

    return render(request,'testapp/home.html')

def display(request):
    students=Student.objects.all()

    return render(request,'testapp/display.html',context={'students':students})
