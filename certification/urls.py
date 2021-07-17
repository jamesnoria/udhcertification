from django.contrib import admin
from django.urls import path

from cert_gen import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),

    # Ambiental
    path('buscador/', views.buscador, name='buscador_ambiental'),
    path('db/', views.db, name='db_ambiental_alum'),
    path('test/', views.test, name='cert_gen_amb_alum'),
    path('validator/', views.validator, name='buscador_validador'),
    path('validator_action/', views.validator_action, name='qr_validador'),

    # Ambiental - Organizadores
    path('buscador_docente/', views.buscador_docente,
         name='buscador_ambiental_org'),
    path('db_docente/', views.db_docente, name='db_ambiental_org'),
    path('test_docente/', views.test_docente, name='cert_gen_amb_org'),

    # Bindin
    path('buscador_bindin/', views.buscador_bindin, name='buscador_bindin_part'),
    path('db_bindin/', views.db_bindin, name='db_bindin_part'),
    path('test_bindin/', views.test_bindin, name='cert_gen_bindin_part'),

    # Bindin - Organizadores
    path('buscador_bindin_org/', views.buscador_bindin_org,
         name='buscador_bindin_org'),
    path('db_bindin_org/', views.db_bindin_org, name='db_bindin_org'),
    path('test_bindin_org/', views.test_bindin_org, name='cert_gen_bindin_org'),

    # Asistencia ECO-CREATIVIDAD
    path('buscador_asistencia/', views.buscador_asistencia,
         name='buscador_asistencia_eco'),
    path('table_validation/', views.table_validation, name='table_validador_eco'),
    path('table_asistencia/', views.table_bindin2, name='table_asistencia_eco'),

]

# Hide side bar in admin-page:
admin.autodiscover()
admin.site.enable_nav_sidebar = False

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
