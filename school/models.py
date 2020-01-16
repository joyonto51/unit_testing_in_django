from django.db import models

# Create your models here.
class SchoolClass(models.Model):
    class_name = models.CharField(max_length=20)
    numeric_value = models.IntegerField()

    def __str__(self):
        return self.class_name

class Student(models.Model):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, related_name='students')

    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.name, self.school_class.class_name)

    def __unicode__(self):
        return self.name
