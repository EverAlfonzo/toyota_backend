from django import  forms

from talleres.models import Taller


class TallerForm(forms.ModelForm):
    class Meta:
        model = Taller
        fields = '__all__'
