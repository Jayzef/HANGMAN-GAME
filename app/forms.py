from django import forms
import unicodedata
from .models import *

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields =  ['nome', 'senha']
    
    def __init__(self, *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'usuario'})
        self.fields['senha'].widget = forms.PasswordInput(attrs={'class': 'usuario'})
        
class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['jogador', 'sequencia']
    
    def __init__(self, *args, **kwargs):
        super(JogoForm, self).__init__(*args, **kwargs)
        self.fields['jogador'].widget.attrs.update({'class': 'texto'})
        self.fields['sequencia'].widget.attrs.update({'class': 'texto'})
        
    def clean_palavra(self):
        palavra = self.cleaned_data.get('palavra')
        if palavra:
            palavra = unidecode(palavra).upper()
        return palavra

class SenhaForm(forms.Form):
    usuario = forms.CharField(
        label='Usuário',
        max_length=100
    )
    senha = forms.CharField(
        label='Senha',
        max_length=100,
        widget=forms.PasswordInput()
    )

class palavraForm(forms.ModelForm):
    class Meta:
        model = Palavra
        fields = ['palavra', 'dica', 'CDP']
    
    def __init__(self, *args, **kwargs):
        super(palavraForm, self).__init__(*args, **kwargs)
        self.fields['palavra'].widget.attrs.update({'class': 'palavraF'})
        self.fields['dica'].widget.attrs.update({'class': 'palavraF'})
        self.fields['CDP'].widget.attrs.update({'class': 'palavraF'})
        
    def clean_palavra(self):
        palavra = self.cleaned_data.get('palavra')
        if palavra:
            # Remove acentos e transforma em maiúsculas
            palavra = ''.join(c for c in unicodedata.normalize('NFD', palavra) if unicodedata.category(c) != 'Mn').upper()
        return palavra

class cdpForm(forms.ModelForm):
    class Meta:
        model = ClasseDePalavra
        fields = ['NDC']

    def __init__(self, *args, **kwargs):
        super(cdpForm, self).__init__(*args, **kwargs)
        self.fields['NDC'].widget.attrs.update({'class': 'ndc'})