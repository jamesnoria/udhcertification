from django.contrib import admin

from django.contrib.auth.models import Group

from import_export.admin import ImportExportModelAdmin

from .models import Registro
from .models import Mentore
from .models import Ponentes
from .models import Des_Log
from .models import Innova
from .models import AniversarioAmbiente
from .models import ConferenciaInternacional
from .models import RegistroGeneral

class RegistroAdmin(ImportExportModelAdmin):
    list_display=('nombre_alumno', 'creacion_cert', 'username', 'dni', 'carrera', 'id')
    search_fields=('nombre_alumno', 'dni')
    list_filter =('username',)

class MentoreAdmin(ImportExportModelAdmin):
    list_display=('nombre_mentor', 'creacion_cert', 'username', 'dni', 'evento', 'id')
    search_fields=('nombre_mentor', 'dni')
    list_filter =('username', 'evento')

class PonentesAdmin(ImportExportModelAdmin):
    list_display=('nombre_ponente', 'creacion_cert', 'username', 'dni', 'evento', 'id')
    search_fields=('nombre_ponente', 'dni')
    list_filter =('username',)

class DesLogAdmin(ImportExportModelAdmin):
    list_display=('nombre_participante', 'creacion_cert', 'username', 'dni', 'evento', 'id')
    search_fields=('nombre_participante', 'dni')
    list_filter =('username',)

class InnovaAdmin(ImportExportModelAdmin):
    list_display=('nombre_participante', 'creacion_cert', 'username', 'dni', 'carrera', 'id')
    search_fields=('nombre_participante', 'dni')
    list_filter =('username',)

class AniAmbienteAdmin(ImportExportModelAdmin):
    list_display=('nombre_participante', 'creacion_cert', 'codigo_udh', 'email', 'validation_code', 'id')
    search_fields=('nombre_participante', 'codigo_udh')

class ConfInterAdmin(ImportExportModelAdmin):
    list_display=('nombre_participante', 'creacion_cert', 'dni', 'email', 'pais', 'id')
    search_fields=('nombre_participante', 'dni')

class RegistroGeneralAdmin(ImportExportModelAdmin):
    list_display=('id', 'nombre_participante', 'creacion_cert', 'email', 'celular', 'carrera', 'evento')
    search_fields=('nombre_participante', 'codigo_estudiante')
    list_filter =('evento', 'carrera',)

admin.site.register(Registro, RegistroAdmin)
admin.site.register(Mentore, MentoreAdmin)
admin.site.register(Ponentes, PonentesAdmin)
admin.site.register(Des_Log, DesLogAdmin)
admin.site.register(Innova, InnovaAdmin)
admin.site.register(AniversarioAmbiente, AniAmbienteAdmin)
admin.site.register(ConferenciaInternacional, ConfInterAdmin)
admin.site.register(RegistroGeneral, RegistroGeneralAdmin)

admin.site.site_header = 'UDH - CERTIFICADOS'