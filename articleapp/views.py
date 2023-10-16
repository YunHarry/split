from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class TempView(TemplateView):
    template_name = 'articleapp/temp.html'