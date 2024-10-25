from django.shortcuts import render
from .models import GrauPerda
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class GrauPerdaListView(ListView):
    model = GrauPerda
    paginate_by = 10
    template_name = 'grau_perda/index.html'
    context_object_name = 'graus_list'
    ordering = ['id']


class GrauPerdaDetailView(DetailView):
    model = GrauPerda
    template_name = 'grau_perda/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GrauPerdaCreateView(CreateView):
    model = GrauPerda
    fields = ['grau_perda', 'media_frequencias', 'desempenho']
    template_name = 'grau_perda/create.html'
    success_url = reverse_lazy('grau_perda:index')


class GrauPerdaUpdateView(UpdateView):
    model = GrauPerda
    fields = ['grau_perda', 'media_frequencias', 'desempenho']
    template_name = 'grau_perda/update.html'
    success_url = reverse_lazy('grau_perda:index')


class GrauPerdaDeleteView(DeleteView):
    model = GrauPerda
    template_name = 'grau_perda/delete.html'
    success_url = reverse_lazy('grau_perda:index')
