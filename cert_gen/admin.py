# Django
from .models import EcoAsistencia
from .models import EcoConcurso
from .models import ConferenciaInternacionalOrg
from .models import ConferenciaInternacional
from .models import AniversarioAmbientalDocente
from .models import AniversarioAmbiente
from django.contrib import admin
from django.contrib.auth.models import Group

# Pip
from import_export.admin import ImportExportModelAdmin

# --- Aniversario Ambiental --->


class AniAmbienteAdmin(ImportExportModelAdmin):
    list_display = ('nombre_participante', 'creacion_cert',
                    'codigo_udh', 'email', 'validation_code', 'id')
    search_fields = ('nombre_participante', 'codigo_udh')


admin.site.register(AniversarioAmbiente, AniAmbienteAdmin)


class AniAmbienteDocenteAdmin(ImportExportModelAdmin):
    list_display = ('docente_nombre', 'dni', 'email', 'id')
    search_fields = ('docente_nombre', 'dni')


admin.site.register(AniversarioAmbientalDocente, AniAmbienteDocenteAdmin)

# --- Semillero Internacional --->


class ConfInterAdmin(ImportExportModelAdmin):
    list_display = ('nombre_participante', 'creacion_cert',
                    'dni', 'email', 'pais', 'id')
    search_fields = ('nombre_participante', 'dni')


admin.site.register(ConferenciaInternacional, ConfInterAdmin)


class ConfInterOrgAdmin(ImportExportModelAdmin):
    list_display = ('nombre_organizador', 'dni', 'universidad', 'id')
    search_fields = ('nombre_organizador', 'dni')

admin.site.register(ConferenciaInternacionalOrg, ConfInterOrgAdmin)


# --- Eco Concurso --->


class EcoConAdmin(ImportExportModelAdmin):
    list_display = ('nombre_participante', 'dni', 'correo')
    search_fields = ('nombre_participante', 'dni')


admin.site.register(EcoConcurso, EcoConAdmin)


class EcoAsiAdmin(ImportExportModelAdmin):
    list_display = ('nombre_participante', 'dni', 'correo', 'id')
    search_fields = ('nombre_participante', 'dni')

admin.site.register(EcoAsistencia, EcoAsiAdmin)


# ADMIN SITE HEADER

admin.site.site_header = 'UDH - CERTIFICADOS'
