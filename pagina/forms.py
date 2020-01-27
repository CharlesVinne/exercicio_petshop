from django import forms
from pagina.models import Pet, Pessoa, Ong

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class OngForm(forms.ModelForm):
    class Meta:
        model = Ong
        fields = '__all__'