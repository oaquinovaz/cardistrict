from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 50)
    apellidoP = models.CharField(max_length = 50)
    apellidoM = models.CharField(max_length = 50, blank = True)
    tiempoPracticando = models.DateTimeField(blank = True, null = True)
    movimientosFavoritos = models.TextField()
    movimientosOriginales = models.TextField()
    imagen = models.ImageField(upload_to="fotos_perfil")
    ciudad = models.CharField(max_length = 35)
    correo = models.CharField(max_length = 50)
    youtube = models.URLField(max_length = 100, blank = True)
    instagram = models.URLField(max_length = 100, blank = True)
    reddit = models.URLField(max_length = 100, blank = True)

    def __str__(self):
        return self.usuario.username

class Enciclopedia(models.Model):
    Grips = 'Grips'
    Spreads = 'Spreads'
    Shuffles = 'Shuffles'
    Isolations = 'Isolations'
    Twirls = 'Twirls'
    Utilities = 'Utilities'
    OneHandedCuts = 'One-Handed Cuts'
    TwoHandedCuts = 'Two-Handed Cuts'
    OneHandedFans = 'One-Handed Fans'
    TwoHandedFans = 'Two-Handed Fans'
    cat = {
        (Grips, 'Grips'),
        (Spreads, 'Spreads'),
        (Shuffles, 'Shuffles'),
        (Isolations, 'Isolations'),
        (Twirls, 'Twirls'),
        (Utilities, 'Utilities'),
        (OneHandedCuts, 'One-Handed Cuts'),
        (TwoHandedCuts, 'Two-Handed Cuts'),
        (OneHandedFans, 'One-Handed Fans'),
        (TwoHandedFans, 'Two-Handed Fans'),
    }

    nombreMovimiento = models.CharField(max_length = 30)
    creador = models.CharField(max_length = 50)
    video = models.FileField(upload_to="movimientos")
    categoria = models.CharField(max_length=16, choices = cat)

    def __str__(self):
        return self.nombreMovimiento

class Galeria(models.Model):
    titulo = models.CharField(max_length = 50)
    descripcion = models.TextField()
    imagenGaleria = models.ImageField(upload_to="galeria")

    def __str__(self):
        return self.titulo

class IdentificarMovimiento(models.Model):
    nombreIMovimiento = models.CharField(max_length = 50)
    linkVideo = models.URLField(max_length = 100)
    minuto = models.IntegerField()
    segundo = models.IntegerField()
    comentario = models.TextField(blank = True)

    def __str__(self):
        return self.nombreIMovimiento

class CorregirInformacion(models.Model):
    nombreCMovimiento = models.ForeignKey(Enciclopedia)
    correccionInfo = models.TextField()
    justificacionInfo = models.TextField()

    def __str__(self):
        return self.nombreCMovimiento.nombreMovimiento

class ReordenacionMovimiento(models.Model):
    nombreRMovimiento = models.ForeignKey(Enciclopedia)
    correccionMov = models.TextField()
    justificacionMov = models.TextField()

    def __str__(self):
        return self.nombreRMovimiento.nombreMovimiento

class Retroalimentacion(models.Model):
    comentarioRetro = models.TextField()

    def __str__(self):
        return self.comentarioRetro
