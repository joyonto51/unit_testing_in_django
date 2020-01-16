from django import forms


class SchoolClassForm(forms.Form):
    class_name = forms.CharField(max_length=20)
    numeric_value = forms.IntegerField(max_value=100)

class StudentForm(forms.Form):
    name = forms.CharField(max_length=50)
    roll = forms.IntegerField()
    address = forms.CharField(max_length=50)