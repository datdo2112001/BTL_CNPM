from django.shortcuts import render
from .models import Exam
from django.views.generic import ListView,DetailView
from django.http import JsonResponse
import random

# Create your views here.

class ExamListView(ListView):
    model = Exam
    template_name = 'exams/main.html'

class Exam_detail_view(DetailView):
    model = Exam
    template_name = 'exams/exam.html'

def exam_data_view(request,pk):
    exam = Exam.objects.get(pk=pk)
    questions = []
    for q in exam.get_questions():
        questions.append(q)
    random.shuffle(questions)
    return render(request, 'exams/exam_data.html', {'data':questions})

def exam_edit_view(request,pk):
    all_exam = Exam.objects.all()
    exam = Exam.objects.get(pk=pk)
    questions = []
    all_questions = []
    for ex in all_exam:
        for quest in ex.get_questions():
            all_questions.append(quest)
    for q in exam.get_questions():
        questions.append(q)
    return render(request, 'exams/exam_edit.html', {'questions':questions , 'all_questions' : all_questions})