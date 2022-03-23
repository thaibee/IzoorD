from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, ListView

from .forms import OrgForm
from .models import Organization


def org_list(request):
    orgs = Organization.objects.all()
    context = {'orgs': orgs}
    return render(request, 'organizations/org_list.html', context)


class OrgList(ListView):
    model = Organization
    template_name = 'organizations/org_list.html'
    context_object_name = 'orgs'
    paginate_by = 25


class OrgDetail(UpdateView):
    model = Organization
    form_class = OrgForm
    # fields = ['org_name']
    template_name = 'organizations/org_details.html'
    context_object_name = 'org'
    success_url = '/org'


def test_func(request):
    # countries = Organization.objects.order_by().values_list('org_country', flat=True).exclude(org_country=' ').exclude(org_country__isnull=True).distinct()
    countries = Organization
    print(countries)
    context = {'countries': countries}
    return render(request, 'organizations/test_func.html', context)

