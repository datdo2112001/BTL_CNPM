from django.db import models
from django.conf import settings
from django.urls import reverse
from datetime import date, datetime
from exams.models import Exam
User = settings.AUTH_USER_MODEL
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
       return self.name

    def get_absolute_url(self):
        #return reverse('question-detail', args=(str(self.pk)))
        return reverse('home')


class Question(models.Model):
    #id = models.AutoField();
    exam = models.ForeignKey(Exam,null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length= 255, default='')
    question = models.CharField(max_length=255)
    rightAnswer = models.CharField(max_length=255)
    a1 = models.CharField(max_length=255)
    a2 = models.CharField(max_length=255)
    a3 = models.CharField(max_length=255)
    correctFeedback = models.TextField(max_length=255, null=True, blank=True, default="")
    incorrectFeedback = models.TextField(max_length=255, null=True, blank=True, default="")


    def __str__(self):
       return self.question + self.category

    def get_absolute_url(self):
        #return reverse('question-detail', args=(str(self.pk)))
        return reverse('home')
