from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from .models import ExameAudiometria
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from paciente.models import Paciente
from .forms import ExameAudiometriaForm


class ExameAudiometriaListView(LoginRequiredMixin, ListView):
    model = ExameAudiometria
    paginate_by = 10
    template_name = 'exame_audiometria/index.html'
    context_object_name = 'object'
    ordering = ['id']
    login_url = "/authentication/login/"


class ExameAudiometriaDetailView(LoginRequiredMixin, DetailView):
    model = ExameAudiometria
    template_name = 'exame_audiometria/detail.html'
    login_url = "/authentication/login/"


class ExameAudiometriaCreateView(LoginRequiredMixin, CreateView):
    model = ExameAudiometria
    login_url = "/authentication/login/"
    context_object_name = 'object'
    fields = '__all__'
    template_name = 'exame_audiometria/create.html'
    success_url = reverse_lazy('exame_audiometria:index')

    def get_context_data(self, **kwargs):
        pacientes_list = Paciente.objects.all()
        context = super(ExameAudiometriaCreateView, self).get_context_data(**kwargs)
        context['pacientes_list'] = pacientes_list
        return context

@login_required(login_url="/authentication/login/")
def exame_audiometria_update(request, pk):
    exame_audiometria = get_object_or_404(ExameAudiometria, pk=pk)

    if request.method == 'POST':
        form = ExameAudiometriaForm(request.POST, instance=exame_audiometria)
        if form.is_valid():
            form.save()
            return redirect('exame_audiometria:index')
    return render(request, 'exame_audiometria/update.html', {'object': exame_audiometria})


class ExameAudiometriaDeleteView(LoginRequiredMixin, DeleteView):
    model = ExameAudiometria
    template_name = 'exame_audiometria/delete.html'
    success_url = reverse_lazy('exame_audiometria:index')
    login_url = "/authentication/login/"
