import datetime
from django import forms
from django.db import models
from .models import Meetup 
from .models import Resources 
from django.utils import timezone
from django.forms.renderers import TemplatesSetting
from django.contrib.admin.widgets import AdminDateWidget
from .widgets import HTML5DateTimeInput
from studybuddy_app.common.date import date_from_form

# https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/#validation-on-a-modelform


class CustomFormRenderer(TemplatesSetting):
    form_template_name = "studybuddy_app/form_snippet.html"


class HTML5DateField(forms.DateField):
    widget = HTML5DateTimeInput
    
    def to_python(self, value):
        value = date_from_form(value)
        return value
    

class MeetupForm(forms.ModelForm):
    start_time = HTML5DateField(widget=HTML5DateTimeInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control form-control-sm"})
    
    class Meta:
        model = Meetup
        exclude = ('participants',)
    

    class ResourceForm(forms.ModelForm):
        class Meta:
            model = Resources
        exclude = ('recources',)
