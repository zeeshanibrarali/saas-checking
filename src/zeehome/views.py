from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVist
def home_view(request, *args, **kwargs):
    queryset  = PageVist.objects.all()
    my_context = {
        "queryset": queryset.count()
    }
    PageVist.objects.create()
    return render(request, 'home.html', my_context)

