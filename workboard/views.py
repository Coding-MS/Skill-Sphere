from django.shortcuts import render, redirect
from django.views.generic import DetailView , DeleteView , ListView
from django.shortcuts import get_object_or_404
from .models import workboard

class workboard_list(ListView):
    template_name = "workboard/workboard_list"
    model = workboard
    context_object_name = 'jobs'

class workboardDetailView(DetailView):
    model = workboard
    template_name = 'workboard_detail.html'
    context_object_name = 'task'

class workboardDeleteView(DeleteView):
    model = workboard
    template_name = 'workboard_detail.html' 
    context_object_name = 'task'
    success_url = 'workboard_list.html'