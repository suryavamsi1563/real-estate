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
from django.conf.urls import url
from .views import (home_view,
                    PropertyList,
                    sell_property_view,
                    PropertyDetail,
                    PropertyCreateView,
                    PropertyUpdateView,
                    PropertyDeleteView)

urlpatterns = [
    url(r'^buy',PropertyList.as_view(),name='list'),
    url(r'^view/(?P<pk>\d+)',PropertyDetail.as_view(),name='detail'),
    url(r'^update/(?P<pk>\d+)',PropertyUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)',PropertyDeleteView.as_view(),name='delete'),
    url(r'^sell',sell_property_view,name='sell'),
    url(r'^create',PropertyCreateView.as_view(),name='create'),
]