from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Div, Layout, Row, Submit

from saas_boilerplate.organisations.models import Organisation


class OrganisationForm(forms.ModelForm):
    logo = forms.ImageField(
        label=_("Logo"),
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Organisation
        fields = [
            'name',
            'description',
            'logo'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("logo", css_class="form-group col-md-6 mb-0"),
                Column("name", css_class="form-group col-md-6 mb-0"),
            ),
            Row(
                Column("description", css_class="form-group col-md-12 mb-0"),
            ),
            Submit("submit", _("Save"), css_class="btn btn-primary")
        )
        self.fields['name'].required = True
