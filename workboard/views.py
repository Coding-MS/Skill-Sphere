from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import DetailView , DeleteView , ListView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404


from .models import workboard

class WorkboardView(View):
    template_name = 'workboard/workboard.html'
    paginate_by=6
    ordering= ['-start_date']


class Workboard_list(ListView):
    template_name = "workboard/workboard_list"
    model = workboard
    paginate_by=6
    ordering= ['-start_date']
    context_object_name = 'workboard'

class WorkboardDetail(DetailView):
    model = workboard
    template_name = 'workboard/workboard_detail.html'
    context_object_name = 'workboard'

class WorkboardCreate(CreateView):
    model= workboard
    fields = '__all__'
    success_url = 'workboard_list/'
    template_name= 'workboard/workboard_create.html'
     

class WorkboardDelete(DeleteView):
    model = workboard
    template_name = 'workboard_delete.html'
    context_object_name = 'event'
    success_url = Workboard_list  
    pk_url_kwarg = 'custom_pk'
    

def delete_event(request, event_id):
    event = get_object_or_404(Workboard, pk=event_id)
    if request.user == event.creator or request.user.is_superuser:
        event.delete()
        messages.success(request, f"Request {event.title} successfully deleted.")
    else:
        messages.error(request, "You don't have permission to delete this job request.")

    return redirect('home')

    