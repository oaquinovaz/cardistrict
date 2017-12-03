from django.contrib import admin
from .models import Perfil, Enciclopedia, Galeria, IdentificarMovimiento, CorregirInformacion, ReordenacionMovimiento, Retroalimentacion

# Register your models here.
admin.site.register(Perfil)
admin.site.register(Enciclopedia)
admin.site.register(Galeria)
admin.site.register(IdentificarMovimiento)
admin.site.register(CorregirInformacion)
admin.site.register(ReordenacionMovimiento)
admin.site.register(Retroalimentacion)
