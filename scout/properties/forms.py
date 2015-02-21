from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

from scout.properties.models import Property


class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        exclude = ()

    @property
    def helper(self):
        h = FormHelper()
        h.layout = Layout(
            'name',
            'address',
            FormActions(
                Submit('submit', 'Save')
            )
        )
        return h
