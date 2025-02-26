from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.template import loader


# Create your views here.



class Todolist(APIView):

    def get(self, request):
        print("HIIIIIIIIII")
        template = loader.get_template("templates/todo.html")
        return HttpResponse(template.render())
  