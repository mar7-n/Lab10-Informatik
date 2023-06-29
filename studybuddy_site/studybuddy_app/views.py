from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse

from .models import Meetup



def index(request):
    meetup_list = Meetup.objects.order_by("start_time")[:10]
    context = {"meetup_list": meetup_list}
    return render(request, "studybuddy_app/index.html", context)


def detail(request, meetup_id):
    meetup = get_object_or_404(Meetup, pk=meetup_id)
    context = {"meetup": meetup}
    return render(request, "studybuddy_app/detail.html", context)


def rsvp(request, meetup_id):
    return HttpResponse("You rsvp on meetup %s." % meetup_id)

