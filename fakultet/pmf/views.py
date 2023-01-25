import requests
from django.http import HttpResponse
from django.shortcuts import render

from .forms import RegistrationStudentForm, RegistrationProfessorForm
from .models import Professor, Student


# Create your views here.

def homepage(request):
    return render(request, 'pmf/homepage.html')


def professors(request):
    if request.method == 'GET':
        registration_form = RegistrationProfessorForm()
        return render(request, 'pmf/professors.html', {
            "form": registration_form
        })

    elif request.method == 'POST':
        registration_form = RegistrationProfessorForm(request.POST, request.FILES)

        if registration_form.is_valid():
            professor = registration_form.cleaned_data

            pr = Professor(
                name=professor['name'],
                surname=professor['surname'],
                jmbg=professor['jmbg'],
                image=professor["image"]
            )

            body = {
                "name": "%s" % professor['name'],
                "lastName": "%s" % professor['surname'],
                "jmbg": "%s" % professor['jmbg'],
            }
            response = requests.post('http://uns:8080/professors', headers={'Content-Type': 'application/json'},
                                     json=body)
            try:
                if response.status_code == 200:
                    pr.save()
                    response = "Professor registered. "
                elif response.status_code == 409:
                    response = "Professor already exists. "
                else:
                    response = "Internal server error. Sorry, try again :( ."

                return render(request, 'pmf/professors.html', {
                    "form": registration_form,
                    "response": response
                })
            finally:
                return HttpResponse(response)


def index(request):
    if request.method == 'GET':
        registration_form = RegistrationStudentForm()
        return render(request, 'pmf/index.html', {
            "form": registration_form
        })

    elif request.method == 'POST':
        registration_form = RegistrationStudentForm(request.POST, request.FILES)

        if registration_form.is_valid():
            student = registration_form.cleaned_data
            print(student.get('image'))
            st = Student(
                name=student['name'],
                surname=student['surname'],
                jmbg=student['jmbg'],
                indexNumber=student['indexNumber'],
                image=student["image"]
            )

            body = {
                "name": "%s" % student['name'],
                "lastName": "%s" % student['surname'],
                "jmbg": "%s" % student['jmbg'],
            }
            response = requests.post('http://uns:8080/students', headers={'Content-Type': 'application/json'},
                                     json=body)
            try:
                if response.status_code == 200:
                    st.save()
                    response = "Student registered. "
                elif response.status_code == 409:
                    response = "Student already exists. "
                else:
                    response = "Internal server error. Sorry, try again :( ."

                return render(request, 'pmf/index.html', {
                    "form": registration_form,
                    "response": response
                })
            finally:
                return HttpResponse(response)
