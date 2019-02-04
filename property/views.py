from django.shortcuts import render
from django.http import HttpResponse
from .models import PropertyTable
# Create your views here.

def home_view(request):
    template_name = 'property/home.html'
    context_data = {}
    
    return render(request,template_name,context_data)
    # return HttpResponse("This is Home.")


def list_view(request):
    template_name = 'property/list.html'
    context_data = {}
    property_all = PropertyTable.objects.all()
    context_data['property'] = property_all
    return render(request,template_name,context_data)
    # return HttpResponse("This is Home.")

def contact_view(request):
    template_name = 'property/contact.html'
    context_data = {}
    
    return render(request,template_name,context_data)
    # return HttpResponse("This is Home.")

def about_view(request):
    template_name = 'property/about.html'
    context_data = {}
    
    return render(request,template_name,context_data)
    # return HttpResponse("This is Home.")