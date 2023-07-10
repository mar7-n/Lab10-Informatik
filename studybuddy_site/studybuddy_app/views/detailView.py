from django.views.generic import DetailView
from .models import Subject

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subject_detail.html'
    context_object_name = 'subject'
