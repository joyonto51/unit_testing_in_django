from django.test import TestCase

from school.models import SchoolClass, Student

# test models
class StudentTest(TestCase):
    @staticmethod
    def get_or_create_school_class():
        school_classes = SchoolClass.objects.all()

        if school_classes:
            return school_classes.first()
        else:
            return SchoolClass.objects.create(class_name="One", numeric_value=1)

    def create_student(self, name='test_student', roll=1, address='Dhaka 1212'):
        school_class = self.get_or_create_school_class()
        return Student.objects.create(school_class=school_class, name=name, roll=roll, address=address)

    # test model
    def test_student_creation(self):
        student = self.create_student()
        self.assertTrue(isinstance(student, Student))
        self.assertEqual(student.__unicode__(), student.name)


# test models with dummy data
from model_bakery import baker

class TestStudentModel(TestCase):
    def test_create_student(self):
        student = baker.make(Student)
        self.assertTrue(isinstance(student, Student))
        self.assertEqual(student.__unicode__(), student.name)