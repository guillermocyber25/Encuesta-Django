from django.contrib import admin

# Register your models here.

from models import Conferencia
from models import Evento
from models import Pregunta
from models import RelPregunta
from models import RelUe
from models import Usuario
from models import Respuesta

admin.site.register(Conferencia)
admin.site.register(Evento)
admin.site.register(Pregunta)
admin.site.register(RelPregunta)
admin.site.register(RelUe)
admin.site.register(Usuario)
admin.site.register(Respuesta)


