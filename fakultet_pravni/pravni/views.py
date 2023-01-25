import requests
from django.http import HttpResponse
from django.shortcuts import render

from .forms import RegistrationStudentForm, RegistrationProfessorForm
from .models import Professor, Student


# Create your views here.

def homepage(request):
    return render(request, 'pravni/homepage.html')


def professors(request):
    if request.method == 'GET':
        registration_form = RegistrationProfessorForm()
        return render(request, 'pravni/professors.html', {
            "form": registration_form
        })

    elif request.method == 'POST':
        registration_form = RegistrationProfessorForm(request.POST)

        if registration_form.is_valid():
            professor = registration_form.cleaned_data

            pr = Professor(
                name=professor['name'],
                surname=professor['surname'],
                jmbg=professor['jmbg'],
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

                return render(request, 'pravni/professors.html', {
                    "form": registration_form,
                    "response": response
                })
            finally:
                return HttpResponse(response)


def index(request):
    if request.method == 'GET':
        registration_form = RegistrationStudentForm()
        return render(request, 'pravni/index.html', {
            "form": registration_form
        })

    elif request.method == 'POST':
        registration_form = RegistrationStudentForm(request.POST)

        if registration_form.is_valid():
            student = registration_form.cleaned_data

            st = Student(
                name=student['name'],
                surname=student['surname'],
                jmbg=student['jmbg'],
                indexNumber=student['indexNumber']
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

                return render(request, 'pravni/index.html', {
                    "form": registration_form,
                    "response": response
                })
            finally:
                return HttpResponse(response)
