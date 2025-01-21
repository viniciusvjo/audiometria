from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from .models import ExameAudiometria
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from paciente.models import Paciente
from .forms import ExameAudiometriaForm
from datetime import datetime
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from django.db.models import Q, DateField
import tempfile
from django.template.loader import render_to_string
import  os
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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


def export_pdf(request):
    exames_audiometria = ExameAudiometria.objects.all()
    total = ExameAudiometria.objects.count()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=ExamesAudiometria' + str(datetime.now()) + '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    html_string = render_to_string('exame_audiometria/pdf-output.html', {'exames_audiometria': exames_audiometria, 'total': total})
    html = HTML(string=html_string)

    font_config = FontConfiguration()
    css = CSS(os.path.join(settings.BASE_DIR, 'exame_audiometria/templates/exame_audiometria/report.css'), font_config=font_config)

    result = html.write_pdf(stylesheets=[css], font_config=font_config)

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return  response

class Search(ExameAudiometriaListView):
    def get_queryset(self, *args, **kwargs):
        search = self.request.GET.get('search')
        data_exame_search = datetime.strptime(self.request.GET.get('data_exame_search'), '%Y-%d-%m').date()
        qs = super().get_queryset(*args, **kwargs)

        #if not search:
            #return qs

        qs = qs.filter(
            Q(paciente__nome__icontains=search) |
            Q(data_exame__date=data_exame_search)
        )

        #logger.info(qs.query)
        return qs
