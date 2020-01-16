from django.test import TestCase

from school.models import Student
from school.views import StudentAddView
from school.forms import SchoolClassForm, StudentForm

# test forms
class TestStudentForm(TestCase):
    def test_valid_from(self):
        school_class = StudentAddView.get_school_class(None)
        student = Student.objects.create(school_class=school_class, name='test student', roll=1, address="test address")

        data = {
            'name': student.name,
            'roll': student.roll,
            'address': student.address,
        }

        form = StudentForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'name':'test student',
            'roll': None,
            'address': None
        }

        form = StudentForm(data)
        self.assertFalse(form.is_valid())