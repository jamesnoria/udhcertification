from django.contrib import admin
from django.urls import path

from cert_gen import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),

    # generators front-end:
    path('ic/', views.innovation_challenge),
    path('men/', views.mentores),
    path('pon/', views.ponentes),
    path('log/', views.des_log),
    path('innova/', views.innova),
    path('ambiente/', views.ani_ambiente),
    path('conf_inter/', views.conf_internacional),

    # generators back-end:
    path('generator_ic/', views.generator_ic),
    path('generator_men/', views.generator_men),
    path('generator_pon/', views.generator_pon),
    path('generator_des_log/', views.generator_des_log),
    path('generator_innova/', views.generator_innova),
    path('generator_ani/', views.generator_ani),
    path('generator_conf/', views.generator_conf),

    # Ambiental
    path('buscador/', views.buscador),
    path('db/', views.db),
    path('test/', views.test),
    path('validator/', views.validator),
    path('validator_action/', views.validator_action),

    # Ambiental - Organizadores
    path('buscador_docente/', views.buscador_docente),
    path('db_docente/', views.db_docente),
    path('test_docente/', views.test_docente),

    # Bindin
    path('buscador_bindin/', views.buscador_bindin),
    path('db_bindin/', views.db_bindin),
    path('test_bindin/', views.test_bindin),

    # Bindin - Organizadores
    path('buscador_bindin_org/', views.buscador_bindin_org),
    path('db_bindin_org/', views.db_bindin_org),
    path('test_bindin_org/', views.test_bindin_org),

    # Asistencia Bindin2
    path('buscador_asistencia/', views.buscador_asistencia),
    path('table_validation/', views.table_validation),
    path('table_asistencia/', views.table_bindin2),

]

# Hide side bar in admin-page:
admin.autodiscover()
admin.site.enable_nav_sidebar = False

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
