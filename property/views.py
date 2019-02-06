from django.shortcuts import render
from django.http import HttpResponse
from .models import PropertyTable
from .forms import ContactForm,ContactModalForm,botform
from django.contrib.auth.decorators import login_required
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


@login_required
def contact_view(request):
    template_name = 'property/contact.html'
    context_data = {'form':ContactForm,'form2':ContactModalForm,'formb':botform}


    if request.method =='POST':
        # print(request.POST)
        # form = ContactModalForm(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is Valid")
            # form.save(commit=True)
            
        # else:
        #     print(form.errors)
        #     return render(request,template_name,context_data)
    # else:
    #     form = ContactForm()
    return render(request,template_name,context_data)
    # return HttpResponse("This is Home.")

def about_view(request):
    template_name = 'property/about.html'
    context_data = {}
    
    return render(request,template_name,context_data)
    # return HttpResponse("This is Home.")