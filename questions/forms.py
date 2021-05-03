from django import forms
from .models import Question, Category
from exams.models import *

choices = Category.objects.all().values_list('name', 'name')
all_exams = Exam.objects.all().values_list('name', 'name')

choice_list=[]
exam_list =[]
for item in choices:
    choice_list.append(item)

for item in all_exams:
    exam_list.append(item)


class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'exam',
            'category',
            'question',
            'rightAnswer',
            'a1',
            'a2',
            'a3',
            'correctFeedback',
            'incorrectFeedback',
            'user',

        ]

        widgets = {
            'exam': forms.Select(choices=exam_list, attrs={'class': 'form-control'}),
            'category': forms.Select(choices = choice_list, attrs={ 'class': 'form-control'}),
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your question'}),
            'rightAnswer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'The right answer'}),
            'a1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wrong answer No1'}),
            'a2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wrong answer No2'}),
            'a3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wrong answer No3'}),
            'correctFeedback': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "What to show if the user get the right answer"}),
            'incorrectFeedback': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "What to show if the user get the wrong answer"}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }
