from django.forms import Form, CharField, BooleanField, ModelChoiceField, ModelForm, TextInput, Textarea, Select, \
    CheckboxInput, ValidationError, EmailInput, PasswordInput, ChoiceField
from .models import Organization
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import re


class OrgForm(ModelForm):
    countries = Organization.objects.order_by().values_list('org_country', flat=True).exclude(org_country=' ').exclude(
        org_country__isnull=True).distinct()
    org_name = CharField(label='Name', widget=TextInput(attrs={"class": "form-control"}))
    org_country = ChoiceField(label='Country', widget=Select())

    class Meta:
        model = Organization

        fields = ['org_name', 'org_country', 'org_address', 'org_phone1', 'org_contact', 'org_mail', 'org_web',
                  'canoverdraft', 'responseperson']

        # widgets = {
        #     'org_name': TextInput(attrs={"class": "form-control"}),
        #     'org_country': Select(attrs={"class": "form-control select"}, choices=countries),
        #     'org_address': TextInput(attrs={"class": "form-control"}),
        #     'org_phone1': TextInput(attrs={"class": "form-control"}),
        #     'org_contact': TextInput(attrs={"class": "form-control"}),
        #     'org_mail': EmailInput(attrs={"class": "form-control"}),
        #     'org_web': TextInput(attrs={"class": "form-control"}),
        #     'canoverdraft': CheckboxInput(attrs={"class": "form-check-input"}),
        #     'responseperson': TextInput(attrs={"class": "form-control"}),
        # }
