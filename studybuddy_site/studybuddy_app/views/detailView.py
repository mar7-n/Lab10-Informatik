from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView
from .models.py import Subject
from .models import Subject
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import get_object_or_404


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subject_detail.html'
    context_object_name = 'subject'

    def get_object(self, pk):
        return get_object_or_404(YourModel, pk=pk)

    def get(self, request, pk, *args, **kwargs):
        object = self.get_object(pk)

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        object.description = request.POST['description']
        object.save()
        return HttpResponseRedirect(
            reverse("studybuddy_app:resource.detail",
                    args=[object.id]))

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

