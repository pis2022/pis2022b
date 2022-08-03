import imp
from django.contrib import admin


# Register your models here.
from .models import Iffaa
from .models import Ipersona
from .models import Ipolicia
from .models import Mareasori
from .models import Mcalibrearma
from .models import Mestado
from .models import Mestadocivil
from .models import Mfactor
from .models import Mgenero
from .models import Mgrado
from .models import Mgradoinstruccion
from .models import Mpais
from .models import Mparentesco
from .models import Mprocedencia
from .models import Msitpolicial
from .models import Mubigeo
from .models import Munidadespnp
#users
from .models import Rfamiliares
from .models import Rfiliacionpolitica
from .models import Rpenales
from .models import Tipocontextura
from .models import Tipodocori
from .models import Tipodocumento
from .models import Tipoffaa
from .models import Tipoorgpolitica
from .models import Tipopersona
from .models import Tiporaza
from .models import Unidad

class EstadoCivilAdmin(admin.ModelAdmin):
    list_display = ('id','estadocivil')
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id','nrodoc','apepaterno','apematerno','nombres','fechanacimiento','natural','domicilio','telefono')
    list_filter = ('apepaterno','nrodoc')

admin.site.register(Iffaa)
admin.site.register(Ipersona, PersonaAdmin)
admin.site.register(Ipolicia)
admin.site.register(Mareasori)
admin.site.register(Mcalibrearma)
admin.site.register(Mestado)
admin.site.register(Mestadocivil, EstadoCivilAdmin)
admin.site.register(Mfactor)
admin.site.register(Mgenero)
admin.site.register(Mgrado)
admin.site.register(Mgradoinstruccion)
admin.site.register(Mpais)
admin.site.register(Mparentesco)
admin.site.register(Mprocedencia)
admin.site.register(Msitpolicial)
admin.site.register(Mubigeo)
admin.site.register(Munidadespnp)
#user
admin.site.register(Rfamiliares)
admin.site.register(Rfiliacionpolitica)
admin.site.register(Rpenales)
admin.site.register(Tipocontextura)
admin.site.register(Tipodocori)
admin.site.register(Tipodocumento)
admin.site.register(Tipoffaa)
admin.site.register(Tipoorgpolitica)
admin.site.register(Tipopersona)
admin.site.register(Tiporaza)
admin.site.register(Unidad)
