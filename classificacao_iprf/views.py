from .models import ClassificacaoIPRF
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class ClassificacaoIPRFListView(ListView):
    model = ClassificacaoIPRF
    paginate_by = 10
    template_name = 'classificacao_iprf/index.html'
    context_object_name = 'object'
    ordering = ['id']


class ClassificacaoIPRFDetailView(DetailView):
    model = ClassificacaoIPRF
    template_name = 'classificacao_iprf/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ClassificacaoIPRFCreateView(CreateView):
    model = ClassificacaoIPRF
    fields = ['resultado', 'dificuldade']
    template_name = 'classificacao_iprf/create.html'
    success_url = reverse_lazy('classificacao_iprf:index')


class ClassificacaoIPRFUpdateView(UpdateView):
    model = ClassificacaoIPRF
    fields = ['resultado', 'dificuldade']
    template_name = 'classificacao_iprf/update.html'
    success_url = reverse_lazy('classificacao_iprf:index')


class ClassificacaoIPRFDeleteView(DeleteView):
    model = ClassificacaoIPRF
    template_name = 'classificacao_iprf/delete.html'
    success_url = reverse_lazy('classificacao_iprf:index')
