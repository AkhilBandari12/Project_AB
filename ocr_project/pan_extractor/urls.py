from django.urls import path
from .views import PanOCRView

urlpatterns = [
    path('extract_pan/', PanOCRView.as_view(), name='extract_pan'),
]
