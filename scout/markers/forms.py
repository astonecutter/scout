from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

from scout.markers.models import Marker


class MarkerForm(forms.ModelForm):

    class Meta:
        model = Marker
        exclude = ()

    @property
    def helper(self):
        h = FormHelper()
        h.layout = Layout(
            'name',
            'lat',
            'long',
            FormActions(
                Submit('submit', 'Save')
            )
        )
        return h