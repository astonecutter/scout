from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from djangae.contrib.gauth.models import GaeDatastoreUser
from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = GaeDatastoreUser
        fields = ('email',)

    @property
    def helper(self):
        h = FormHelper()
        h.layout = Layout(
            'email',
            FormActions(
                Submit('submit', 'Save')
            )
        )
        return h
