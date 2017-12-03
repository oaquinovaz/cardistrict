from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from Cardistrict import settings
from django.contrib.auth.views import login, logout_then_login
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index, name="index"),
    url(r'^enciclopedia/$', views.enciclopedia, name="enciclopedia"),
    url(r'^galeria/$', views.galeria, name="galeria"),
    url(r'^guia/$', views.guia, name="guia"),
    url(r'^historia/$', views.historia, name="historia"),
    url(r'^login/$', login, {'template_name': 'iniciar_sesion.html'}, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^signup/$', views.SignUp.as_view(),name="signup"),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
