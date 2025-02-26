from django.urls import path
# from . import views
from app1.views import Todolist



urlpatterns = [
    path('todolist/',Todolist.as_view(),name='todolist'),
]
