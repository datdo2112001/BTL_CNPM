from django.db import models

# Create your models here.

class Exam(models.Model):
    name = models.CharField(max_length=255)
    number_of_questions = models.TextField(max_length = 255)

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()


