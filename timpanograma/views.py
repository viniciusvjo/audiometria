from .models import Timpanograma
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class TimpanogramaListView(ListView):
    model = Timpanograma
    paginate_by = 10
    template_name = 'timpanograma/index.html'
    context_object_name = 'object'
    ordering = ['id']


class TimpanogramaDetailView(DetailView):
    model = Timpanograma
    template_name = 'timpanograma/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TimpanogramaCreateView(CreateView):
    model = Timpanograma
    fields = ['tipo', 'definicao', 'valor_referencia']
    template_name = 'timpanograma/create.html'
    success_url = reverse_lazy('timpanograma:index')


class TimpanogramaUpdateView(UpdateView):
    model = Timpanograma
    fields = ['tipo', 'definicao', 'valor_referencia']
    template_name = 'timpanograma/update.html'
    success_url = reverse_lazy('timpanograma:index')


class TimpanogramaDeleteView(DeleteView):
    model = Timpanograma
    template_name = 'timpanograma/delete.html'
    success_url = reverse_lazy('timpanograma:index')
