from django.contrib.auth.mixins import LoginRequiredMixin
from .models import GrauPerda
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class GrauPerdaListView(LoginRequiredMixin, ListView):
    model = GrauPerda
    paginate_by = 10
    template_name = 'grau_perda/index.html'
    context_object_name = 'graus_list'
    ordering = ['id']
    login_url = "/authentication/login/"


class GrauPerdaDetailView(LoginRequiredMixin, DetailView):
    model = GrauPerda
    template_name = 'grau_perda/detail.html'
    login_url = "/authentication/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GrauPerdaCreateView(LoginRequiredMixin, CreateView):
    model = GrauPerda
    fields = ['grau_perda', 'media_frequencias', 'desempenho']
    template_name = 'grau_perda/create.html'
    success_url = reverse_lazy('grau_perda:index')
    login_url = "/authentication/login/"


class GrauPerdaUpdateView(LoginRequiredMixin, UpdateView):
    model = GrauPerda
    fields = ['grau_perda', 'media_frequencias', 'desempenho']
    template_name = 'grau_perda/update.html'
    success_url = reverse_lazy('grau_perda:index')
    login_url = "/authentication/login/"


class GrauPerdaDeleteView(LoginRequiredMixin, DeleteView):
    model = GrauPerda
    template_name = 'grau_perda/delete.html'
    success_url = reverse_lazy('grau_perda:index')
    login_url = "/authentication/login/"
