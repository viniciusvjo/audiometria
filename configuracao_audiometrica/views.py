from .models import ConfiguracaoAudiometrica
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class ConfiguracaoAudiometricaListView(ListView):
    model = ConfiguracaoAudiometrica
    paginate_by = 10
    template_name = 'configuracao_audiometrica/index.html'
    context_object_name = 'object'
    ordering = ['id']


class ConfiguracaoAudiometricaDetailView(DetailView):
    model = ConfiguracaoAudiometrica
    template_name = 'configuracao_audiometrica/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ConfiguracaoAudiometricaCreateView(CreateView):
    model = ConfiguracaoAudiometrica
    fields = ['tipo', 'caracteristicas']
    template_name = 'configuracao_audiometrica/create.html'
    success_url = reverse_lazy('configuracao_audiometrica:index')


class ConfiguracaoAudiometricaUpdateView(UpdateView):
    model = ConfiguracaoAudiometrica
    fields = ['tipo', 'caracteristicas']
    template_name = 'configuracao_audiometrica/update.html'
    success_url = reverse_lazy('configuracao_audiometrica:index')


class ConfiguracaoAudiometricaDeleteView(DeleteView):
    model = ConfiguracaoAudiometrica
    template_name = 'configuracao_audiometrica/delete.html'
    success_url = reverse_lazy('configuracao_audiometrica:index')
