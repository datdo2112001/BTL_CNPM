"""BTL_CNPM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
import questions.views
import exams.views

urlpatterns = [
    path("", questions.views.Home_view.as_view(), name='home'),
    path("question/list", questions.views.All_question_view.as_view(), name='question-list'),
    path("question/<int:pk>/", questions.views.Question_detail_view.as_view(), name='question-detail'),
    path("question/create/", questions.views.Add_question_view.as_view(), name='question-create'),
    path("question/edit/<int:pk>/", questions.views.Update_question_view.as_view(), name='question-edit'),
    path("question/delete/<int:pk>/", questions.views.Delete_question_view.as_view(), name='question-delete'),
    path("category/create/", questions.views.Category_create_view.as_view(), name='category-create'),
    path("category/<str:cats>/", questions.views.Category_view, name='category'),
    path("exam/<int:pk>/", exams.views.Exam_detail_view.as_view(), name='exam-detail'),
    path("exam/", exams.views.ExamListView.as_view(),name = 'exam'),
    path("exam/<int:pk>/edit", exams.views.exam_edit_view, name='exam-edit'),
    path("exam/<int:pk>/data", exams.views.exam_data_view, name='exam-detail'),
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/", include('accounts.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
