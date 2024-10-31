from .models import Timpanograma
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class TimpanogramaListView(LoginRequiredMixin, ListView):
    model = Timpanograma
    paginate_by = 10
    template_name = 'timpanograma/index.html'
    context_object_name = 'object'
    ordering = ['id']
    login_url = "/authentication/login/"


class TimpanogramaDetailView(LoginRequiredMixin, DetailView):
    model = Timpanograma
    template_name = 'timpanograma/detail.html'
    login_url = "/authentication/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TimpanogramaCreateView(LoginRequiredMixin, CreateView):
    model = Timpanograma
    fields = ['tipo', 'definicao', 'valor_referencia']
    template_name = 'timpanograma/create.html'
    success_url = reverse_lazy('timpanograma:index')
    login_url = "/authentication/login/"


class TimpanogramaUpdateView(LoginRequiredMixin, UpdateView):
    model = Timpanograma
    fields = ['tipo', 'definicao', 'valor_referencia']
    template_name = 'timpanograma/update.html'
    success_url = reverse_lazy('timpanograma:index')
    login_url = "/authentication/login/"


class TimpanogramaDeleteView(LoginRequiredMixin, DeleteView):
    model = Timpanograma
    template_name = 'timpanograma/delete.html'
    success_url = reverse_lazy('timpanograma:index')
    login_url = "/authentication/login/"
