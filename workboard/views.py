from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import DetailView , DeleteView , ListView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator


from .models import Workboard
from .forms import WorkboardForm

class WorkboardView(View):
    template_name = 'workboard/workboard.html'
    model = Workboard
    paginate_by=6
    ordering= '-start_date'

    def get_context_data(self, **kwargs):
        context = {}
        queryset = Workboard.objects.all().order_by(self.ordering)

        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            workboards = paginator.page(page)
        except Exception as e:
            workboards = paginator.page(1)

        context['workboards'] = workboards
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)


class Workboard_list(ListView):
    template_name = "workboard/workboard_list"
    model = Workboard
    paginate_by=6
    ordering= ['-start_date']
    context_object_name = 'workboard'

class WorkboardDetail(DetailView):
    model = Workboard
    template_name = 'workboard/workboard_detail.html'
    context_object_name = 'workboard'

def create_workboard(request):
    if request.method == 'POST':
        form = WorkboardForm(request.POST)
        if form.is_valid():
            workboard = form.save(commit=False)
            workboard.user = request.user
            workboard.save()
            messages.success(request, 'Task created successfully')

            return redirect('home')
        else:
            print(form.errors)
    else:
        form = WorkboardForm()

    context = {
        'form': form,
    }

    return render(request, 'workboard/workboard_create.html', context)

            


class WorkboardDelete(DeleteView):
    model = Workboard
    template_name = 'workboard_delete.html'
    context_object_name = 'event'
    success_url = Workboard_list  
    pk_url_kwarg = 'custom_pk'
    

def delete_workboard(request, event_id):
    workboard = get_object_or_404(Workboard, pk=event_id)
    if request.user == event.creator or request.user.is_superuser:
        workboard.delete()
        messages.success(request, f"Request {workboard.title} successfully deleted.")
    else:
        messages.error(request, "You don't have permission to delete this job request.")

    return redirect('home')

    