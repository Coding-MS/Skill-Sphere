from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import DetailView , DeleteView , ListView
from django.shortcuts import get_object_or_404
from .models import workboard

class WorkboardView(View):
    template_name = 'workboard/workboard.html'

    def get(self, request, *args, **kwargs):
        workboard_data = workboard.objects.all()
        context = {
            'workboard_data': workboard_data,
        }
        return render(request, self.template_name, context)


class Workboard_list(ListView):
    template_name = "workboard/workboard_list"
    model = workboard
    context_object_name = 'workboard'

class WorkboardDetailView(DetailView):
    model = workboard
    template_name = 'workboard/workboard_detail.html'
    context_object_name = 'workboard'

class WorkboardDeleteView(DeleteView):
    model = workboard
    template_name = 'workboard/workboard.html' 
    context_object_name = 'task'
    success_url = 'workboard/workboard_list.html'