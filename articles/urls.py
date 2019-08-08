from django.urls import path
from . import views

urlpatterns = [
    #create
    path('new/', views.new),
    path('create/', views.create),
    #read 전체 게시물 읽는 것만 만든다
    path('', views.index),
    path('<int:question_id>/answers/create/', views.answer_create),
]