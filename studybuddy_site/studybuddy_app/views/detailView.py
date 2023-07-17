from django.views.generic import DetailView
from .models import Subject
from django.shortcuts import render

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subject_detail.html'
    context_object_name = 'subject'

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
