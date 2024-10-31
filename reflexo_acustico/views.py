from .models import ReflexoAcustico
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ReflexoAcusticoListView(LoginRequiredMixin, ListView):
    model = ReflexoAcustico
    paginate_by = 10
    template_name = 'reflexo_acustico/index.html'
    context_object_name = 'object'
    ordering = ['id']
    login_url = "/authentication/login/"


class ReflexoAcusticoDetailView(LoginRequiredMixin, DetailView):
    model = ReflexoAcustico
    template_name = 'reflexo_acustico/detail.html'
    login_url = "/authentication/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReflexoAcusticoCreateView(LoginRequiredMixin, CreateView):
    model = ReflexoAcustico
    fields = ['tipo', 'descricao', 'caracteristicas']
    template_name = 'reflexo_acustico/create.html'
    success_url = reverse_lazy('reflexo_acustico:index')
    login_url = "/authentication/login/"


class ReflexoAcusticoUpdateView(LoginRequiredMixin, UpdateView):
    model = ReflexoAcustico
    fields = ['tipo', 'descricao', 'caracteristicas']
    template_name = 'reflexo_acustico/update.html'
    success_url = reverse_lazy('reflexo_acustico:index')
    login_url = "/authentication/login/"


class ReflexoAcusticoDeleteView(LoginRequiredMixin, DeleteView):
    model = ReflexoAcustico
    template_name = 'reflexo_acustico/delete.html'
    success_url = reverse_lazy('reflexo_acustico:index')
    login_url = "/authentication/login/"
