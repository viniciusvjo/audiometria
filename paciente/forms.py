from django import forms


class PacienteForm(forms.Form):
    nome = forms.CharField(max_length=80, blank=False, null=False)
    cpf = forms.CharField(max_length=11, blank=False, null=False)
    data_nascimento = forms.DateField(verbose_name='Data de Nascimento')
    endereco = forms.CharField(max_length=100, blank=True, null=True)

