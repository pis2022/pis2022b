from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Iffaa(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey('Ipersona', models.DO_NOTHING, db_column='IdPersona')  # Field name made lowercase.
    nrodoc = models.CharField(db_column='NroDoc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idtipoffaa = models.ForeignKey('Tipoffaa', models.DO_NOTHING, db_column='IdTipoFFAA', blank=True, null=True)  # Field name made lowercase.
    carnet = models.CharField(db_column='Carnet', max_length=100)  # Field name made lowercase.
    grado = models.CharField(db_column='Grado', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idsitffaa = models.IntegerField(db_column='IdSitFFAA', blank=True, null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=300, blank=True, null=True)  # Field name made lowercase.
    observ = models.CharField(db_column='Observ', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase.
    archivo = models.CharField(db_column='Archivo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'IFFAA'


class Ipersona(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idtipopersona = models.ForeignKey('Tipopersona', models.DO_NOTHING, db_column='IdTipoPersona')  # Field name made lowercase.
    idprocedencia = models.ForeignKey('Mprocedencia', models.DO_NOTHING, db_column='IdProcedencia', blank=True, null=True)  # Field name made lowercase.
    idpais = models.ForeignKey('Mpais', models.DO_NOTHING, db_column='IdPais', blank=True, null=True)  # Field name made lowercase.
    idtipodocumento = models.ForeignKey('Tipodocumento', models.DO_NOTHING, db_column='IdTipoDocumento')  # Field name made lowercase.
    nrodoc = models.CharField(db_column='NroDoc', max_length=100)  # Field name made lowercase.
    otrodocumento = models.CharField(db_column='OtroDocumento', max_length=300, blank=True, null=True)  # Field name made lowercase.
    apepaterno = models.CharField(db_column='ApePaterno', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apematerno = models.CharField(db_column='ApeMaterno', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=100)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='FechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    natural = models.CharField(db_column='Natural', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idestadocivil = models.ForeignKey('Mestadocivil', models.DO_NOTHING, db_column='IdEstadoCivil', blank=True, null=True)  # Field name made lowercase.
    idgenero = models.ForeignKey('Mgenero', models.DO_NOTHING, db_column='IdGenero', blank=True, null=True)  # Field name made lowercase.
    foto = models.TextField(db_column='Foto', blank=True, null=True)  # Field name made lowercase.
    idubigeo = models.ForeignKey('Mubigeo', models.DO_NOTHING, db_column='IdUbigeo', blank=True, null=True)  # Field name made lowercase.
    domicilio = models.CharField(db_column='Domicilio', max_length=300, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=300, blank=True, null=True)  # Field name made lowercase.
    ocupacion = models.CharField(db_column='Ocupacion', max_length=300, blank=True, null=True)  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=300, blank=True, null=True)  # Field name made lowercase.
    idgradoinstruccion = models.ForeignKey('Mgradoinstruccion', models.DO_NOTHING, db_column='IdGradoInstruccion', blank=True, null=True)  # Field name made lowercase.
    profesion = models.CharField(db_column='Profesion', max_length=300, blank=True, null=True)  # Field name made lowercase.
    centroestudios = models.CharField(db_column='CentroEstudios', max_length=300, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=300, blank=True, null=True)  # Field name made lowercase.
    redessociales = models.CharField(db_column='RedesSociales', max_length=300, blank=True, null=True)  # Field name made lowercase.
    idfactor = models.ForeignKey('Mfactor', models.DO_NOTHING, db_column='IdFactor', blank=True, null=True)  # Field name made lowercase.
    tipoorganizacion = models.CharField(db_column='TipoOrganizacion', max_length=300, blank=True, null=True)  # Field name made lowercase.
    modalidaddelito = models.CharField(db_column='ModalidadDelito', max_length=300, blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=300, blank=True, null=True)  # Field name made lowercase.
    talla = models.DecimalField(db_column='Talla', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    peso = models.DecimalField(db_column='Peso', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    idraza = models.ForeignKey('Tiporaza', models.DO_NOTHING, db_column='IdRaza', blank=True, null=True)  # Field name made lowercase.
    idcontextura = models.ForeignKey('Tipocontextura', models.DO_NOTHING, db_column='IdContextura', blank=True, null=True)  # Field name made lowercase.
    caminada = models.CharField(db_column='Caminada', max_length=300, blank=True, null=True)  # Field name made lowercase.
    cicatrices = models.CharField(db_column='Cicatrices', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tatuajes = models.CharField(db_column='Tatuajes', max_length=300, blank=True, null=True)  # Field name made lowercase.
    habitos = models.CharField(db_column='Habitos', max_length=300, blank=True, null=True)  # Field name made lowercase.
    vicios = models.CharField(db_column='Vicios', max_length=300, blank=True, null=True)  # Field name made lowercase.
    defectos = models.CharField(db_column='Defectos', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase.
    archivo = models.TextField(db_column='Archivo', blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'IPersona'


class Ipolicia(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey(Ipersona, models.DO_NOTHING, db_column='IdPersona')  # Field name made lowercase.
    nrodoc = models.CharField(db_column='NroDoc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cip = models.IntegerField(db_column='CIP', unique=True)  # Field name made lowercase.
    idgrado = models.ForeignKey('Mgrado', models.DO_NOTHING, db_column='IdGrado', blank=True, null=True)  # Field name made lowercase.
    idsitpolicial = models.ForeignKey('Msitpolicial', models.DO_NOTHING, db_column='IdSitPolicial', blank=True, null=True)  # Field name made lowercase.
    idunidad = models.ForeignKey('Munidadespnp', models.DO_NOTHING, db_column='IdUnidad', blank=True, null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=300, blank=True, null=True)  # Field name made lowercase.
    observ = models.CharField(db_column='Observ', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase.
    archivo = models.CharField(db_column='Archivo', max_length=300, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'IPolicia'


class Mareasori(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=200)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    encargado = models.CharField(db_column='Encargado', max_length=200, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nexo = models.CharField(db_column='Nexo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MAreasORI'


class Mcalibrearma(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    calibre = models.CharField(db_column='Calibre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MCalibreArma'


class Mestado(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return "{} {}".format(self.id, self.nombre)

    class Meta:
        managed = True
        db_table = 'MEstado'


class Mestadocivil(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    estadocivil = models.CharField(db_column='EstadoCivil', max_length=50)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.


    def __str__(self):
        return "%s - %s" % (self.id, self.estadocivil)

    class Meta:
        managed = True
        db_table = 'MEstadoCivil'


class Mfactor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idasunto = models.IntegerField(db_column='IdAsunto', blank=True, null=True)  # Field name made lowercase.
    asunto = models.CharField(db_column='Asunto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idfactor = models.IntegerField(db_column='IdFactor', blank=True, null=True)  # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idsubfactor = models.IntegerField(db_column='IdSubFactor', blank=True, null=True)  # Field name made lowercase.
    subfactor = models.CharField(db_column='SubFactor', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    historial = models.CharField(db_column='Historial', max_length=200, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MFactor'


class Mgenero(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=20)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return "{} - {}".format(self.id, self.sexo)

    class Meta:
        managed = True
        db_table = 'MGenero'


class Mgrado(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codgrado = models.IntegerField(db_column='CodGrado', blank=True, null=True)  # Field name made lowercase.
    grado = models.CharField(db_column='Grado', max_length=50)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=100, blank=True, null=True)  # Field name made lowercase.
    jerarquia = models.CharField(db_column='Jerarquia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MGrado'


class Mgradoinstruccion(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    gradoinstruccion = models.CharField(db_column='GradoInstruccion', max_length=100)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MGradoInstruccion'


class Mpais(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paisiso = models.CharField(db_column='PaisISO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codigoiso = models.IntegerField(db_column='CodigoISO', blank=True, null=True)  # Field name made lowercase.
    alfa2 = models.CharField(db_column='Alfa2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    alfa3 = models.CharField(db_column='Alfa3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    continente = models.CharField(db_column='Continente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):

        # format 
        return "{} - {}".format(self.id, self.pais)

    class Meta:
        managed = True
        db_table = 'MPais'


class Mparentesco(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    parentesco = models.CharField(db_column='Parentesco', max_length=50, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MParentesco'


class Mprocedencia(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    procedencia = models.CharField(db_column='Procedencia', max_length=100)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=300, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return "{} - {}".format(self.id, self.procedencia)

    class Meta:
        managed = True
        db_table = 'MProcedencia'


class Msitpolicial(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sitpolicial = models.CharField(db_column='SitPolicial', max_length=30)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MSitPolicial'


class Mubigeo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    iddepartamento = models.IntegerField(db_column='IdDepartamento', blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='Departamento', max_length=30, blank=True, null=True)  # Field name made lowercase.
    idprovincia = models.IntegerField(db_column='IdProvincia', blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=30, blank=True, null=True)  # Field name made lowercase.
    iddistrito = models.IntegerField(db_column='IdDistrito', blank=True, null=True)  # Field name made lowercase.
    distrito = models.CharField(db_column='Distrito', max_length=50, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.id)
    class Meta:
        managed = True
        db_table = 'MUbigeo'


class Munidadespnp(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codarequipa = models.CharField(db_column='CodArequipa', max_length=4, blank=True, null=True)  # Field name made lowercase.
    codlima = models.IntegerField(db_column='CodLima', blank=True, null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=300, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=300, blank=True, null=True)  # Field name made lowercase.
    nombrecorto = models.CharField(db_column='NombreCorto', max_length=300, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=300, blank=True, null=True)  # Field name made lowercase.
    granunidad = models.CharField(db_column='GranUnidad', max_length=300, blank=True, null=True)  # Field name made lowercase.
    divisiones = models.CharField(db_column='Divisiones', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tipounidad = models.CharField(db_column='TipoUnidad', max_length=300, blank=True, null=True)  # Field name made lowercase.
    idubicacion = models.IntegerField(db_column='IdUbicacion', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=300, blank=True, null=True)  # Field name made lowercase.
    latitud = models.CharField(db_column='Latitud', max_length=300, blank=True, null=True)  # Field name made lowercase.
    longitud = models.CharField(db_column='Longitud', max_length=300, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=300, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=300, blank=True, null=True)  # Field name made lowercase.
    correoinst = models.CharField(db_column='CorreoInst', max_length=300, blank=True, null=True)  # Field name made lowercase.
    emailalterno = models.CharField(db_column='EmailAlterno', max_length=300, blank=True, null=True)  # Field name made lowercase.
    redsocial = models.CharField(db_column='RedSocial', max_length=300, blank=True, null=True)  # Field name made lowercase.
    contacto = models.CharField(db_column='Contacto', max_length=300, blank=True, null=True)  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    codhistorico = models.CharField(db_column='CodHistorico', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MUnidadesPNP'


class Muser(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cip = models.CharField(db_column='CIP', unique=True, max_length=8)  # Field name made lowercase.
    codigo = models.TextField(db_column='Codigo')  # Field name made lowercase.
    idgrado = models.IntegerField(db_column='IdGrado', blank=True, null=True)  # Field name made lowercase.
    grado = models.CharField(db_column='Grado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apepaterno = models.CharField(db_column='ApePaterno', max_length=60, blank=True, null=True)  # Field name made lowercase.
    apematerno = models.CharField(db_column='ApeMaterno', max_length=60, blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=100)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.

    imagen = models.ImageField(db_column='Imagen', blank=True, null=True)  # Field name made lowercase.

    administrador = models.IntegerField(db_column='Administrador', blank=True, null=True)  # Field name made lowercase.
    idrol = models.ForeignKey('Muserrol', models.DO_NOTHING, db_column='IdRol', blank=True, null=True)  # Field name made lowercase.
    idnivel = models.IntegerField(db_column='IdNivel', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    motivobaja = models.CharField(db_column='MotivoBaja', max_length=200, blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase.
    femodificapass = models.DateTimeField(db_column='FeModificaPass', blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = True
        db_table = 'MUser'


class Musermodulo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    modulo = models.CharField(db_column='Modulo', max_length=10)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MUserModulo'


class Museroperacion(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    operacion = models.CharField(db_column='Operacion', max_length=10)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idmodulo = models.IntegerField(db_column='IdModulo', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MUserOperacion'


class Muserpermisos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idrol = models.IntegerField(db_column='IdRol', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    idmodulo = models.IntegerField(db_column='IdModulo', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MUserPermisos'


class Muserrol(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    rol = models.CharField(db_column='Rol', max_length=50)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.rol

    class Meta:
        managed = True
        db_table = 'MUserRol'


class Rfamiliares(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey(Ipersona, models.DO_NOTHING, db_column='IdPersona')  # Field name made lowercase.
    nrodoc = models.CharField(db_column='NroDoc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idparentesco = models.ForeignKey(Mparentesco, models.DO_NOTHING, db_column='IdParentesco', blank=True, null=True)  # Field name made lowercase.
    apepaterno = models.CharField(db_column='ApePaterno', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apematerno = models.CharField(db_column='ApeMaterno', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombresall = models.CharField(db_column='NombresAll', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dnifamiliar = models.CharField(db_column='DniFamiliar', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ocupacion = models.CharField(db_column='Ocupacion', max_length=300, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=300, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'RFamiliares'


class Rfiliacionpolitica(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey(Ipersona, models.DO_NOTHING, db_column='IdPersona')  # Field name made lowercase.
    nrodoc = models.CharField(db_column='NroDoc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idtipoorganizacion = models.ForeignKey('Tipoorgpolitica', models.DO_NOTHING, db_column='IdTipoOrganizacion', blank=True, null=True)  # Field name made lowercase.
    organizacion = models.CharField(db_column='Organizacion', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tintepolitico = models.CharField(db_column='TintePolitico', max_length=300, blank=True, null=True)  # Field name made lowercase.
    cargoocupa = models.CharField(db_column='CargoOcupa', max_length=300, blank=True, null=True)  # Field name made lowercase.
    anio = models.CharField(db_column='Anio', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase.
    archivo = models.CharField(db_column='Archivo', max_length=300, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'RFiliacionPolitica'


class Rpenales(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey(Ipersona, models.DO_NOTHING, db_column='IdPersona')  # Field name made lowercase.
    nrodoc = models.CharField(db_column='NroDoc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombreepenal = models.CharField(db_column='NombreEPenal', max_length=300, blank=True, null=True)  # Field name made lowercase.
    direccionpenal = models.CharField(db_column='DireccionPenal', max_length=300, blank=True, null=True)  # Field name made lowercase.
    procedencia = models.CharField(db_column='Procedencia', max_length=300, blank=True, null=True)  # Field name made lowercase.
    nroingresos = models.IntegerField(db_column='NroIngresos', blank=True, null=True)  # Field name made lowercase.
    motivoingreso = models.CharField(db_column='MotivoIngreso', max_length=300, blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.DateTimeField(db_column='FechaIngreso', blank=True, null=True)  # Field name made lowercase.
    situacionjuridica = models.CharField(db_column='SituacionJuridica', max_length=300, blank=True, null=True)  # Field name made lowercase.
    delitogenerico = models.CharField(db_column='DelitoGenerico', max_length=300, blank=True, null=True)  # Field name made lowercase.
    delitoespecifico = models.CharField(db_column='DelitoEspecifico', max_length=300, blank=True, null=True)  # Field name made lowercase.
    autoridadsentencia = models.CharField(db_column='AutoridadSentencia', max_length=300, blank=True, null=True)  # Field name made lowercase.
    salasentencia = models.CharField(db_column='SalaSentencia', max_length=300, blank=True, null=True)  # Field name made lowercase.
    docsentencia = models.CharField(db_column='DocSentencia', max_length=300, blank=True, null=True)  # Field name made lowercase.
    fechasentencia = models.DateTimeField(db_column='FechaSentencia', blank=True, null=True)  # Field name made lowercase.
    agraviado = models.CharField(db_column='Agraviado', max_length=300, blank=True, null=True)  # Field name made lowercase.
    cantanios = models.IntegerField(db_column='CantAnios', blank=True, null=True)  # Field name made lowercase.
    cantmeses = models.IntegerField(db_column='CantMeses', blank=True, null=True)  # Field name made lowercase.
    cantdias = models.IntegerField(db_column='CantDias', blank=True, null=True)  # Field name made lowercase.
    autoridadlibera = models.CharField(db_column='AutoridadLibera', max_length=300, blank=True, null=True)  # Field name made lowercase.
    salalibera = models.CharField(db_column='SalaLibera', max_length=300, blank=True, null=True)  # Field name made lowercase.
    docsalida = models.CharField(db_column='DocSalida', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tipolibertad = models.CharField(db_column='TipoLibertad', max_length=300, blank=True, null=True)  # Field name made lowercase.
    fechalibertad = models.DateTimeField(db_column='FechaLibertad', blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase.
    archivo = models.CharField(db_column='Archivo', max_length=300, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'RPenales'


class Tipocontextura(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contextura = models.CharField(db_column='Contextura', max_length=100)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=300, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TipoContextura'


class Tipodocori(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    documento = models.CharField(db_column='Documento', max_length=100)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TipoDocORI'


class Tipodocumento(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    documento = models.CharField(db_column='Documento', max_length=100)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return "{} - {}".format(self.id, self.documento)

    class Meta:
        managed = True
        db_table = 'TipoDocumento'


class Tipoffaa(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tipoffaa = models.CharField(db_column='TipoFFAA', max_length=100)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=300, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=300, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TipoFFAA'


class Tipoorgpolitica(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    organizacion = models.CharField(db_column='Organizacion', max_length=100)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TipoOrgPolitica'


class Tipopersona(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tipopersona = models.CharField(db_column='TipoPersona', max_length=50)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return "{} - {}".format(self.id, self.tipopersona)

    class Meta:
        managed = True
        db_table = 'TipoPersona'


class Tiporaza(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    raza = models.CharField(db_column='Raza', max_length=30)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=300, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.IntegerField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.IntegerField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.DateTimeField(db_column='FechaCrea', blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateTimeField(db_column='FechaModifica', blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TipoRaza'
"""

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'

"""
class Unidad(models.Model):
    #id = models.FloatField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codarequipa = models.CharField(db_column='CodArequipa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codlima = models.FloatField(db_column='CodLima', blank=True, null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombrecorto = models.CharField(db_column='NombreCorto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    granunidad = models.CharField(db_column='GranUnidad', max_length=255, blank=True, null=True)  # Field name made lowercase.
    divisiones = models.CharField(db_column='Divisiones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipounidad = models.CharField(db_column='TipoUnidad', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idubicacion = models.FloatField(db_column='IdUbicacion', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    latitud = models.CharField(db_column='LATITUD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitud = models.CharField(db_column='LONGITUD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=255, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=255, blank=True, null=True)  # Field name made lowercase.
    correoinst = models.CharField(db_column='CorreoInst', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailalterno = models.CharField(db_column='EmailAlterno', max_length=255, blank=True, null=True)  # Field name made lowercase.
    redsocial = models.CharField(db_column='RedSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contacto = models.CharField(db_column='Contacto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orden = models.FloatField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    codhistorico = models.CharField(db_column='CodHistorico', max_length=255, blank=True, null=True)  # Field name made lowercase.
    activo = models.FloatField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    estado = models.FloatField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idusercrea = models.FloatField(db_column='IdUserCrea', blank=True, null=True)  # Field name made lowercase.
    idusermodifica = models.FloatField(db_column='IdUserModifica', blank=True, null=True)  # Field name made lowercase.
    fechacrea = models.CharField(db_column='FechaCrea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.CharField(db_column='FechaModifica', max_length=255, blank=True, null=True)  # Field name made lowercase.
    maqcrea = models.CharField(db_column='MaqCrea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    maqmodifica = models.CharField(db_column='MaqModifica', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'unidad'
