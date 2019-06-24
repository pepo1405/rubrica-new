from django import forms

from .models import Rubrica, Rubricar

class RubricaForm(forms.ModelForm):

    class Meta:
        model = Rubrica
        fields = ('nome', 'indirizzo', 'telefono', 'fax', 'email',)
		
class RubricarForm(forms.ModelForm):

    class Meta:
        model = Rubricar
        fields = ('ragione_sociale', 'nome', 'incarico', 'telefono', 'cellulare', 'fax', 'email',)