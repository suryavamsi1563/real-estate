from django.shortcuts import render
from django.http import HttpResponse
from .models import PropertyTable
from profiles.models import UserProfile
from .forms import ContactForm,ContactModalForm,botform,SellPropertyForm,PropertyDetailsForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponseRedirect
from django.forms import Textarea
from regression_code.machine import pred_price


# Create your views here.


@login_required
def home_view(request):
    template_name = 'property/home.html'
    context_data = {}

    return render(request,template_name,context_data)


# def list_view(request):
#     template_name = 'property/list.html'
#     context_data = {}
#     property_all = PropertyTable.objects.all()
#     context_data['property'] = property_all
#     return render(request,template_name,context_data)
#     # return HttpResponse("This is Home.")

@method_decorator(login_required, name='dispatch')
class PropertyList(ListView):
    model = PropertyTable
    template_name = 'property/list.html'

@method_decorator(login_required, name='dispatch')
class PropertyDetail(DetailView):
    model = PropertyTable
    template_name = 'property/detail.html'
    def get_context_data(self, **kwargs):
        context = super(PropertyDetail, self).get_context_data(**kwargs)
        user = User.objects.get(username__iexact = self.object.user_data.username)
        profile = UserProfile.objects.get(user = self.object.user_data)
        print(user,profile)
        context['profile'] = profile
        context['user1'] = user
        location = None
        type_ = None
        size = None
        print(self.object.__dir__())
        if  self.object.property_type == 'unit/flat':
            type_ = 2
        elif self.object.property_type == 'house':
            type_ = 1
        else:
            type_ = 3

        size = int(self.object.property_rooms)
        if self.object.property_location == 'South':
            location = 2
        elif self.object.property_location == 'North':
            location = 1
        elif self.object.property_location == 'East':
            location = 3
        else:
            location = 4

        input_list = [size,type_,location]
        context['guided_price'] = pred_price(input_list)
        return context

@method_decorator(login_required, name='dispatch')
class PropertyCreateView(CreateView):
    model = PropertyTable
    fields = ['property_name',
            'property_address',
            'property_rooms',
            'property_type',
            'property_location',
            'property_pincode',
            'image',
            'property_price']
    widgets = {
        'property_address': Textarea(attrs={'cols': 80, 'rows': 20}),
    }
    template_name="property/create.html"
    success_url = reverse_lazy('property:list')

    def form_valid(self, form):
        current_user = User.objects.filter(username__iexact = self.request.user)
        form.instance.user_data = user=current_user[0]
        print(form.cleaned_data)
        # form.instance.property_price = property_price

        return super(PropertyCreateView, self).form_valid(form)

    def form_invalid(self,form):
        print("Form Invalid")
        print(form)
        return HttpResponse("Form Invalid")

@method_decorator(login_required, name='dispatch')
class PropertyUpdateView(UpdateView):
    model = PropertyTable
    fields = '__all__'
    template_name="property/update.html"
    success_url = reverse_lazy('property:list')

@method_decorator(login_required, name='dispatch')
class PropertyDeleteView(DeleteView):
    model = PropertyTable
    template_name="property/delete.html"
    success_url = reverse_lazy('property:list')

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

@login_required
def about_view(request):
    template_name = 'property/about.html'
    context_data = {}
    
    return render(request,template_name,context_data)

@login_required
def sell_property_view(request):
    template_name = "property/sell.html"
    context_data = {"form":SellPropertyForm,'form_details':PropertyDetailsForm}

    return render(request,template_name,context_data)


def validate_username(request):
    username = request.GET.get('username', None)
    print(request.POST)
    print(request.GET)
    location = None
    type_ = None
    size = None
    if  request.GET['type'] == 'unit/flat':
        type_ = 2
    elif request.GET['type'] == 'house':
        type_ = 1
    else:
        type_ = 3

    size = int(request.GET['rooms'])
    if request.GET["location"] == 'South':
        location = 2
    elif request.GET["location"] == 'North':
        location = 1
    elif request.GET["location"] == 'East':
        location = 3
    else:
        location = 4

    input_list = [size,type_,location]
    Predicted_price = pred_price(input_list)
    data = {
        'Predicted_price':Predicted_price
    }
    return JsonResponse(data)