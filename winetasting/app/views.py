from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RedTastingForm
from .models import RedTasting

# 詳細画面
class DetailView(LoginRequiredMixin, DetailView):
    model = RedTasting

# 登録画面
class CreateView(LoginRequiredMixin, CreateView):
    model = RedTasting
    form_class = RedTastingForm
    success_url = reverse_lazy('detail')

# 更新画面
class UpdateView(LoginRequiredMixin, UpdateView):
    model = RedTasting
    form_class = RedTastingForm
    success_url = reverse_lazy('detail')

# 削除画面
class DeleteView(LoginRequiredMixin, DeleteView):
    model = RedTasting
    success_url = reverse_lazy('detail')
