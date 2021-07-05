from django.db import models


class Registro(models.Model):
    """
    Registro de la creación de un certificado
    """
    nombre_alumno = models.CharField(
        max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de emisión')
    username = models.CharField(
        max_length=100, null=True, verbose_name='Usuario')
    dni = models.CharField(max_length=100, null=True, verbose_name='DNI')
    carrera = models.CharField(
        max_length=100, null=True, verbose_name='Carrera')
    evento = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_alumno

    class Meta:
        verbose_name = 'Innovation Challenge'


class Mentore(models.Model):
    """
    Registro para creacion de certificados en mentores
    """
    nombre_mentor = models.CharField(
        max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de emisión')
    username = models.CharField(
        max_length=100, null=True, verbose_name='Usuario')
    dni = models.CharField(max_length=100, null=True, verbose_name='DNI')
    evento = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_mentor


class Ponentes(models.Model):
    """
    Registro para creacion de certificados en ponentes
    """
    nombre_ponente = models.CharField(
        max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de emisión')
    username = models.CharField(
        max_length=100, null=True, verbose_name='Usuario')
    dni = models.CharField(max_length=100, null=True, verbose_name='DNI')
    evento = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_ponente


class Des_Log(models.Model):
    """
    Registro para creacion de certificados para Desarrollo y Logistica
    """
    nombre_participante = models.CharField(
        max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de emisión')
    username = models.CharField(
        max_length=100, null=True, verbose_name='Usuario')
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
    nombre_participante = models.CharField(
        max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de emisión')
    username = models.CharField(
        max_length=100, null=True, verbose_name='Usuario')
    dni = models.CharField(max_length=100, null=True, verbose_name='DNI')
    carrera = models.CharField(
        max_length=100, null=True, verbose_name='Carrera')
    evento = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_participante

    class Meta:
        verbose_name = 'Innova 62'


class AniversarioAmbiente(models.Model):
    """
    Registro para creacion de certificados para Aniversario Ambiente
    """
    nombre_participante = models.CharField(
        max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de emisión')
    codigo_udh = models.CharField(
        max_length=100, null=True, verbose_name='CODIGO UDH')
    email = models.CharField(max_length=100, null=True, verbose_name='email')
    validation_code = models.CharField(
        max_length=100, null=True, verbose_name='Número de validación')

    def __str__(self):
        return self.nombre_participante

    class Meta:
        verbose_name = 'Aniversario Ambiente'
        verbose_name_plural = 'Aniversario Ambiental ALUMNOS'


class AniversarioAmbientalDocente(models.Model):
    """Model definition for AniversarioAmbientalDocente."""

    docente_nombre = models.CharField(
        max_length=50, null=True, verbose_name='Nombre Docente')
    dni = models.CharField(max_length=50, null=True, verbose_name='dni')
    email = models.CharField(max_length=50, null=True, verbose_name='email')

    class Meta:
        """Meta definition for AniversarioAmbientalDocente."""

        verbose_name = 'Aniversario Ambiental ORGANIZADORES'
        verbose_name_plural = 'Aniversario Ambiental ORGANIZADORES'

    def __str__(self):
        """Unicode representation of AniversarioAmbientalDocente."""
        return self.docente_nombre


class ConferenciaInternacional(models.Model):
    """
    Registro para creacion de certificados para Bindin
    """
    nombre_participante = models.CharField(
        max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de emisión')
    dni = models.CharField(max_length=100, null=True, verbose_name='DNI')
    email = models.CharField(max_length=100, null=True, verbose_name='email')
    pais = models.CharField(max_length=100, null=True, verbose_name='pais')
    evento = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_participante

    class Meta:
        verbose_name = 'Semillero Internacional'
        verbose_name_plural = 'BINDIN'


class RegistroGeneral(models.Model):
    """
    Registro general de eventos
    """
    nombre_participante = models.CharField(
        max_length=100, null=True, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de registro')
    codigo_estudiante = models.CharField(
        max_length=100, null=True, verbose_name='Codigo UDH')
    email = models.CharField(max_length=100, null=True, verbose_name='email')
    celular = models.CharField(
        max_length=100, null=True, verbose_name='Celular')
    carrera = models.CharField(
        max_length=100, null=True, verbose_name='Carrera')
    evento = models.CharField(max_length=100, null=True, verbose_name='Evento')

    def __str__(self):
        return self.nombre_participante

    class Meta:
        verbose_name = 'Registro General'


class Bindin(models.Model):
    """ Nuevo registro """
    nombre_participante = models.CharField(
        max_length=100, verbose_name='Nombre y Apellidos')
    creacion_cert = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de emisión')
    dni = models.CharField(max_length=100, null=True, verbose_name='DNI')
    email = models.CharField(max_length=100, null=True, verbose_name='email')
    pais = models.CharField(max_length=100, null=True, verbose_name='pais')
    evento = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_participante
