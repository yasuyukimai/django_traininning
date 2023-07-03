from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import RedTastingForm
from .models import RedTasting

class ListView(ListView):
    model = RedTasting
    template_name = 'app/list.html'
    context_object_name = 'list'

class DetailView(DetailView):
    queryset = RedTasting.objects.all()

# class CreateView(CreateView):
#     model = RedTasting
#     form_class = RedTastingForm
#     success_url = reverse_lazy('detail')

# class UpdateView(UpdateView):
#     model = RedTasting
#     form_class = RedTastingForm
#     success_url = reverse_lazy('detail')

# class DeleteView(DeleteView):
#     model = RedTasting
#     success_url = reverse_lazy('detail')
