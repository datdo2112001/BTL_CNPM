from django.urls import path
from .views import exam_view,ExamListView

urlpatterns = [
    path("", ExamListView.as_view() , name='list-view'),
]