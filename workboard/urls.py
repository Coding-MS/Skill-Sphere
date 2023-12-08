"""
URL configuration for Skill_Sphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from workboard.views import Workboard_list, WorkboardDetail,WorkboardCreate, WorkboardDelete
from home.views import home
from .views import WorkboardView
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')), 
    path('workboard/workboard/', WorkboardView.as_view(), name='workboard'),
    path('workboard/workboard_list/', Workboard_list.as_view(), name='workboard_list'),
    path('workboard/<int:pk>/', WorkboardDetail.as_view(), name='workboard_detail'),
    path('workboard/workboard_create/', WorkboardCreate.as_view(), name='workboard_create'),
    path('workboard_delete/<int:pk>/', WorkboardDelete.as_view(), name='workboard_delete'),
]

