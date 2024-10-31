from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tipo
from .forms import TipoForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
class IndexView(LoginRequiredMixin, ListView):
    model = Tipo
    paginate_by = 10
    template_name = 'tipo_perda_auditiva/index.html'
    context_object_name = 'tipos_list'
    ordering = ['id']
    login_url = "/authentication/login/"


class TipoDetailView(LoginRequiredMixin, DetailView):
    model = Tipo
    template_name = 'tipo_perda_auditiva/detail.html'
    success_url = reverse_lazy('tipo_perda_auditiva:index')
    login_url = "/authentication/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@login_required(login_url="/authentication/login/")
def createView(request):
    if request.method == "POST":
        form = TipoForm(request.POST)
        if form.is_valid():
            tipo_perda = form.save()
            messages.success(
                request,
                'Seu cadastro foi criado ou atualizado com sucesso.'
            )

            return redirect("tipo_perda_auditiva:index")
    else:
        form = TipoForm()
    return render(request, "tipo_perda_auditiva/create.html", {'form': form})


class TipoUpdateView(LoginRequiredMixin, UpdateView):
    model = Tipo
    fields = ['tipo_perda', 'caracteristicas']
    template_name = 'tipo_perda_auditiva/update.html'
    success_url = reverse_lazy('tipo_perda_auditiva:index')
    login_url = "/authentication/login/"


class TipoDeleteView(LoginRequiredMixin, DeleteView):
    model = Tipo
    success_url = reverse_lazy('tipo_perda_auditiva:index')
    template_name = 'tipo_perda_auditiva/tipo_check_delete.html'
    login_url = "/authentication/login/"
