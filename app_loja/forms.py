# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext as _
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)

        # Personalize as mensagens de erro conforme necessário
        self.fields['old_password'].label = 'Senha Atual'
        self.error_messages['password_incorrect'] = 'A senha atual não está correta.'
        self.error_messages['password_mismatch'] = 'As novas senhas não coincidem.'

class PedidoForm(forms.Form):
    SEGMENTO_CHOICES = [
        ('batizado', 'Batizado'),
        ('debutante', 'Debutante'),
        ('casamento', 'Casamento'),
        ('aniversario', 'Aniversário'),
    ]

    MASSA_CHOICES = [
        ('baunilha', 'Baunilha'),
        ('cenoura', 'Cenoura'),
        ('paodelo', 'Pão de Ló'),
        ('festa', 'Festa'),
    ]

    RECHEIO_CHOICES = [
        ('brigadeiro', 'Brigadeiro'),
        ('docedeleite', 'Doce de Leite'),
        ('abacaxi', 'Abacaxi'),
        ('morango', 'Morango'),
    ]

    segmento = forms.ChoiceField(choices=SEGMENTO_CHOICES, widget=forms.RadioSelect)
    massa = forms.ChoiceField(choices=MASSA_CHOICES, widget=forms.RadioSelect)
    recheio = forms.ChoiceField(choices=RECHEIO_CHOICES, widget=forms.RadioSelect)
    data_de_entrega = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    detalhes = forms.CharField(widget=forms.Textarea)
    contato = forms.CharField()
    # Adicione outros campos conforme necessário para o seu pedido