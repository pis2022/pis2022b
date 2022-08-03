
import imp
from django.contrib import admin
from django.urls import path

from ProyectoPNP.vista import index
from ProyectoPNP import vista
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    
    path('admin/', admin.site.urls),
    path('', include('Aplicacion1.urls')),
    path('index/',index),


    #path('documentType/form', vista.registerTipoDocumento),
    #path('documentType/create', vista.createTipoDocumento),
    #path('documentType/', vista.listTipoDocumento),
    #path('documentType/delete/<id>', vista.deleteTipoDocumento),
    #path('documentType/edit/<id>', vista.editTipoDocumento),
    #path('documentType/modify/<id>', vista.modifyTipoDocumento),
    #path('documentType/view/<id>', vista.viewTipoDocumento),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
