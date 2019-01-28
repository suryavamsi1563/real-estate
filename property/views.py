from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    template_name = 'property/home.html'
    context_data = {}
    
    return render(request,template_name,context_data)
    # return HttpResponse("This is Home.")