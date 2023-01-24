import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

from .models import Professor, Student
from .forms import RegistrationStudentForm, RegistrationProfessorForm

# Create your views here.

def index(request):
 
    if request.method == 'GET':
        registration_form = RegistrationStudentForm()
        return render(request, 'pmf/index.html', {
            "form" : registration_form
        })
    else:
        registration_form = RegistrationStudentForm(request.POST)
        
        if registration_form.is_valid():
            student = registration_form.cleaned_data

            st = Student(
                name = student['name'],
                surname = student['surname'],
                jmbg = student['jmbg'],
                indexNumber = student['indexNumber']
            )

            body = {
                "name" : "%s" % student['name'], 
                "lastName" : "%s" % student['surname'],
                "jmbg" : "%s" % student['jmbg'],
                }
            
            try:
                response = requests.post('http://localhost:8080/students', headers={'Content-Type': 'application/json'},json=body)
                if( response.status_code == 200):
                    st.save()
                    response = "Sudent registered ."
                elif(response.status_code == 409):
                    response = "Student allready exists."
                else : 
                    response = "Internal server error. Sorry, try again :( ."

              
                return render(request, 'pmf/index.html', {
                    "form" : registration_form,
                    "response": response
                })
            except:
                
                return HttpResponse(response)
