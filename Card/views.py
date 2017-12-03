from django.shortcuts import render, redirect
from .models import Perfil, Enciclopedia, Galeria, IdentificarMovimiento, CorregirInformacion, ReordenacionMovimiento, Retroalimentacion
from .forms import User_Form, Enciclopedia_Form, Galeria_Form, IdentificarMovimiento_Form, CorregirInformacion_Form, ReordenacionMovimiento_Form, Retroalimentacion_Form
from django.contrib.auth import authenticate, login
from .forms import User_Form
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def base(request):
    return render(request, 'base.html', {})

def index(request):
    return render(request, 'index.html', {})

def enciclopedia(request):
    form = IdentificarMovimiento_Form(request.POST or None, request.FILES or None)
    form2 = CorregirInformacion_Form(request.POST or None, request.FILES or None)
    form3 = ReordenacionMovimiento_Form(request.POST or None, request.FILES or None)
    form4 = Retroalimentacion_Form(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    if request.method == "POST":
        if form2.is_valid():
            form2.save()
    if request.method == "POST":
        if form3.is_valid():
            form3.save()
    if request.method == "POST":
        if form4.is_valid():
            form4.save()
    return render(request, 'enciclopedia.html', {"form":form, "form2":form2, "form3":form3, "form4":form4})

def galeria(request):
    form = Galeria_Form(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, 'galeria.html', {"form":form})

def guia(request):
    return render(request, 'guia.html', {})

def historia(request):
    return render(request, 'historia.html', {})

class SignUp(FormView):
    template_name = 'signup.html'
    form_class = User_Form
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        p = Perfil()
        p.usuario = user
        p.nombre = form.cleaned_data['nombre']
        p.apellidoP = form.cleaned_data['apellidoP']
        p.apellidoM = form.cleaned_data['apellidoM']
        p.tiempoPracticando = form.cleaned_data['tiempoPracticando']
        p.movimientosFavoritos = form.cleaned_data['movimientosFavoritos']
        p.movimientosOriginales = form.cleaned_data['movimientosOriginales']
        p.imagen = form.cleaned_data['imagen']
        p.ciudad = form.cleaned_data['ciudad']
        p.correo = form.cleaned_data['correo']
        p.youtube = form.cleaned_data['youtube']
        p.instagram = form.cleaned_data['instagram']
        p.reddit = form.cleaned_data['reddit']
        p.save()

        return super(SignUp, self).form_valid(form)
