from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil, Enciclopedia, Galeria, IdentificarMovimiento, CorregirInformacion, ReordenacionMovimiento, Retroalimentacion

class User_Form(UserCreationForm):
    nombre = forms.CharField(max_length = 50)
    apellidoP = forms.CharField(max_length = 50)
    apellidoM = forms.CharField(max_length = 50, required = False)
    tiempoPracticando = forms.DateTimeField(required = False)
    movimientosFavoritos = forms.CharField(widget = forms.Textarea)
    movimientosOriginales = forms.CharField(widget = forms.Textarea)
    imagen = forms.ImageField()
    ciudad = forms.CharField(max_length = 35)
    correo = forms.CharField(max_length = 50)
    youtube = forms.URLField(max_length = 100, required = False)
    instagram = forms.URLField(max_length = 100, required = False)
    reddit = forms.URLField(max_length = 100, required = False)

class Enciclopedia_Form(forms.ModelForm):
	class Meta:
		model = Enciclopedia
		fields = '__all__'

class Galeria_Form(forms.ModelForm):
	class Meta:
		model = Galeria
		fields = '__all__'

class IdentificarMovimiento_Form(forms.ModelForm):
	class Meta:
		model = IdentificarMovimiento
		fields = '__all__'

class CorregirInformacion_Form(forms.ModelForm):
	class Meta:
		model = CorregirInformacion
		fields = '__all__'

class ReordenacionMovimiento_Form(forms.ModelForm):
	class Meta:
		model = ReordenacionMovimiento
		fields = '__all__'

class Retroalimentacion_Form(forms.ModelForm):
	class Meta:
		model = Retroalimentacion
		fields = '__all__'
