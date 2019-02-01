from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('set', views.qa_set),
    path('qlist', views.question_list),
    path('log', views.log_conversation)
]