from django import forms
from .models import Pytje


class PytjaForm(forms.ModelForm):
    class Meta:
        model = Pytje
        # fields ='__all__'
        fields = ['EmriMbiemri','Email','NumriTelefonit','Pytja']