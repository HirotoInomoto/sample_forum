from django.urls import path
from . import views

app_name = "forum"

urlpatterns = [
    path('', views.index, name='index'),
    path('<topic>/', views.forum, name='forum'),
]