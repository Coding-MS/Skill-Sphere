from django.urls import reverse, reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.forms import ModelForm

from workboard.forms import WorkboardUpdateForm
from .models import Workboard
from .forms import WorkboardForm, WorkboardDeleteForm


class WorkboardView(View):
    template_name = 'workboard/workboard.html'
    model = Workboard
    paginate_by = 6
    ordering = '-start_date'

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
    paginate_by = 6
    ordering = ['-start_date']
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


def delete_workboard(request, workboard_id):
    workboard = get_object_or_404(Workboard, pk=workboard_id)

    if request.user == workboard.user:
        workboard.delete()
        messages.success(request, 'Task deleted successfully')
    else:
        messages.error(request, 'You do not have permission to delete this task')  # noqa

    return redirect('home')


class WorkboardUpdateView(UpdateView):
    template_name = "workboard/workboard_update.html"
    model = Workboard
    form_class = WorkboardUpdateForm

    def get_queryset(self):
        # Fetch only the workboards that belong to the current user
        return Workboard.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('home')
