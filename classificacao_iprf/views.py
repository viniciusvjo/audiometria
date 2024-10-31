from .models import ClassificacaoIPRF
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class ClassificacaoIPRFListView(LoginRequiredMixin, ListView):
    model = ClassificacaoIPRF
    paginate_by = 10
    template_name = 'classificacao_iprf/index.html'
    context_object_name = 'object'
    ordering = ['id']
    login_url = "/authentication/login/"


class ClassificacaoIPRFDetailView(LoginRequiredMixin, DetailView):
    model = ClassificacaoIPRF
    template_name = 'classificacao_iprf/detail.html'
    login_url = "/authentication/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ClassificacaoIPRFCreateView(LoginRequiredMixin, CreateView):
    model = ClassificacaoIPRF
    fields = ['resultado', 'dificuldade']
    template_name = 'classificacao_iprf/create.html'
    success_url = reverse_lazy('classificacao_iprf:index')
    login_url = "/authentication/login/"


class ClassificacaoIPRFUpdateView(LoginRequiredMixin, UpdateView):
    model = ClassificacaoIPRF
    fields = ['resultado', 'dificuldade']
    template_name = 'classificacao_iprf/update.html'
    success_url = reverse_lazy('classificacao_iprf:index')
    login_url = "/authentication/login/"


class ClassificacaoIPRFDeleteView(LoginRequiredMixin, DeleteView):
    model = ClassificacaoIPRF
    template_name = 'classificacao_iprf/delete.html'
    success_url = reverse_lazy('classificacao_iprf:index')
    login_url = "/authentication/login/"