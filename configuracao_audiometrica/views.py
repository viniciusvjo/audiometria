from .models import ConfiguracaoAudiometrica
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class ConfiguracaoAudiometricaListView(LoginRequiredMixin, ListView):
    model = ConfiguracaoAudiometrica
    paginate_by = 10
    template_name = 'configuracao_audiometrica/index.html'
    context_object_name = 'object'
    ordering = ['id']
    login_url = "/authentication/login/"


class ConfiguracaoAudiometricaDetailView(LoginRequiredMixin, DetailView):
    model = ConfiguracaoAudiometrica
    template_name = 'configuracao_audiometrica/detail.html'
    login_url = "/authentication/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ConfiguracaoAudiometricaCreateView(LoginRequiredMixin, CreateView):
    model = ConfiguracaoAudiometrica
    fields = ['tipo', 'caracteristicas']
    template_name = 'configuracao_audiometrica/create.html'
    success_url = reverse_lazy('configuracao_audiometrica:index')
    login_url = "/authentication/login/"


class ConfiguracaoAudiometricaUpdateView(LoginRequiredMixin, UpdateView):
    model = ConfiguracaoAudiometrica
    fields = ['tipo', 'caracteristicas']
    template_name = 'configuracao_audiometrica/update.html'
    success_url = reverse_lazy('configuracao_audiometrica:index')
    login_url = "/authentication/login/"


class ConfiguracaoAudiometricaDeleteView(LoginRequiredMixin, DeleteView):
    model = ConfiguracaoAudiometrica
    template_name = 'configuracao_audiometrica/delete.html'
    success_url = reverse_lazy('configuracao_audiometrica:index')
    login_url = "/authentication/login/"
