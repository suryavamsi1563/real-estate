from django.shortcuts import render
from .form import UserProfileForm,UserForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import UserProfile




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

        if user_form.is_valid() and profile_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = UserProfile.objects.create(
                user = user,
                address = request.POST.get('address'),
                mobile_no = request.POST.get('mobile_no')
            )
            profile.user = user
            profile.save()

            return HttpResponseRedirect('/login')

    return render(request,template_name,context)


def login_view(request):
    template_name = 'profiles/login.html'
    context = {
        'user_form':UserForm,
    }

    if request.POST:
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/home')
            else:
                return HttpResponse("Account not active")
            

    return render(request,template_name,context)

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')


from django.views import View

class ProfileView(View):
    def get(self, request):
        # <view logic>
        print(request)
        template_name = "profiles/profile_view.html"
        
        context = {

        }

        return render(request,template_name,context)