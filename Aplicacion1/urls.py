from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from ProyectoPNP.settings import MEDIA_ROOT, MEDIA_URL
from . import views

urlpatterns = [
    path('', views.inicio, name ='inicio'),
    path('documentType/form', views.registerTipoDocumento, name = "addDocuments"),
    path('documentType/', views.listTipoDocumento, name = "listDocuments"),
    path('documentType/create', views.createTipoDocumento, name = "addDocument"),
    path('documentType/delete/<id>', views.deleteTipoDocumento, name = "deletDocument"),
    path('documentType/edit/<id>', views.editTipoDocumento, name = "editDocument"),
    path('documentType/modify/<id>', views.modifyTipoDocumento, name = "modifyDocument"),
    path('documentType/view/<id>', views.viewTipoDocumento, name = "viewTypeDocument"),
    path('signup/', views.signup, name = "signup"),
    path('signin/', views.signin, name = "signin"),
    path('logout/', views.logoutUser, name="logout"),




    
    path('documentTypeORI/form', views.registerTipoDocumentoORI, name = "addDocumentsORI"),
    path('documentTypeORI/', views.listTipoDocumentoORI, name = "listDocumentsORI"),
    path('documentTypeORI/create', views.createTipoDocumentoORI, name = "addDocumentORI"),
    path('documentTypeORI/delete/<id>', views.deleteTipoDocumentoORI, name = "deletDocumentORI"),
    path('documentTypeORI/edit/<id>', views.editTipoDocumentoORI, name = "editDocumentORI"),
    path('documentTypeORI/modify/<id>', views.modifyTipoDocumentoORI, name = "modifyDocumentORI"),
    path('documentTypeORI/view/<id>', views.viewTipoDocumentoORI, name = "viewTypeDocumentORI"),



    path('mAreasORI/form', views.registerMAreasORI, name = "addMAreasORI"),
    path('mAreasORI/', views.listMAreasORI, name = "listMAreasORI"),
    path('mAreasORI/create', views.createMAreasORI, name = "addMFactor"),
    path('mAreasORI/delete/<id>', views.deleteMAreasORI, name = "deletMAreaORI"),
    path('mAreasORI/edit/<id>', views.editMAreasORI, name = "editMAreaORI"),
    path('mAreasORI/modify/<id>', views.modifyMAreasORI, name = "modifyMAreaORI"),
    path('mAreasORI/view/<id>', views.viewMAreasORI, name = "viewTypeMAreaORI"),


    
    path('mFactor/form', views.registerMFactor, name = "addMFactor"),
    path('mFactor/', views.listMFactor, name = "listMFactor"),
    path('mFactor/create', views.createMFactor, name = "addMFactor"),
    path('mFactor/delete/<id>', views.deleteMFactor, name = "deletMFactor"),
    path('mFactor/edit/<id>', views.editMFactor, name = "editMFactor"),
    path('mFactor/modify/<id>', views.modifyMFactor, name = "modifyMFactor"),
    path('mFactor/view/<id>', views.viewMFactor, name = "viewTypeMFactor"),




    path('mUserRol/form', views.registerMUserRol, name = "addmUserRol"),
    path('mUserRol/', views.listMUserRol, name = "listmUserRol"),
    path('mUserRol/create', views.createMUserRol, name = "addmUserRol"),
    path('mUserRol/delete/<id>', views.deleteMUserRol, name = "deletmUserRol"),
    path('mUserRol/edit/<id>', views.editMUserRol, name = "editmUserRol"),
    path('mUserRol/modify/<id>', views.modifyMUserRol, name = "modifymUserRol"),
    path('mUserRol/view/<id>', views.viewMUserRol, name = "viewTypemUserRol"),



    
    path('mUserRol/form', views.registerMUserRol, name = "addmUserRol"),
    path('mUserRol/', views.listMUserRol, name = "listmUserRol"),
    path('mUserRol/create', views.createMUserRol, name = "addmUserRol"),
    path('mUserRol/delete/<id>', views.deleteMUserRol, name = "deletmUserRol"),
    path('mUserRol/edit/<id>', views.editMUserRol, name = "editmUserRol"),
    path('mUserRol/modify/<id>', views.modifyMUserRol, name = "modifymUserRol"),
    path('mUserRol/view/<id>', views.viewMUserRol, name = "viewTypemUserRol"),


    path('mUser/form', views.registerMUser, name = "addmUser"),
    path('mUser/', views.listMUser, name = "listmUser"),
    path('mUser/create', views.createMUser, name = "addmUser"),
    path('mUser/delete/<id>', views.deleteMUser, name = "deletmUser"),
    path('mUser/edit/<id>', views.editMUser, name = "editmUser"),
    path('mUser/modify/<id>', views.modifyMUser, name = "modifymUser"),
    path('mUser/view/<id>', views.viewMUser, name = "viewTypemUser"),




    path('iPersona/form', views.registerIPersona, name = "addiPersona"),
    path('iPersona/', views.listIPersona, name = "listiPersona"),
    path('iPersona/create', views.createIPersona, name = "addiPersona"),
    path('iPersona/delete/<id>', views.deleteIPersona, name = "deletiPersona"),
    path('iPersona/edit/<id>', views.editIPersona, name = "editiPersona"),
    path('iPersona/modify/<id>', views.modifyIPersona, name = "modifyiPersona"),
    path('iPersona/view/<id>', views.viewIPersona, name = "viewTypeiPersona"),
    path('ajax_province/', views.load_province, name='ajax_province'),
    path('ajax_cities/', views.load_cities, name="ajax_cities")

]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)      

