from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import workboard

def workboard_list(request):
    tasks = workboard.objects.all()
    return render(request, 'workboard_list.html', {'tasks': tasks})

class WorkboardDetailView(DetailView):
    model = workboard
    template_name = 'workboard_detail.html'
    context_object_name = 'task'

class WorkboardDeleteView(DeleteView):
    model = workboard
    template_name = 'workboard_detail.html' 
    context_object_name = 'task'
    success_url = reverse_lazy('workboard_list')