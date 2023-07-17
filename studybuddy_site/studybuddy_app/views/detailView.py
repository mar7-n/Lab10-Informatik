from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView
from .models.py import Subject

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subject_detail.html'
    context_object_name = 'subject'


def post(self, request, *args, **kwargs):
    meetup = self.get_object()
    meetup.field_to_edit = request.POST['field_to_edit']
    meetup.save()
    return HttpResponseRedirect(
        reverse("studybuddy_app:meetup_detail", args=[meetup.id]))
