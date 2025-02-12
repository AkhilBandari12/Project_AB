from django.urls import path
from .views import split_pdf

urlpatterns = [
    path('split-pdf/', split_pdf, name='split_pdf'),
]
