# Django
from django.shortcuts import render
from django.http import HttpResponse

# Pip
import io
from PIL import Image, ImageDraw, ImageFont

# My settings for BASE DIR
from certification import settings

# My models
from .models import AniversarioAmbiente
from .models import AniversarioAmbientalDocente
from .models import ConferenciaInternacional
from .models import ConferenciaInternacionalOrg
from .models import EcoAsistencia
from .models import EcoConcurso

# ----- INDEX ----->


def index(request):

    return render(request, 'index.html')

# ----- AMBIENTAL ----->


def buscador(request):
    """ Buscador para ambiental """
    return render(request, 'buscador.html')


def db(request):
    """ BD donde se consulta si el alumno existe o es participante """
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
    """ Generador de certificado una vez que el ususario fue encontrado en la BD """
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
    """ BD donde se consulta si el organizador existe o es participante """
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
    """ Generador de certificado una vez que el ususario fue encontrado en la BD """
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
    """ Valida si la persona es participante o no """
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
    """ Generador de certificado si el usuario valido """
    stream = io.BytesIO()
    name = request.GET["nombre"]

    if len(name) <= 22:

        certificado = Image.open(
            f'{settings.BASE_DIR}/staticfiles/images/certificado_bindin.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (925, 900)
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

        coordenadas = (1056, 990)
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

        coordenadas = (851, 990)
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


# --- BINDIN ORGANIZADOR --->

def buscador_bindin_org(request):

    return render(request, 'buscador_bindin_org.html')


def db_bindin_org(request):
    """ db que busca si el organizador se encuentra en la BD """
    dni = request.GET["dni"]

    try:
        if ConferenciaInternacionalOrg.objects.get(dni__exact=dni):
            registro = ConferenciaInternacionalOrg.objects.filter(
                dni=dni)
            context = {
                'registros': registro,
            }
            return render(request, 'table_bindin_org.html', context)

    except ConferenciaInternacionalOrg.DoesNotExist:
        return render(request, 'not_found_ibndin_org.html')


def test_bindin_org(request):
    """ Generador de certificado si el usuario se encuentra """
    stream = io.BytesIO()
    name = request.GET["nombre"]

    if len(name) <= 22:

        certificado = Image.open(
            f'{settings.BASE_DIR}/staticfiles/images/certificado_bindin_org.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (925, 900)
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
            f'{settings.BASE_DIR}/staticfiles/images/certificado_bindin_org.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (1056, 990)
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
            f'{settings.BASE_DIR}/staticfiles/images/certificado_bindin_org.jpg')
        nuevo = ImageDraw.Draw(certificado)

        coordenadas = (851, 990)
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

# ----- ASISTENCIA ECO - CREATIVIDAD ---->


def buscador_asistencia(request):
    """ Buscador con dni y tabla - ONLY HTML """
    return render(request, 'table_dni_finder.html')


def table_bindin2(request):
    """ Se recoge datos de dni validado y se alimenta BD de
    EcoAsistencia para luego renderizarlo en table2.html  """
    db = EcoAsistencia()
    db.nombre_participante = request.GET["user_name"]
    db.dni = request.GET["user_dni"]
    db.correo = request.GET["user_email"]
    db.save()

    bindin = EcoAsistencia.objects.all()
    context = {
        'bindins': bindin,
    }
    return render(request, 'table_bindin2.html', context)


def table_validation(request):
    """ Backend que valida que el usuario sea miembro del evento (eco-creatividad) """

    codigo_udh = request.GET["dni"]

    try:
        if EcoConcurso.objects.get(dni__exact=codigo_udh):
            registro = EcoConcurso.objects.filter(dni=codigo_udh)
            context = {
                'registros': registro,
            }

        return render(request, 'table_dni_finder.html', context)
    except EcoConcurso.DoesNotExist:
        return render(request, 'table_dni_finder.html')
