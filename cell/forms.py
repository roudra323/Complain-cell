from django import forms
from .models import cellf


class cellfForm(forms.ModelForm):
    class Meta:
        model = cellf
        fields = "__all__"  # < /pre >
