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
from django.urls import path, include
from workboard.views import Workboard_list, WorkboardDetail, create_workboard, WorkboardDeleteForm  # noqa
from home.views import home
from .views import WorkboardView, WorkboardDetail, create_workboard, delete_workboard  # noqa
from workboard.views import WorkboardView, WorkboardDetail, create_workboard, delete_workboard, CreateView,  WorkboardUpdateView  # noqa


urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('workboard/', WorkboardView.as_view(), name='workboard'),
    path('workboard/workboard_list/', Workboard_list.as_view(), name='workboard_list'),  # noqa
    path("<int:pk>/", WorkboardDetail.as_view(), name="workboard_detail"),
    path('workboard/create/', create_workboard, name='workboard_create'),
    path("delete/<int:workboard_id>/", delete_workboard, name="workboard_delete"),  # noqa
    path('workboard/update/<int:pk>/', WorkboardUpdateView.as_view(), name='workboard_update'),  # noqa
]
