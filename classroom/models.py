from django.db import models
from administrator.models import Session, Course
from student.models import Student
from django.core.validators import MinValueValidator
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Assignment(models.Model):
    import datetime
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    expiry_date = models.DateField(
        validators=[MinValueValidator(datetime.date.today)])


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    answer = RichTextUploadingField()
    submission_date = models.DateTimeField(auto_now_add=True)