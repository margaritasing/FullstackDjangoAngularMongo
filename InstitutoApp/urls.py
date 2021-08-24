from django.conf.urls import url
from InstitutoApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^docente$',views.docenteApi),
    url(r'^docente/([0-9]+)$',views.docenteApi),
    url(r'^docentes$',views.docenteApis),
    url(r'^docentes/(?P<id>[0-9]+)$',views.docenteApis),


    url(r'^alumno$',views.alumnoApi),
    url(r'^alumno/([0-9]+)$',views.alumnoApi),
    url(r'^alumnos/(?P<id>[0-9]+)$',views.alumnoApis),


    url(r'^curso$',views.cursoApi),
    url(r'^curso/([0-9]+)$',views.cursoApi),
    url(r'^cursos/(?P<id>[0-9]+)$',views.cursoApis),
    url(r'^alumnosencurso/([0-9]+)$',views.alumnisApi),

    url(r'^docente/savefile',views.saveFile),
    url(r'^alumno/savefile',views.saveFile),

 ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
