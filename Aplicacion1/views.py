
import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from xml.dom.minidom import Document
from Aplicacion1.models import Tipodocumento, Tipodocori, Mareasori, Mfactor, Muserrol, Muser, Ipersona, Tipopersona, Mprocedencia, Mubigeo
from django.template import RequestContext
from django.contrib import messages	
import datetime,socket
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 

delete_state="3"
exist_state="1"


def signup(request):
    return render(request, 'paginas/auth/signup.html')

def signin(request):
	flag = 0
	if request.user.is_authenticated:
		return redirect('inicio')
    
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		try:
			user = User.objects.get(username=username)
		except:
			flag = 1
			messages.error(request, 'El usuario o contraseña no existe')
            
		user = authenticate(request, username=username, password=password)

		if flag != 1:
			if user is not None:
				login(request, user)
				try:
					return redirect(request.GET.get('next'))
				except:
					return redirect('inicio')

			else:
				messages.error(request, 'El usuario o contraseña no existe')
	
	return render(request, 'paginas/auth/signin.html')
    #return render(request, 'paginas/auth/signin.html')

@login_required(login_url='signin')
def logoutUser(request):
    logout(request)
    return redirect('signin')

# Create your views here.


@login_required(login_url='signin')
def inicio(request):
	return render(request, 'paginas/index.html')


@login_required(login_url='signin')
def registerTipoDocumento(request):
	return render(request,'paginas/type_doc/add.html')

@login_required(login_url='signin')
def listTipoDocumento(request):
    TiposdeDocumento=Tipodocumento.objects.filter(activo="1")

    return render(request, "paginas/type_doc/list.html", {"tiposDocumento": TiposdeDocumento})

@login_required(login_url='signin')
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

		maqcrea=socket.gethostbyname(socket.gethostname()),
		maqmodifica=socket.gethostbyname(socket.gethostname()),


		)
	messages.success(request, "Documento guardado correctamente")
	return redirect("/documentType/",  RequestContext(request))

@login_required(login_url='signin')
def deleteTipoDocumento(request, id):
	Tiposdocumento=Tipodocumento.objects.get(id=id)
	Tiposdocumento.activo="0"
	Tiposdocumento.estado="3"
	Tiposdocumento.save()
	return redirect("/documentType/")

@login_required(login_url='signin')
def editTipoDocumento(request, id):
	Tiposdocumento=Tipodocumento.objects.get(id=id) 
	return render(request,'paginas/type_doc/add.html', {"tipoDocumento": Tiposdocumento})

@login_required(login_url='signin')
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

	Tiposdocumento.maqmodifica=socket.gethostbyname(socket.gethostname()),

	messages.success(request, "Documento editado correctamente")
	return redirect("/documentType/")


@login_required(login_url='signin')
def viewTipoDocumento(request, id):
	Tiposdocumento=Tipodocumento.objects.get(id=id)
	return render(request,'paginas/type_doc/view.html', {"tipoDocumento": Tiposdocumento})



#Tipo de documento ORI

@login_required(login_url='signin')
def registerTipoDocumentoORI(request):
	return render(request,'paginas/tipo_doc_ori/add.html')

@login_required(login_url='signin')
def listTipoDocumentoORI(request):
    TiposdeDocumentoORI=Tipodocori.objects.filter(activo="1")

    return render(request, "paginas/tipo_doc_ori/list.html", {"tiposDocumentoORI": TiposdeDocumentoORI})

@login_required(login_url='signin')
def createTipoDocumentoORI(request):
	
	documento = request.POST.get('Documento',False)
	descripcion =request.POST.get('Descripcion',False)
	obs = request.POST.get('Obs',False)
	grupo = request.POST.get('Grupo',False)
	TiposdeDocumentoORI = Tipodocori.objects.create(
		documento=documento,
		descripcion=descripcion,
		grupo = grupo,
		activo= "1",
		estado="1",
		obs=obs,
		fechacrea= datetime.datetime.now(),
		fechamodifica=datetime.datetime.now(),
		idusercrea= request.user.id,
		idusermodifica= request.user.id,
		maqcrea=socket.gethostbyname(socket.gethostname()),
		maqmodifica=socket.gethostbyname(socket.gethostname()),


		)
	messages.success(request, "Documento guardado correctamente")
	return redirect("/documentTypeORI/",  RequestContext(request))

@login_required(login_url='signin')
def deleteTipoDocumentoORI(request, id):
	TiposdocumentoORI=Tipodocori.objects.get(id=id)
	TiposdocumentoORI.activo="0"
	TiposdocumentoORI.estado="3"
	TiposdocumentoORI.save()
	return redirect("/documentTypeORI/")

@login_required(login_url='signin')
def editTipoDocumentoORI(request, id):
	TiposdocumentoORI= Tipodocori.objects.get(id=id) 
	return render(request,'paginas/tipo_doc_ori/add.html', {"tipoDocumentoORI": TiposdocumentoORI})

@login_required(login_url='signin')
def modifyTipoDocumentoORI(request, id):
	documentoORI = request.POST.get('Documento',False)
	descripcion =request.POST.get('Descripcion',False)
	obs =request.POST.get('Obs',False)
	grupo = request.POST.get('Grupo',False)
	TiposdocumentoORI=Tipodocori.objects.get(id=id)
	TiposdocumentoORI.documento=documentoORI
	TiposdocumentoORI.descripcion=descripcion
	TiposdocumentoORI.grupo=grupo
	TiposdocumentoORI.obs=obs
	TiposdocumentoORI.fechamodifica=datetime.datetime.now()
	TiposdocumentoORI.idusermodifica= request.user.id
	TiposdocumentoORI.maqmodifica=socket.gethostbyname(socket.gethostname())

	TiposdocumentoORI.save()
	return redirect("/documentTypeORI/")


@login_required(login_url='signin')
def viewTipoDocumentoORI(request, id):
	TiposdocumentoORI=Tipodocori.objects.get(id=id)
	return render(request,'paginas/tipo_doc_ori/view.html', {"tipoDocumentoORI": TiposdocumentoORI})





#Maestro Areas ORI

@login_required(login_url='signin')
def registerMAreasORI(request):
	return render(request,'paginas/m_areas_ori/add.html')

@login_required(login_url='signin')
def listMAreasORI(request):
    MAreasori=Mareasori.objects.filter(activo="1")

    return render(request, "paginas/m_areas_ori/list.html", {"MAreasori":  MAreasori})

@login_required(login_url='signin')
def createMAreasORI(request):
	
	MAreasori = Mareasori.objects.create(
		area=request.POST.get('area',False),
		grupo =request.POST.get('grupo',False),
		tipo=request.POST.get('tipo',False),
		encargado=request.POST.get('encargado',False),
		email=request.POST.get('email',False),
		nexo=request.POST.get('nexo',False),
		obs=request.POST.get('obs',False),
		activo= "1",
		estado="1",
		fechacrea= datetime.datetime.now(),
		fechamodifica=datetime.datetime.now(),
		idusercrea= request.user.id,
		idusermodifica= request.user.id,
		maqcrea=socket.gethostbyname(socket.gethostname()),
		maqmodifica=socket.gethostbyname(socket.gethostname()),


		)
	messages.success(request, "Area guardada correctamente")
	return redirect("/mAreasORI/",  RequestContext(request))

@login_required(login_url='signin')
def deleteMAreasORI(request, id):
	MAreasori=Mareasori.objects.get(id=id)
	MAreasori.activo="0"
	MAreasori.estado="3"
	MAreasori.save()
	return redirect("/mAreasORI/")

@login_required(login_url='signin')
def editMAreasORI(request, id):
	MAreasori= Mareasori.objects.get(id=id) 
	return render(request,'paginas/m_areas_ori/add.html', {"MAreaORI": MAreasori})

@login_required(login_url='signin')
def modifyMAreasORI(request, id):
	
	MAreasori=Mareasori.objects.get(id=id)
	MAreasori.area=request.POST.get('area',False)
	MAreasori.grupo =request.POST.get('grupo',False)
	MAreasori.tipo=request.POST.get('tipo',False)
	MAreasori.encargado=request.POST.get('encargado',False)
	MAreasori.email=request.POST.get('email',False)
	MAreasori.nexo=request.POST.get('nexo',False)
	MAreasori.obs=request.POST.get('obs',False)
	MAreasori.fechamodifica=datetime.datetime.now()
	MAreasori.idusermodifica= request.user.id
	MAreasori.maqmodifica=socket.gethostbyname(socket.gethostname())

	MAreasori.save()
	messages.success(request, "Documento editado correctamente")
	return redirect("/mAreasORI/")


@login_required(login_url='signin')
def viewMAreasORI(request, id):
	MAreasori=Mareasori.objects.get(id=id)
	return render(request,'paginas/m_areas_ori/view.html', {"MAreaORI": MAreasori})







#Maestro Factor

@login_required(login_url='signin')
def registerMFactor(request):
	return render(request,'paginas/m_factor/add.html')

@login_required(login_url='signin')
def listMFactor(request):
    MFactor=Mfactor.objects.filter(activo="1")

    return render(request, "paginas/m_factor/list.html", {"MFactors":  MFactor})

@login_required(login_url='signin')
def createMFactor(request):
	
	MFactor = Mfactor.objects.create(
		idasunto=request.POST.get('idasunto',False),
		asunto=request.POST.get('asunto',False),
		idfactor=request.POST.get('idfactor',False),
		factor=request.POST.get('factor',False),
		idsubfactor=request.POST.get('idsubfactor',False),
		subfactor=request.POST.get('subfactor',False),
		historial =request.POST.get('historial',False),
		grupo =request.POST.get('grupo',False),
		obs=request.POST.get('obs',False),
		activo= "1",
		estado="1",
		fechacrea= datetime.datetime.now(),
		fechamodifica=datetime.datetime.now(),
		idusercrea= request.user.id,
		idusermodifica= request.user.id,
		maqcrea=socket.gethostbyname(socket.gethostname()),
		maqmodifica=socket.gethostbyname(socket.gethostname()),


		)
	messages.success(request, "Factor guardado correctamente")
	return redirect("/mFactor/",  RequestContext(request))

@login_required(login_url='signin')
def deleteMFactor(request, id):
	MFactor=Mfactor.objects.get(id=id)
	MFactor.activo="0"
	MFactor.estado="3"
	MFactor.save()
	return redirect("/mFactor/")

@login_required(login_url='signin')
def editMFactor(request, id):
	MFactor= Mfactor.objects.get(id=id) 
	return render(request,'paginas/m_factor/add.html', {"MFactor": MFactor})

@login_required(login_url='signin')
def modifyMFactor(request, id):
	
	MFactor=Mfactor.objects.get(id=id)
	MFactor.idasunto=request.POST.get('idasunto',False)
	MFactor.asunto=request.POST.get('asunto',False)
	MFactor.idfactor=request.POST.get('idfactor',False)
	MFactor.factor=request.POST.get('factor',False)
	MFactor.idsubfactor=request.POST.get('idsubfactor',False)
	MFactor.subfactor=request.POST.get('subfactor',False)
	MFactor.historial =request.POST.get('historial',False)
	MFactor.grupo =request.POST.get('grupo',False)
	MFactor.obs=request.POST.get('obs',False)
	MFactor.fechamodifica=datetime.datetime.now()
	MFactor.idusermodifica= request.user.id
	MFactor.maqmodifica=socket.gethostbyname(socket.gethostname())
	MFactor.save()
	messages.success(request, "Factore editado correctamente")
	return redirect("/mFactor/")


@login_required(login_url='signin')
def viewMFactor(request, id):
	MFactor=Mfactor.objects.get(id=id)
	return render(request,'paginas/m_factor/view.html', {"MFactor": MFactor})





#Maestro User Rol

@login_required(login_url='signin')
def registerMUserRol(request):
	return render(request,'paginas/m_user_rol/add.html')

@login_required(login_url='signin')
def listMUserRol(request):
    MUserRol=Muserrol.objects.filter(activo="1")

    return render(request, "paginas/m_user_rol/list.html", {"MUsersRols":  MUserRol})

@login_required(login_url='signin')
def createMUserRol(request):
	
	MUserRol = Muserrol.objects.create(
		
		rol =request.POST.get('rol',False),
		descripcion =request.POST.get('descripcion',False),
		obs=request.POST.get('obs',False),
		activo= "1",
		estado="1",
		fechacrea= datetime.datetime.now(),
		fechamodifica=datetime.datetime.now(),
		idusercrea= request.user.id,
		idusermodifica= request.user.id,
		maqcrea=socket.gethostbyname(socket.gethostname()),
		maqmodifica=socket.gethostbyname(socket.gethostname()),


		)
	messages.success(request, "Nuevo rol guardado correctamente")

	return redirect("/mUserRol/",  RequestContext(request))

@login_required(login_url='signin')
def deleteMUserRol(request, id):
	MUserRol=Muserrol.objects.get(id=id)
	MUserRol.activo="0"
	MUserRol.estado="3"
	MUserRol.save()
	return redirect("/mUserRol/")

@login_required(login_url='signin')
def editMUserRol(request, id):
	MUserRol= Muserrol.objects.get(id=id) 
	return render(request,'paginas/m_user_rol/add.html', {"MUserRol": MUserRol})

@login_required(login_url='signin')
def modifyMUserRol(request, id):
	
	MUserRol=Muserrol.objects.get(id=id)
	MUserRol.rol =request.POST.get('rol',False)
	MUserRol.descripcion =request.POST.get('descripcion',False)
	MUserRol.obs=request.POST.get('obs',False)
	MUserRol.fechamodifica=datetime.datetime.now()
	MUserRol.idusermodifica= request.user.id
	MUserRol.maqmodifica=socket.gethostbyname(socket.gethostname())
	MUserRol.save()
	messages.success(request, "Rol de usuario editado correctamente")
	return redirect("/mUserRol/")


@login_required(login_url='signin')
def viewMUserRol(request, id):
	MUserRol=Muserrol.objects.get(id=id)
	return render(request,'paginas/m_user_rol/view.html', {"MUserRol": MUserRol})





#Maestro User

@login_required(login_url='signin')
def registerMUser(request):
	return render(request,'paginas/m_user/add.html',{"Roles": Muserrol.objects.filter(activo="1")})

@login_required(login_url='signin')
def listMUser(request):
    MUser=Muser.objects.filter(activo="1")
    return render(request, "paginas/m_user/list.html", {"MUsers":  MUser})

@login_required(login_url='signin')
def createMUser(request):
	
	MUser = Muser.objects.create(
		
		cip =request.POST.get('cip',False),
		codigo =request.POST.get('codigo',False),
		apepaterno =request.POST.get('apepaterno',False),
		apematerno =request.POST.get('apematerno',False),
		nombres =request.POST.get('nombres',False),
		email =request.POST.get('email',False),
		idrol = Muserrol.objects.get(id=request.POST.get('idrol',False)),
		motivobaja =request.POST.get('motivobaja',False),
		obs=request.POST.get('obs',False),
		activo= "1",
		estado="1",
		fechacrea= datetime.datetime.now(),
		fechamodifica=datetime.datetime.now(),
		idusercrea= request.user.id,
		idusermodifica= request.user.id,
		maqcrea=socket.gethostbyname(socket.gethostname()),
		maqmodifica=socket.gethostbyname(socket.gethostname()),


		)
	messages.success(request, "Nuevo usuario guardado correctamente")
	return redirect("/mUser/",  RequestContext(request))

@login_required(login_url='signin')
def deleteMUser(request, id):
	MUser=Muser.objects.get(id=id)
	MUser.activo="0"
	MUser.estado="3"
	MUser.save()
	return redirect("/mUser/")

@login_required(login_url='signin')
def editMUser(request, id):
	MUser= Muser.objects.get(id=id) 
	return render(request,'paginas/m_user/add.html', {"MUser": MUser,"Roles": Muserrol.objects.filter(activo="1")})

@login_required(login_url='signin')
def modifyMUser(request, id):
	
	MUser=Muser.objects.get(id=id)
	MUser.cip =request.POST.get('cip',False)
	MUser.codigo =request.POST.get('codigo',False)
	MUser.apepaterno =request.POST.get('apepaterno',False)
	MUser.apematerno =request.POST.get('apematerno',False)
	MUser.nombres =request.POST.get('nombres',False)
	MUser.email =request.POST.get('email',False)
	MUser.idrol = Muserrol.objects.get(id=request.POST.get('idrol',False))
	MUser.motivobaja =request.POST.get('motivobaja',False)

	MUser.obs=request.POST.get('obs',False)
	MUser.fechamodifica=datetime.datetime.now()
	MUser.idusermodifica= request.user.id
	MUser.maqmodifica=socket.gethostbyname(socket.gethostname())
	MUser.save()
	messages.success(request, "Usuario editado correctamente")
	return redirect("/mUser/")


@login_required(login_url='signin')
def viewMUser(request, id):
	MUser=Muser.objects.get(id=id)
	return render(request,'paginas/m_user/view.html', {"MUser": MUser})





#Maestro IPersona

@login_required(login_url='signin')
def registerIPersona(request):
	departamentos = Mubigeo.objects.all().values('iddepartamento',
                                                 'departamento').distinct()

	return render(request,'paginas/i_persona/add.html', 
	{"Tipopersona":Tipopersona.objects.filter(activo="1"),
	"Mprocedencia":Mprocedencia.objects.filter(activo="1"),
	"Tipodocumento":Tipodocumento.objects.filter(activo="1"),
	"Mubigeo":Mubigeo.objects.filter(activo="1"),
	"d": departamentos
	})

@login_required(login_url='signin')
def listIPersona(request):
    IPersona=Ipersona.objects.filter(activo="1")
    return render(request, "paginas/i_persona/list.html", {"IPersonas":  IPersona})

@login_required(login_url='signin')
def createIPersona(request):
	
	IPersona = Ipersona.objects.create(
		idtipopersona = Tipopersona.objects.get(id=request.POST.get('idtipopersona',False)),
		idprocedencia =  Mprocedencia.objects.get(id=request.POST.get('idprocedencia',False)),
		idtipodocumento =  Tipodocumento.objects.get(id=request.POST.get('idtipodocumento',False)),
		idubigeo =  Mubigeo.objects.get(iddepartamento = request.POST.get('departamentos'), idprovincia=request.POST.get('provincias'),iddistrito=request.POST.get('ciudades') ),
		obs=request.POST.get('obs',False),
		activo= "1",
		estado="1",
		fechacrea= datetime.datetime.now(),
		fechamodifica=datetime.datetime.now(),
		idusercrea= request.user.id,
		idusermodifica= request.user.id,
		maqcrea=socket.gethostbyname(socket.gethostname()),
		maqmodifica=socket.gethostbyname(socket.gethostname()),


		)
	messages.success(request, "Nueva persona guardada correctamente")

	return redirect("/iPersona/",  RequestContext(request))

@login_required(login_url='signin')
def deleteIPersona(request, id):
	IPersona=Ipersona.objects.get(id=id)
	IPersona.activo="0"
	IPersona.estado="3"
	IPersona.save()
	return redirect("/iPersona/")

@login_required(login_url='signin')
def editIPersona(request, id):
	IPersona= Ipersona.objects.get(id=id) 
	return render(request,'paginas/i_persona/add.html', {"IPersona": IPersona,
	"Tipopersona":Tipopersona.objects.filter(activo="1"),
	"Mprocedencia":Mprocedencia.objects.filter(activo="1"),
	"Tipodocumento":Tipodocumento.objects.filter(activo="1"),
	"Mubigeo":Mubigeo.objects.filter(activo="1")})

@login_required(login_url='signin')
def modifyIPersona(request, id):
	
	IPersona=Ipersona.objects.get(id=id)
	IPersona.idtipopersona = Tipopersona.objects.get(id=request.POST.get('idtipopersona',False))
	IPersona.idprocedencia =  Mprocedencia.objects.get(id=request.POST.get('idprocedencia',False))
	IPersona.idtipodocumento =  Tipodocumento.objects.get(id=request.POST.get('idtipodocumento',False))
	IPersona.idubigeo =  Mubigeo.objects.get(id=request.POST.get('idubigeo',False))
	IPersona.obs=request.POST.get('obs',False)
	IPersona.fechamodifica=datetime.datetime.now()
	IPersona.idusermodifica= request.user.id
	IPersona.maqmodifica=socket.gethostbyname(socket.gethostname())
	IPersona.save()
	return redirect("/iPersona/")


@login_required(login_url='signin')
def viewIPersona(request, id):
	IPersona=Ipersona.objects.get(id=id)
	return render(request,'paginas/i_persona/view.html', {"IPersona": IPersona})

@login_required(login_url='signin')
def load_province(request):
    iddepartamento = request.GET.get('departamentoid')
    provincias = Mubigeo.objects.all().filter(
        iddepartamento=iddepartamento).values('idprovincia',
                                              'provincia').distinct()
    return render(request, 'paginas/i_persona/provinceSelect.html', {'provincias': provincias})


@login_required(login_url='signin')
def load_cities(request):
    iddepartamento = request.GET.get('departamentoid')
    idprovincia = request.GET.get('provinciaid')
    ciudades = Mubigeo.objects.all().filter(iddepartamento=iddepartamento,
                                            idprovincia=idprovincia)
    return render(request, 'paginas/i_persona/ciudadSelect.html', {'ciudad': ciudades})












