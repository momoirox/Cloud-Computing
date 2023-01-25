from django import forms


class RegistrationStudentForm(forms.Form):
    name = forms.CharField(label="Student's name", max_length=60)
    surname = forms.CharField(label="Student's surname", max_length=100)
    jmbg = forms.CharField(label="JMBG", max_length=20)
    indexNumber = forms.CharField(label="Index number", max_length=50)


class RegistrationProfessorForm(forms.Form):
    name = forms.CharField(label="Professor's name", max_length=60)
    surname = forms.CharField(label="Professor's surname", max_length=100)
    jmbg = forms.CharField(label="JMBG", max_length=20)
