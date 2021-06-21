from django.db import models

class Registro(models.Model):
    """
    Registro de la creación de un certificado
    """
    nombre_alumno = models.CharField(max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de emisión')
    username = models.CharField(max_length=100, null=True, verbose_name='Usuario')
    dni = models.CharField(max_length=100, null=True, verbose_name='DNI')
    carrera = models.CharField(max_length=100, null=True, verbose_name='Carrera')
    evento = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_alumno

    class Meta:
        verbose_name = 'Innovation Challenge'

class Mentore(models.Model):
    """
    Registro para creacion de certificados en mentores
    """
    nombre_mentor = models.CharField(max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de emisión')
    username = models.CharField(max_length=100, null=True, verbose_name='Usuario')
    dni = models.CharField(max_length=100, null=True, verbose_name='DNI')
    evento = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_mentor

class Ponentes(models.Model):
    """
    Registro para creacion de certificados en ponentes
    """
    nombre_ponente = models.CharField(max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de emisión')
    username = models.CharField(max_length=100, null=True, verbose_name='Usuario')
    dni = models.CharField(max_length=100, null=True, verbose_name='DNI')
    evento = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_ponente

class Des_Log(models.Model):
    """
    Registro para creacion de certificados para Desarrollo y Logistica
    """
    nombre_participante = models.CharField(max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de emisión')
    username = models.CharField(max_length=100, null=True, verbose_name='Usuario')
    dni = models.CharField(max_length=100, null=True, verbose_name='DNI')
    evento = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_participante

    class Meta:
        verbose_name = 'Desarrollo & Logistica'

class Innova(models.Model):
    """
    Registro para creacion de certificados para Innova 62
    """
    nombre_participante = models.CharField(max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de emisión')
    username = models.CharField(max_length=100, null=True, verbose_name='Usuario')
    dni = models.CharField(max_length=100, null=True, verbose_name='DNI')
    carrera = models.CharField(max_length=100, null=True, verbose_name='Carrera')
    evento = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_participante

    class Meta:
        verbose_name = 'Innova 62'

class AniversarioAmbiente(models.Model):
    """
    Registro para creacion de certificados para Aniversario Ambiente
    """
    nombre_participante = models.CharField(max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de emisión')
    codigo_udh = models.CharField(max_length=100, null=True, verbose_name='CODIGO UDH')
    email = models.CharField(max_length=100, null=True, verbose_name='email')
    validation_code = models.CharField(max_length=100, null=True, verbose_name='Número de validación')

    def __str__(self):
        return self.nombre_participante

    class Meta:
        verbose_name = 'Aniversario Ambiente'

class ConferenciaInternacional(models.Model):
    """
    Registro para creacion de certificados para Conferencia Internacional
    """
    nombre_participante = models.CharField(max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de emisión')
    dni = models.CharField(max_length=100, null=True, verbose_name='DNI')
    email = models.CharField(max_length=100, null=True, verbose_name='email')
    celular = models.CharField(max_length=100, null=True, verbose_name='celular')
    pais = models.CharField(max_length=100, null=True, verbose_name='pais')
    universidad = models.CharField(max_length=100, null=True, verbose_name='Universidad')
    carrera = models.CharField(max_length=100, null=True, verbose_name='Escuela')
    evento = models.CharField(max_length=100, null=True)
    validation_code = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_participante

    class Meta:
        verbose_name = 'Conferencia Internacional'

class RegistroGeneral(models.Model):
    """
    Registro general de eventos
    """
    nombre_participante = models.CharField(max_length=100, null=True, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    codigo_estudiante = models.CharField(max_length=100, null=True, verbose_name='Codigo UDH')
    email = models.CharField(max_length=100, null=True, verbose_name='email')
    celular = models.CharField(max_length=100, null=True, verbose_name='Celular')
    carrera = models.CharField(max_length=100, null=True, verbose_name='Carrera')
    evento = models.CharField(max_length=100, null=True, verbose_name='Evento')

    def __str__(self):
        return self.nombre_participante

    class Meta:
        verbose_name = 'Registro General'