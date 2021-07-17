from django.db import models

# ----- Aniversario Ambiental ---->


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

# ----- BINDIN ----->


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
        verbose_name_plural = 'Semillero Internacional - PARTICIPANTES'


class ConferenciaInternacionalOrg(models.Model):
    """Model definition for ConferenciaInternacionalOrg."""

    nombre_organizador = models.CharField(
        max_length=100, null=True, verbose_name="Nombre y Apellidos")
    dni = models.CharField(max_length=100, null=True, verbose_name="dni")
    universidad = models.CharField(
        max_length=100, null=True, verbose_name="universidad")

    class Meta:
        """Meta definition for ConferenciaInternacionalOrg."""
        verbose_name = 'Semillero Internacional'
        verbose_name_plural = 'Semillero Internacional - ORGANIZADORES'

    def __str__(self):
        """Unicode representation of ConferenciaInternacionalOrg."""
        return self.nombre_organizador


# ---- ECO-CONCURSO ----->

class EcoConcurso(models.Model):
    """Model definition for EcoConcurso."""

    nombre_participante = models.CharField(
        max_length=100, null=True, verbose_name='Nombre Participante')
    dni = models.CharField(max_length=100, null=True,
                           verbose_name='dni o código de alumno')
    correo = models.CharField(max_length=100, null=True, verbose_name='email')

    class Meta:
        """Meta definition for EcoConcurso."""

        verbose_name = 'Eco Creatividad - BBDD'
        verbose_name_plural = 'Eco Creatividad - BBDD'

    def __str__(self):
        """Unicode representation of EcoConcurso."""
        return self.nombre_participante


class EcoAsistencia(models.Model):
    """Model definition for EcoAsistencia."""

    nombre_participante = models.CharField(
        max_length=100, null=True, verbose_name='Nombre Participante')
    dni = models.CharField(max_length=100, null=True,
                           verbose_name='dni o código de alumno')
    correo = models.CharField(max_length=100, null=True, verbose_name='email')

    class Meta:
        """Meta definition for EcoAsistencia."""

        verbose_name = 'Eco Creatividad - ASISTENCIA'
        verbose_name_plural = 'Eco Creatividad - ASISTENCIA'

    def __str__(self):
        """Unicode representation of EcoAsistencia."""
        return self.nombre_participante
