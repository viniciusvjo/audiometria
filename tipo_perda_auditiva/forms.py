from django import forms
from .models import Tipo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit


class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ('tipo_perda', 'caracteristicas',)

    tipo_perda = forms.CharField(
        label="Tipo de perda auditiva",
        max_length=40,
        required=True,
    )

    caracteristicas = forms.CharField(
        label="Características",
        max_length=200,
        required=True,
    )
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Teste',
            ),
            Submit('submit', 'Salvar', css_class='btn btn-primary'),
        )"""

    def clean(self, *args, **kwargs):
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        error_msg_required_field = 'Este campo é obrigatório'

        tipo_perda_data = cleaned.get('tipo_perda')
        caracteristicas_data = cleaned.get('caracteristicas')

        if not tipo_perda_data:
            validation_error_msgs['tipo_perda'] = error_msg_required_field

        if not caracteristicas_data:
            validation_error_msgs['caracteristicas'] = error_msg_required_field

        if validation_error_msgs:
            raise (forms.ValidationError(validation_error_msgs))

