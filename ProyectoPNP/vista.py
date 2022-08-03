from xml.dom.minidom import Document
from django.shortcuts import redirect, render
from django.http import HttpResponse
from Aplicacion1.models import Tipodocumento
from django.template import RequestContext
import datetime
def index(request):
	return render(request,'index.html')

def registerTipoDocumento(request):
	return render(request,'Tipodocumento/form.html')

def createTipoDocumento(request):
	
	documento = request.POST.get('Documento',False)
	descripcion =request.POST.get('Descripcion',False)
	obs =request.POST.get('Obs',False)
	TiposdeDocumento = Tipodocumento.objects.create(
		documento=documento,
		descripcion=descripcion,
		activo= "1",
		estado="1",
		obs=obs,
		fechacrea= datetime.datetime.now(),
		fechamodifica=datetime.datetime.now(),
		idusercrea= request.user.id,
		idusermodifica= request.user.id,

		)
	return redirect("/documentType/",  RequestContext(request))

def listTipoDocumento(request):
	TiposdeDocumento=Tipodocumento.objects.filter(activo="1")
	
	return render(request, "Tipodocumento/index.html", {"tiposDocumento": TiposdeDocumento})

def deleteTipoDocumento(request, id):
	Tiposdocumento=Tipodocumento.objects.get(id=id)
	Tiposdocumento.activo="0"
	Tiposdocumento.estado="0"
	Tiposdocumento.save()
	return redirect("/documentType/")

def editTipoDocumento(request, id):
	Tiposdocumento=Tipodocumento.objects.get(id=id) 
	return render(request,'Tipodocumento/form.html', {"tipoDocumento": Tiposdocumento})

def modifyTipoDocumento(request, id):
	documento = request.POST.get('Documento',False)
	descripcion =request.POST.get('Descripcion',False)
	obs =request.POST.get('Obs',False)
	Tiposdocumento=Tipodocumento.objects.get(id=id)
	Tiposdocumento.documento=documento
	Tiposdocumento.descripcion=descripcion
	Tiposdocumento.obs=obs
	Tiposdocumento.fechamodifica=datetime.datetime.now()
	Tiposdocumento.idusermodifica= request.user.id
	Tiposdocumento.save()
	return redirect("/documentType/")


def viewTipoDocumento(request, id):
	Tiposdocumento=Tipodocumento.objects.get(id=id)
	return render(request,'Tipodocumento/view.html', {"tipoDocumento": Tiposdocumento})

	


