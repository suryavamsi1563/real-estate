from django.shortcuts import render
from .form import UserProfileForm,UserForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.models import User
from property.models import PropertyTable

from django.db.utils import IntegrityError

# def user_profile_update(request):



# Create your views here.
def registration(request):
    template_name = 'profiles/registration.html'
    context = {
        'user_form':UserForm,
        'profile_form':UserProfileForm
    }
    
    if request.POST:
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)
        print(request.POST)
        # if user_form.is_valid() and profile_form.is_valid:
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

        if profile_form.is_valid():
            profile = UserProfile.objects.create(
                user = user,
                address = request.POST.get('address'),
                mobile_no = request.POST.get('mobile_no'),
                pan_no = request.POST.get('pan_no'),
                Occupation = request.POST.get('Occupation')
            )
            profile.user = user
            profile.save()

            return HttpResponseRedirect('/login')

    return render(request,template_name,context)


def login_view(request):
    error = None
    error_message = None
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')

    template_name = 'profiles/login.html'

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/home')
            else:
                return HttpResponse("Account not active")
        else:
            error = True
            error_message = "Username or Password is invalid."
    context = {
        'user_form':UserForm,
        'error':error,
        'error_message':error_message
    }
    return render(request,template_name,context)

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')


from django.views import View

@login_required
def ProfileView(request):
    template_name = "profiles/profile_view.html"
    obj = UserProfile.objects.get(user=request.user)
    address = obj.address
    mobile = obj.mobile_no
    Occupation = obj.Occupation
    properties = PropertyTable.objects.filter(user_data=request.user)

    
    context = {
        'mobile':mobile,
        'address':address,
        'occupation':Occupation,
        'properties':properties
    }
    return render(request,template_name,context)

@login_required
def profile_update_view(request):
    print("called the profile update view")
    template_name = "profiles/profile_update.html"

    obj = UserProfile.objects.get(user=request.user)
    address = obj.address
    mobile = obj.mobile_no
    Occupation = obj.Occupation
    pan = obj.pan_no
    print(address)
    context = {'address':address,
                'mobile':mobile,
                'pan':pan,
                'occupation':Occupation
            }
    current_user = User.objects.filter(username__iexact = request.user)
    print("Username object is: ",current_user)
    if request.method == 'POST':
        print(request.POST)
        email = request.POST.get('email')
        occupation = request.POST.get('occupation')
        if occupation=="Self-Employed":
            occupation='Self'
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        pan = request.POST.get('pan')
        
        print(email)
        print(occupation)
        print(address)
        print(mobile)
        print(pan)
        print(current_user)
        try:
            new_object = UserProfile.objects.update_or_create(user=current_user[0],
                                                    address=address,
                                                    mobile_no=mobile,
                                                    pan_no=pan,
                                                    Occupation=occupation)
        except IntegrityError:
            obj = UserProfile.objects.get(user=request.user)
            obj.address = address
            obj.mobile_no = mobile
            obj.pan_no = pan
            obj.Occupation = occupation
            obj.save()

        print(UserProfile.objects.all())
        user_object = User.objects.filter(id=request.user.id).update(email=email)
        return HttpResponseRedirect(reverse('profiles:home'))
    return render(request,template_name,context)