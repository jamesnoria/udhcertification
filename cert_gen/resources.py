from import_export import resources
from .models import Registro
from .models import Mentore

class RegistroResource(resources.ModelResource):
    class Meta:
        model = Registro

class RegistroResource(resources.ModelResource):
    class Meta:
        model = Mentore