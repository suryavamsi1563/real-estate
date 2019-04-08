"""real_ML URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from property.views import (home_view,
                            about_view,
                            contact_view)
from transaction.views import tran_comp
from django.conf.urls.static import static
from django.conf import settings
from profiles.views import registration,login_view,logout_view

urlpatterns = [
    url(r"^home/$",home_view,name='home'),
    url(r"^about/$",about_view,name='about'),
    url(r"^contact/$",contact_view,name='contact'),
    url(r'^property/',include('property.urls',namespace='property')),
    url(r'^transaction/',include('transaction.urls')),
    url(r'^registration/',registration,name='regist'),
    url(r'^login/',login_view,name='login'),
    url(r'^logout/',logout_view,name='logout'),
    url(r'^profile/',include('profiles.urls',namespace='profiles')),
    url(r'^admin/', admin.site.urls),
    url(r"^$",login_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)