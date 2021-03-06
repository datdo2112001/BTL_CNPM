from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Question, Category
from .forms import QuestionModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
import random


# Create your views here.
class Home_view(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home_view, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class All_question_view(ListView):
    model = Question
    template_name = 'questions/questionList.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(All_question_view, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class Question_test(ListView):
    model = Question
    template_name = 'questions/question_test.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Question_test, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class Question_detail_view(DetailView):
    model = Question
    templist = []
    template_name = 'questions/question.html'


class Add_question_view(CreateView):
    model = Question
    form_class = QuestionModelForm
    template_name = "questions/add_quiz.html"

class Update_question_view(UpdateView):
    model = Question
    template_name = "questions/edit.html"
    fields = ['question', 'rightAnswer', 'a1', 'a2', 'a3', 'correctFeedback', 'incorrectFeedback']

class Delete_question_view(DeleteView):
    model = Question
    template_name = "questions/delete.html"
    success_url = reverse_lazy('home')

def Category_view(request, cats):
    category_questions = Question.objects.filter(category = cats)
    return render(request, 'category.html', {'cats':cats.title(), 'category_questions': category_questions})

def Test_view(request, cats):
    category_questions = Question.objects.filter(category = cats)
    suffleList = []
    stack = []
    length = len(category_questions)
    for question in category_questions:
        templist = [question.a1,question.a2,question.a3,question.rightAnswer]
        random.shuffle(templist)
        suffleList.append(templist)
    return render(request, 'questions/test.html', {'cats':cats.title(), 'test_list': category_questions, 'list':suffleList,'length':length, 'stack':stack})


class Category_create_view(CreateView):
    model = Category
    template_name = "questions/addCategory.html"
    fields = '__all__'

def Profile_view(request):
    myques = Question.objects.all()
    context = {'myques':myques}
    return render(request,"questions/profile.html",context)


@login_required()
def question_create_view(request, *args, **kwargs):
    form = QuestionModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = QuestionModelForm()
    return render(request, "forms.html", {"form": form})

