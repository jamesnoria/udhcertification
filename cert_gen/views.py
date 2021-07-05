from django.shortcuts import render
from django.http import HttpResponse

from certification import settings

from .models import Registro
from .models import Mentore
from .models import Ponentes
from .models import Des_Log
from .models import Innova
from .models import AniversarioAmbiente
from .models import AniversarioAmbientalDocente
from .models import ConferenciaInternacional
from .models import Bindin

import io
from PIL import Image, ImageDraw, ImageFont


def index(request):

    return render(request, 'index.html')


def registro_general(request):

    return render(request, 'register_form.html')


def innovation_challenge(request):

    return render(request, 'generadores/innovation_cha.html')


def mentores(request):

    return render(request, 'generadores/mentores.html')


def ponentes(request):

    return render(request, 'generadores/ponentes.html')


def des_log(request):

    return render(request, 'generadores/des_logistica.html')


def innova(request):

    return render(request, 'generadores/innova62.html')


def ani_ambiente(request):

    return render(request, 'generadores/ambiente.html')


def conf_internacional(request):

    return render(request, 'generadores/conf_inter.html')


def generator_ic(request):
    """
    generador para innovation challenge
    """
    if request.method == 'GET':

        db = Registro()
        db.nombre_alumno = request.GET["name"].title()
        db.username = request.user.username
        db.dni = request.GET["dni"]
        db.carrera = request.GET["carrera"]
        db.evento = "Innovation Challenge"
        db.save()

    stream = io.BytesIO()
    nombre = request.GET["name"]

    certificado = Image.open(
        f'{settings.BASE_DIR}/staticfiles/images/certificado.jpg')
    nuevo = ImageDraw.Draw(certificado)

    coordenadas = (589, 483)
    color_texto = (0, 0, 0)
    tipo_letra = ImageFont.truetype(
        f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 200)

    nuevo.text(coordenadas, nombre.title(), fill=color_texto, font=tipo_letra)
    certificado.save(stream, format='pdf')

    pdf_response = HttpResponse(
        stream.getvalue(), content_type='application/pdf')
    pdf_response['Content-Disposition'] = f'attachment; filename={nombre.title()}.pdf'

    return pdf_response


def generator_men(request):
    """
    generador para mentores
    """
    if request.method == 'GET':

        db = Mentore()
        db.nombre_mentor = request.GET["name"].title()
        db.username = request.user.username
        db.save()

    stream = io.BytesIO()
    nombre = request.GET["name"]

    certificado = Image.open(
        f'{settings.BASE_DIR}/staticfiles/images/certificado.jpg')
    nuevo = ImageDraw.Draw(certificado)

    coordenadas = (589, 483)
    color_texto = (0, 0, 0)
    tipo_letra = ImageFont.truetype(
        f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 200)

    nuevo.text(coordenadas, nombre.title(), fill=color_texto, font=tipo_letra)
    certificado.save(stream, format='pdf')

    pdf_response = HttpResponse(
        stream.getvalue(), content_type='application/pdf')
    pdf_response['Content-Disposition'] = f'attachment; filename={nombre.title()}.pdf'

    return pdf_response


def generator_pon(request):
    """
    generador para ponentes
    """
    if request.method == 'GET':

        db = Ponentes()
        db.nombre_ponente = request.GET["name"].title()
        db.username = request.user.username
        db.save()

    stream = io.BytesIO()
    nombre = request.GET["name"]

    certificado = Image.open(
        f'{settings.BASE_DIR}/staticfiles/images/certificado.jpg')
    nuevo = ImageDraw.Draw(certificado)

    coordenadas = (589, 483)
    color_texto = (0, 0, 0)
    tipo_letra = ImageFont.truetype(
        f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 200)

    nuevo.text(coordenadas, nombre.title(), fill=color_texto, font=tipo_letra)
    certificado.save(stream, format='pdf')

    pdf_response = HttpResponse(
        stream.getvalue(), content_type='application/pdf')
    pdf_response['Content-Disposition'] = f'attachment; filename={nombre.title()}.pdf'

    return pdf_response


def generator_des_log(request):
    """
    generador para Desarrollo y Logistica
    """
    if request.method == 'GET':

        db = Des_Log()
        db.nombre_participante = request.GET["name"].title()
        db.username = request.user.username
        db.save()

    stream = io.BytesIO()
    nombre = request.GET["name"]

    certificado = Image.open(
        f'{settings.BASE_DIR}/staticfiles/images/certificado.jpg')
    nuevo = ImageDraw.Draw(certificado)

    coordenadas = (589, 483)
    color_texto = (0, 0, 0)
    tipo_letra = ImageFont.truetype(
        f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 200)

    nuevo.text(coordenadas, nombre.title(), fill=color_texto, font=tipo_letra)
    certificado.save(stream, format='pdf')

    pdf_response = HttpResponse(
        stream.getvalue(), content_type='application/pdf')
    pdf_response['Content-Disposition'] = f'attachment; filename={nombre.title()}.pdf'

    return pdf_response


def generator_innova(request):
    """
    generador para innova62
    """
    if request.method == 'GET':

        db = Innova()
        db.nombre_participante = request.GET["name"].title()
        db.username = request.user.username
        db.save()

    stream = io.BytesIO()
    nombre = request.GET["name"]

    certificado = Image.open(
        f'{settings.BASE_DIR}/staticfiles/images/certificado.jpg')
    nuevo = ImageDraw.Draw(certificado)

    coordenadas = (589, 483)
    color_texto = (0, 0, 0)
    tipo_letra = ImageFont.truetype(
        f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 200)

    nuevo.text(coordenadas, nombre.title(), fill=color_texto, font=tipo_letra)
    certificado.save(stream, format='pdf')

    pdf_response = HttpResponse(
        stream.getvalue(), content_type='application/pdf')
    pdf_response['Content-Disposition'] = f'attachment; filename={nombre.title()}.pdf'

    return pdf_response


def generator_ani(request):
    """
    generador para aniversario de ambiental
    """
    if request.method == 'GET':

        db = AniversarioAmbiente()
        db.nombre_participante = request.GET["name"].upper()
        db.codigo_udh = request.GET["dni"]
        db.email = request.GET["email"]
        db.save()

    stream = io.BytesIO()
    nombre = request.GET["name"]
    name = nombre.replace(',', '')
    codigo = 'none'

    if len(name) <= 22:

        certificado = Image.open(
            f'{settings.BASE_DIR}/staticfiles/images/certificado_ambiental.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (531, 564)
        coordenadas_2 = (222, 364)
        color_texto = (0, 0, 0)
        tipo_letra = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 200)
        tipo_letra_2 = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/script.ttf', 30)

        nuevo.text(coordenadas, name.title(),
                   fill=color_texto, font=tipo_letra)
        nuevo.text(coordenadas_2, codigo, fill=color_texto, font=tipo_letra_2)
        certificado.save(stream, format='pdf')

        pdf_response = HttpResponse(
            stream.getvalue(), content_type='application/pdf')
        pdf_response['Content-Disposition'] = f'attachment; filename={name.title()}.pdf'

        return pdf_response

    elif len(name) <= 30:

        certificado = Image.open(
            f'{settings.BASE_DIR}/staticfiles/images/certificado_ambiental.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (531, 564)
        coordenadas_2 = (222, 364)
        color_texto = (0, 0, 0)
        tipo_letra = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 180)
        tipo_letra_2 = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/script.ttf', 30)

        nuevo.text(coordenadas, name.title(),
                   fill=color_texto, font=tipo_letra)
        nuevo.text(coordenadas_2, codigo, fill=color_texto, font=tipo_letra_2)
        certificado.save(stream, format='pdf')

        pdf_response = HttpResponse(
            stream.getvalue(), content_type='application/pdf')
        pdf_response['Content-Disposition'] = f'attachment; filename={name.title()}.pdf'

        return pdf_response

    else:

        certificado = Image.open(
            f'{settings.BASE_DIR}/staticfiles/images/certificado_ambiental.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (528, 606)
        coordenadas_2 = (222, 364)
        color_texto = (0, 0, 0)
        tipo_letra = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 150)
        tipo_letra_2 = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/script.ttf', 30)

        nuevo.text(coordenadas, name.title(),
                   fill=color_texto, font=tipo_letra)
        nuevo.text(coordenadas_2, codigo, fill=color_texto, font=tipo_letra_2)
        certificado.save(stream, format='pdf')

        pdf_response = HttpResponse(
            stream.getvalue(), content_type='application/pdf')
        pdf_response['Content-Disposition'] = f'attachment; filename={name.title()}.pdf'

        return pdf_response


def generator_conf(request):
    """
    generador para conferencia internacional
    """
    if request.method == 'GET':

        db = ConferenciaInternacional()
        db.nombre_participante = request.GET["name"].title()
        db.username = request.user.username
        db.save()

    stream = io.BytesIO()
    nombre = request.GET["name"]

    certificado = Image.open(
        f'{settings.BASE_DIR}/staticfiles/images/certificado.jpg')
    nuevo = ImageDraw.Draw(certificado)

    coordenadas = (589, 483)
    color_texto = (0, 0, 0)
    tipo_letra = ImageFont.truetype(
        f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 200)

    nuevo.text(coordenadas, nombre.title(), fill=color_texto, font=tipo_letra)
    certificado.save(stream, format='pdf')

    pdf_response = HttpResponse(
        stream.getvalue(), content_type='application/pdf')
    pdf_response['Content-Disposition'] = f'attachment; filename={nombre.title()}.pdf'

    return pdf_response

# ----- AMBIENTAL ----->


def buscador(request):
    """ Buscador para ambiental """
    return render(request, 'buscador.html')


def db(request):
    """ BD que conecta con table.html """
    codigo_udh = request.GET["dni"]

    try:
        if AniversarioAmbiente.objects.get(codigo_udh__exact=codigo_udh):
            registro = AniversarioAmbiente.objects.filter(
                codigo_udh=codigo_udh)
            context = {
                'registros': registro,
            }
            return render(request, 'table.html', context)

    except AniversarioAmbiente.DoesNotExist:
        return render(request, 'not_found.html')


def test(request):
    """ Generador en table.html """
    stream = io.BytesIO()
    nombre = request.GET["nombre"]
    name = nombre.replace(',', '')
    codigo = request.GET["validation_code"]

    if len(name) <= 22:

        certificado = Image.open(
            f'{settings.BASE_DIR}/staticfiles/images/certificado_ambiental.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (531, 564)
        coordenadas_2 = (222, 364)
        color_texto = (0, 0, 0)
        tipo_letra = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 200)
        tipo_letra_2 = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/script.ttf', 30)

        nuevo.text(coordenadas, name.title(),
                   fill=color_texto, font=tipo_letra)
        nuevo.text(coordenadas_2, codigo, fill=color_texto, font=tipo_letra_2)
        certificado.save(stream, format='pdf')

        pdf_response = HttpResponse(
            stream.getvalue(), content_type='application/pdf')
        pdf_response['Content-Disposition'] = f'attachment; filename={name.title()}.pdf'

        return pdf_response

    elif len(name) <= 30:

        certificado = Image.open(
            f'{settings.BASE_DIR}/staticfiles/images/certificado_ambiental.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (531, 564)
        coordenadas_2 = (222, 364)
        color_texto = (0, 0, 0)
        tipo_letra = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 180)
        tipo_letra_2 = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/script.ttf', 30)

        nuevo.text(coordenadas, name.title(),
                   fill=color_texto, font=tipo_letra)
        nuevo.text(coordenadas_2, codigo, fill=color_texto, font=tipo_letra_2)
        certificado.save(stream, format='pdf')

        pdf_response = HttpResponse(
            stream.getvalue(), content_type='application/pdf')
        pdf_response['Content-Disposition'] = f'attachment; filename={name.title()}.pdf'

        return pdf_response

    else:

        certificado = Image.open(
            f'{settings.BASE_DIR}/staticfiles/images/certificado_ambiental.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (528, 606)
        coordenadas_2 = (222, 364)
        color_texto = (0, 0, 0)
        tipo_letra = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 150)
        tipo_letra_2 = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/script.ttf', 30)

        nuevo.text(coordenadas, name.title(),
                   fill=color_texto, font=tipo_letra)
        nuevo.text(coordenadas_2, codigo, fill=color_texto, font=tipo_letra_2)
        certificado.save(stream, format='pdf')

        pdf_response = HttpResponse(
            stream.getvalue(), content_type='application/pdf')
        pdf_response['Content-Disposition'] = f'attachment; filename={name.title()}.pdf'

        return pdf_response

# ----- AMBIENTAL - ORGANIZADORES ---->


def buscador_docente(request):
    """ Buscador para organizadores AMBIENTAL """
    return render(request, 'buscador_amb_doc.html')


def db_docente(request):
    """ BD que conecta con table_amb_doc.html """
    codigo_udh = request.GET["dni"]

    try:
        if AniversarioAmbientalDocente.objects.get(dni__exact=codigo_udh):
            registro = AniversarioAmbientalDocente.objects.filter(
                dni=codigo_udh)
            context = {
                'registros': registro,
            }
            return render(request, 'table_amb_doc.html', context)

    except AniversarioAmbientalDocente.DoesNotExist:
        return render(request, 'not_found_amb_org.html')


def test_docente(request):
    """ Generador para certificados organizadores """
    stream = io.BytesIO()
    name = request.GET["nombre"]

    if len(name) <= 22:

        certificado = Image.open(
            f'{settings.BASE_DIR}/staticfiles/images/certificado_organizador.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (953, 865)
        color_texto = (0, 0, 0)
        tipo_letra = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 230)

        nuevo.text(coordenadas, name.title(),
                   fill=color_texto, font=tipo_letra)
        certificado.save(stream, format='pdf')

        pdf_response = HttpResponse(
            stream.getvalue(), content_type='application/pdf')
        pdf_response['Content-Disposition'] = f'attachment; filename={name.title()}.pdf'

        return pdf_response

    elif len(name) <= 30:

        certificado = Image.open(
            f'{settings.BASE_DIR}/staticfiles/images/certificado_organizador.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (846, 870)
        color_texto = (0, 0, 0)
        tipo_letra = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 200)

        nuevo.text(coordenadas, name.title(),
                   fill=color_texto, font=tipo_letra)
        certificado.save(stream, format='pdf')

        pdf_response = HttpResponse(
            stream.getvalue(), content_type='application/pdf')
        pdf_response['Content-Disposition'] = f'attachment; filename={name.title()}.pdf'

        return pdf_response

    else:

        certificado = Image.open(
            f'{settings.BASE_DIR}/staticfiles/images/certificado_organizador.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (801, 875)
        color_texto = (0, 0, 0)
        tipo_letra = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 200)

        nuevo.text(coordenadas, name.title(),
                   fill=color_texto, font=tipo_letra)
        certificado.save(stream, format='pdf')

        pdf_response = HttpResponse(
            stream.getvalue(), content_type='application/pdf')
        pdf_response['Content-Disposition'] = f'attachment; filename={name.title()}.pdf'

        return pdf_response


# ---- VALIDADOR CODIGO QR AMBIENTAL ----->

def validator(request):
    """ Validator.html """
    return render(request, 'validator.html')


def validator_action(request):
    """ db que conecta con validator """
    codigo_udh = request.GET["dni"]

    try:
        if AniversarioAmbiente.objects.get(validation_code__exact=codigo_udh):
            registro = AniversarioAmbiente.objects.filter(
                validation_code=codigo_udh)
            context = {
                'registros': registro,
            }
            return render(request, 'success.html', context)
    except AniversarioAmbiente.DoesNotExist:
        return render(request, 'not_found.html')

# ----- BINDIN ----->


def buscador_bindin(request):
    """ buscador para buscador_bindin.html """
    return render(request, 'buscador_bindin.html')


def db_bindin(request):
    """ db que conecnta con table_bindin.html """
    dni = request.GET["dni"]

    try:
        if ConferenciaInternacional.objects.get(dni__exact=dni):
            registro = ConferenciaInternacional.objects.filter(
                dni=dni)
            context = {
                'registros': registro,
            }
            return render(request, 'table_bindin.html', context)

    except ConferenciaInternacional.DoesNotExist:
        return render(request, 'not_found_bindin.html')


def test_bindin(request):
    """ Generador en table_bindin.html """
    stream = io.BytesIO()
    name = request.GET["nombre"]

    if len(name) <= 22:

        certificado = Image.open(
            f'{settings.BASE_DIR}/staticfiles/images/certificado_bindin.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (925, 959)
        color_texto = (0, 0, 0)
        tipo_letra = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 400)

        nuevo.text(coordenadas, name.title(),
                   fill=color_texto, font=tipo_letra)
        certificado.save(stream, format='pdf')

        pdf_response = HttpResponse(
            stream.getvalue(), content_type='application/pdf')
        pdf_response['Content-Disposition'] = f'attachment; filename={name.title()}.pdf'

        return pdf_response

    elif len(name) <= 30:

        certificado = Image.open(
            f'{settings.BASE_DIR}/staticfiles/images/certificado_bindin.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (1056, 1023)
        color_texto = (0, 0, 0)
        tipo_letra = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 300)

        nuevo.text(coordenadas, name.title(),
                   fill=color_texto, font=tipo_letra)
        certificado.save(stream, format='pdf')

        pdf_response = HttpResponse(
            stream.getvalue(), content_type='application/pdf')
        pdf_response['Content-Disposition'] = f'attachment; filename={name.title()}.pdf'

        return pdf_response

    else:

        certificado = Image.open(
            f'{settings.BASE_DIR}/staticfiles/images/certificado_bindin.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (851, 1023)
        color_texto = (0, 0, 0)
        tipo_letra = ImageFont.truetype(
            f'{settings.BASE_DIR}/staticfiles/fonts/bergamote.ttf', 300)

        nuevo.text(coordenadas, name.title(),
                   fill=color_texto, font=tipo_letra)
        certificado.save(stream, format='pdf')

        pdf_response = HttpResponse(
            stream.getvalue(), content_type='application/pdf')
        pdf_response['Content-Disposition'] = f'attachment; filename={name.title()}.pdf'

        return pdf_response


# ----- ASISTENCIA ---->

def buscador_asistencia(request):
    """ Buscador con dni y tabla - ONLY HTML """
    return render(request, 'table_dni_finder.html')


def table_bindin2(request):
    """ Se recoge datos de dni validado y se alimenta BD de
    nuevo bindin para luego renderizarlo en table2.html  """
    db = Bindin()
    db.nombre_participante = request.GET["user_name"]
    db.dni = request.GET["user_dni"]
    db.email = request.GET["user_email"]
    db.pais = request.GET["user_pais"]
    db.save()

    bindin = Bindin.objects.all()
    context = {
        'bindins': bindin,
    }
    return render(request, 'table_bindin2.html', context)


def table_validation(request):
    """ Backend que valida que el usuario sea miembro del semillero """

    codigo_udh = request.GET["dni"]

    try:
        if ConferenciaInternacional.objects.get(dni__exact=codigo_udh):
            registro = ConferenciaInternacional.objects.filter(dni=codigo_udh)
            context = {
                'registros': registro,
            }

        return render(request, 'table_dni_finder.html', context)
    except ConferenciaInternacional.DoesNotExist:
        return render(request, 'table_dni_finder.html')
