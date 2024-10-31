from .models import Paciente
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    paginate_by = 10
    template_name = 'paciente/index.html'
    context_object_name = 'object'
    ordering = ['id']
    login_url = "/authentication/login/"


class PacienteDetailView(LoginRequiredMixin, DetailView):
    model = Paciente
    template_name = 'paciente/detail.html'
    login_url = "/authentication/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PacienteCreateView(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ['nome', 'cpf', 'data_nascimento', 'endereco']
    template_name = 'paciente/create.html'
    success_url = reverse_lazy('paciente:index')
    login_url = "/authentication/login/"


class PacienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Paciente
    fields = ['nome', 'cpf', 'data_nascimento', 'endereco']
    template_name = 'paciente/update.html'
    success_url = reverse_lazy('paciente:index')
    login_url = "/authentication/login/"


class PacienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Paciente
    template_name = 'paciente/delete.html'
    success_url = reverse_lazy('paciente:index')
    login_url = "/authentication/login/"
