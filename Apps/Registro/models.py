from django.db import models

# Create your models here.


class Universidad(models.Model):
    id = models.AutoField(primary_key=True, unique=True,
                          blank=False, null=False)
    nombre = models.CharField(max_length=60, blank=False, null=False)
    nombre_corto = models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        verbose_name = 'Universidad'
        verbose_name_plural = 'Universidades'
        ordering = ['id','nombre','nombre_corto']

    def __str__(self):
        return self.nombre_corto

class Facultad(models.Model):
    id = models.AutoField(primary_key=True, unique=True,
                          blank=False, null=False)
    universidad= models.ForeignKey(Universidad, blank=False,null=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60, blank=False, null=False)
    nombre_corto = models.CharField(max_length=20, blank=False, null=False)
    especialidad = models.CharField(max_length=60, blank=False, null=False)

    class Meta:
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'
        ordering = ['id','universidad','nombre','nombre_corto','especialidad']

    def __str__(self):
        return self.nombre_corto + " "+self.especialidad


class Carrera(models.Model):
    id = models.AutoField(primary_key=True, unique=True,
                          blank=False, null=False)
    nombre = models.CharField(max_length=60, blank=False, null=False)
    nombre_corto = models.CharField(max_length=20, blank=False, null=False)
    facultad = models.ForeignKey(
        Facultad, blank=False, null=False, on_delete=models.CASCADE)
    Anho = (("1", "1er Año"), ("2", "2do Año"), ("3", "3er Año"), ("4", "4to Año"),
            ("5", "5to Año"), ("6", "6to Año"), ("7", "7mo Año"), ("8", "8vo Año"))
    año = models.CharField(choices=Anho, max_length=1,
                            blank=False, null=False)

    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
        ordering = ['id','nombre','nombre_corto','facultad','año']

    def __str__(self):
        return self.facultad.nombre_corto+" "+self.nombre_corto+" "+self.año+"° Año"




class Alumno(models.Model):
    id = models.AutoField(primary_key=True, unique=True,
                          blank=False, null=False)
    nombres = models.CharField(max_length=50, blank=False, null=False)
    apellidos = models.CharField(max_length=50, blank=False, null=False)
    SEXOS = (("M", "Masculino"), ("F", "Femenino"))
    sexo = models.CharField(choices=SEXOS, max_length=1,
                            blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(
        "Fecha de creación", auto_now=True, auto_now_add=False)
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['id','nombres','apellidos','sexo','descripcion','carrera']

    def __str__(self):
        return self.nombres+" "+self.apellidos+" "+self.carrera.nombre_corto+" "+self.carrera.año+"° Año"

class DeporteMasculino(models.Model):
    id = models.AutoField(primary_key=True, unique=True,
                          blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name: 'Deporte Masculino'
        verbose_name_plural: 'Deportes Masculinos'
        ordering = ['id','nombre']

    def __str__(self):
        return self.nombre+" (Masculino)"


class DeporteFemenino(models.Model):
    id = models.AutoField(primary_key=True, unique=True,
                          blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name: 'Deporte Femenino'
        verbose_name_plural: 'Deportes Femeninos'
        ordering = ['id','nombre']

    def __str__(self):
        return self.nombre+" (Femenino)"

class Deporte(models.Model):
    id = models.AutoField(primary_key=True, blank=False,
                          null=False, unique=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    masculino = models.ForeignKey(
        DeporteMasculino,blank=True, null=True,  on_delete=models.CASCADE)
    femenino = models.ForeignKey(
        DeporteFemenino,blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name: 'Deporte'
        verbose_name_plural: 'Deportes'
        ordering = ['id','alumno','masculino','femenino']

    def verif(self):
        if self.masculino :
            return self.alumno.nombres +" "+self.alumno.apellidos+" participa en: " + self.masculino.nombre+" (Masculino)"
        elif self.femenino: 
            return self.alumno.nombres +" "+self.alumno.apellidos+" participa en: " + self.femenino.nombre+" (Femenino)"
        else :
            return self.alumno.nombres +" "+self.alumno.apellidos+" participa en: Ningun Deporte"

           
    def __str__(self):
        return self.verif()



# class Libro(models.Model):
#     id = models.AutoField(primary_key=True, unique=True,
#                           blank=False, null=False)
#     titulo = models.CharField(max_length=30, blank=False, null=False)
#     fecha_publicacion = models.DateField(
#         "Fecha de publicación", blank=False, null=False,auto_now=False, auto_now_add=False)
#     autor = models.ManyToManyField(Autor)
#     fecha_creacion = models.DateField(
#         "Fecha de creación", auto_now=True, auto_now_add=False)
#     estado= models.BooleanField('Estado',default= True)

#     class Meta:
#         verbose_name = 'Libro'
#         verbose_name_plural = 'Libros'
#         ordering = ['-id']

#     def __str__(self):
#         return self.titulo
