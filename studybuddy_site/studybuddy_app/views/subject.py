from django.views.generic import ListView
from .models import Subject

class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'subject_list.html'
    context_object_name = 'subject_list'
