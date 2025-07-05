from django.urls import path
from . import views

app_name = "forum"

urlpatterns = [
    path('', views.indeIndexView.as_view()x, name='index'),
    path('<topic>/', views.ForumView.as_view(), name='forum'),
]