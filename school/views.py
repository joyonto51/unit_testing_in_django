from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework.views import APIView

from school.forms import SchoolClassForm, StudentForm
from school.models import SchoolClass, Student


class URLListView(View):
    def get(self, request):
        return render(request, "url_list.html")


class SchoolClassAddView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'school_class_add.html')

    def post(self, request, *args, **kwargs):
        form = SchoolClassForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            SchoolClass.objects.get_or_create(**data)

        return HttpResponseRedirect(reverse('student_add'))


class StudentAddView(View):

    def get(self, request, *args, **kwargs):
        context = {
            'school_classes': SchoolClass.objects.all()
        }

        return render(request, 'student_add.html', context)

    def post(self, request, *args, **kwargs):
        school_class_id = request.POST.get('class_id', None)
        school_class = self.get_school_class(school_class_id)

        form = StudentForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            data['school_class'] = school_class

            Student.objects.create(**data)

        return HttpResponseRedirect(reverse('student_list'))

    @staticmethod
    def get_school_class(class_id):
        if class_id:
            return SchoolClass.objects.get(id=class_id)
        elif SchoolClass.objects.exists():
            return SchoolClass.objects.all().first()
        else:
            return SchoolClass.objects.get_or_create(class_name="One", numeric_value=1)[0]


class StudentListView(View):

    def get(self, request, *args, **kwargs):
        context = {
            'students': Student.objects.all().order_by('roll')
        }

        return render(request, 'student_list.html', context)


class StudentAddAPIView(APIView):
    def get(self, request):
        data = {
            'message':'API is Okay',
        }
        return Response(data)
