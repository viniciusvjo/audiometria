from .models import Paciente
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PacienteListView(ListView):
    model = Paciente
    paginate_by = 10
    template_name = 'paciente/index.html'
    context_object_name = 'object'
    ordering = ['id']


class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'paciente/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PacienteCreateView(CreateView):
    model = Paciente
    fields = ['nome', 'cpf', 'data_nascimento', 'endereco']
    template_name = 'paciente/create.html'
    success_url = reverse_lazy('paciente:index')


class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = ['nome', 'cpf', 'data_nascimento', 'endereco']
    template_name = 'paciente/update.html'
    success_url = reverse_lazy('paciente:index')


class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'paciente/delete.html'
    success_url = reverse_lazy('paciente:index')
